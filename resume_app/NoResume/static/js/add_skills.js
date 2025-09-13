let totalFormsInput = document.getElementById('id_form-TOTAL_FORMS');
let totalForms = parseInt(totalFormsInput.value, 10);

document.getElementById('add_skill').addEventListener('click', function () {
    let formContainer = document.getElementById('formset_container');
    let newForm = formContainer.children[0].cloneNode(true);

    // Update the form index in the new form's fields
    newForm.innerHTML = newForm.innerHTML.replace(/form-(\d+)-/g, `form-${totalForms}-`);

    // Clear all input, select, and textarea values in the cloned form
    newForm.querySelectorAll("input, select, textarea").forEach(input => {
        if (input.tagName === "SELECT") {
            input.selectedIndex = 0;
        } else {
            input.value = "";
        }
    });

    formContainer.appendChild(newForm);

    totalForms++;
    totalFormsInput.value = totalForms;
});