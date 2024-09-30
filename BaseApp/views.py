# BaseApp/views.py

from typing import Any

from django.views.generic.base import TemplateView

from BaseApp.utils import get_module_logger

module_logger = get_module_logger("views", __file__)


class BasePage(TemplateView):
    """
    A default base page to inherit from.

    A page represents a single page in the application.
    One page can be used to represent multiple views with
    @staticmethods and @require_htmx.

    Each view within a page represents an interchangeable
    component that fits within a page.
    """
    template_name = 'BaseApp/base.html'
    page_title = "Base"
    page_description = "This is a base for all pages."
    page_disclaimer = ""

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_description'] = self.page_description
        context['page_disclaimer'] = self.page_disclaimer
        return context


class HomePage(BasePage):
    template_name = 'BaseApp/home.html'
    page_title = "Home"
    page_description = "This is the home page."
    page_disclaimer = "This is the home page."
