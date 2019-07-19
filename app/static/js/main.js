// main.js - app's main javascript file

$(function () {
    console.log('hello world! - jquery');

    $('[data-toggle="popover"]').popover();

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
});