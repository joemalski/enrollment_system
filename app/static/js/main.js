// main.js - app's main javascript file

$(function () {
    console.log('hello world! - jquery');

    $('[data-toggle="popover"]').popover();

    /*
    Note: If you wanted to implement client-side validation can enable
          this code block and add 'needs-validation' class to the form.

    var form = document.querySelector('.needs-validation');

    if(form) {
        form.addEventListener('submit', function(event) {
            
            if (form.checkValidity() === false) {
                event.preventDefault();
                event.stopPropagation();
            }
            
            form.classList.add('was-validated')
        });        
    }
    */
});