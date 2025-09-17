let totalFormsInput = document.getElementById('id_form-TOTAL_FORMS');
const formsetContainer = document.getElementById('formset_container');
let totalForms = parseInt(totalFormsInput.value, 10);

document.getElementById('add_button').addEventListener('click', function () {
    let newForm = formsetContainer.children[0].cloneNode(true);

    newForm.innerHTML = newForm.innerHTML.replace(/form-(\d+)-/g, `form-${totalForms}-`);

    newForm.querySelectorAll("input, select, textarea").forEach(input => {
        if (input.tagName === "SELECT") {
            input.selectedIndex = 0;
        } else {
            input.value = "";
        }
    });

    newForm.classList.add('form_row');

    formsetContainer.appendChild(newForm);

    totalForms++;
    totalFormsInput.value = totalForms;
});

formsetContainer.addEventListener('click', function (e) {
    if (e.target && e.target.classList.contains('remove_form')) {
        let formRows = document.querySelectorAll('.form_row');
        if (formRows.length > 1) {
            e.target.closest('.form_row').remove();
            let totalForms = document.querySelectorAll('.form_row').length;
            totalFormsInput.value = totalForms;
        }
    }
});