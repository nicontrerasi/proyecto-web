$(document).ready(function() {
    var validator = $("#basic-form").validate({
        rules: {
            pwd: "required",
            email: "required",
            username: {
                required: true,
                minlength: 10,
            }
        },
    });

});