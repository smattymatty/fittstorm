import os
import re

from functools import wraps
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.template import Template, RequestContext
from django.template.loader import render_to_string, get_template
from django.shortcuts import redirect
from django.urls import reverse

from loguru import logger

from .constants import LOG_FORMAT


def get_parent_folder(path: str):
    """
    Returns the parent folder of a given path.
        - path: The path to get the parent folder of.
    """
    return os.path.dirname(path)


def get_module_logger(module_name: str, file: str):
    """
    Returns a logger for a specific module.
        - module_name: The name of the module.
        - file: The file path to the log file.
    """
    log_file_path = os.path.join(get_parent_folder(
        file), "logs", f"{module_name}.log")
    module_logger = logger.bind(name=module_name)
    module_logger.add(
        log_file_path,
        format=LOG_FORMAT,
        level="DEBUG",
        filter=lambda record: record["extra"].get("name") == module_name,
        rotation="10 MB",
        compression="zip",
    )
    return module_logger


def join_paths(*paths):
    """
    Joins multiple paths into a single path, handling different OS path separators.
    """
    return os.path.join(*paths)


def check_htmx(
    request: HttpRequest,
    part_template_name: str,
    context: dict = None,
    base_template: str = 'BaseApp/pages/generic_page.html'
) -> HttpResponse:
    """
    Checks if the request is an HTMX request and returns the appropriate response.

    If the request is not HTMX, it will build a generic page with the part filling the content.

    Example usage:
        ( at the end of a view function )
        return HttpResponse(
            check_htmx(
                request, 
                'workouts_app/workout_user_list.html',
                context
                )
            )
    """
    if context is None:
        context = {}

    if request.htmx:
        # For HTMX requests, render only the part
        return render_to_string(part_template_name, context, request=request)
    else:
        # For non-HTMX requests, inject the part into the full template
        # Step 1: Get the base template content
        base_template_content = get_template(base_template).template.source

        # Step 2 & 3: Find the page_content block and build the include tag
        include_tag = "{% include '" + part_template_name + "' %}"

        # Step 4: Inject the include tag into the page_content block
        pattern = r"{% block page_content %}.*?{% endblock %}"
        replacement = f"{{% block page_content %}}{include_tag}{{% endblock %}}"
        modified_template_content = re.sub(
            pattern, replacement, base_template_content, flags=re.DOTALL)

        # Step 5: Create a Template object and render it with RequestContext
        template = Template(modified_template_content)
        request_context = RequestContext(request, context)
        return HttpResponse(template.render(request_context))


def parse_config(config_string):
    """
    Parses a configuration string into a dictionary.
    Example usage:
        config_string = "key1:value1, key2:value2"
        config_dict = parse_config(config_string)
        print(config_dict)
        # Output: {'key1': 'value1', 'key2': 'value2'}
    """
    if not config_string:
        return {}
    config_dict = {}
    for item in config_string.split():
        if ':' in item:
            key, value = item.split(':', 1)
            config_dict[key.strip()] = value.strip()
    return config_dict
