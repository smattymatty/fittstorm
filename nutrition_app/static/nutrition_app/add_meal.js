document.addEventListener('DOMContentLoaded', function() {
    const ingredientFormset = document.getElementById('ingredient-formset');
    const addIngredientBtn = document.getElementById('add-ingredient');
    let formCount = {{ ingredient_formset.total_form_count }};

    addIngredientBtn.addEventListener('click', function() {
        const newForm = ingredientFormset.querySelector('.ba-ingredient-form').cloneNode(true);
        newForm.innerHTML = newForm.innerHTML.replace(/form-(\d+)/g, `form-${formCount}`);
        ingredientFormset.appendChild(newForm);
        formCount++;
        document.getElementById('id_form-TOTAL_FORMS').value = formCount;
    });

    ingredientFormset.addEventListener('click', function(e) {
        if (e.target.classList.contains('ba-remove-ingredient')) {
            e.target.closest('.ba-ingredient-form').remove();
            formCount--;
            document.getElementById('id_form-TOTAL_FORMS').value = formCount;
        }
    });
});