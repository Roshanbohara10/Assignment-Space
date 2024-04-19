
$(document).ready(function () {
    // When a form field is changed...
    $('#myForm :input').change(function () {
        // Check if at least one field has a value
        var isFormFilled = false;
        $('#myForm :input').each(function () {
            if ($(this).val() !== '') {
                isFormFilled = true;
                return false;  // Exit the loop
            }
        });

        // Enable or disable the submit button based on whether the form is filled
        $('#submitBtn').prop('disabled', !isFormFilled);
    });
});
