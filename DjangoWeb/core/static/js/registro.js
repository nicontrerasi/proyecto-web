$(document).ready(function() {
    $('#basic-form').validate({
        rules: {
            pwd: {
                required: true,
                minlength: 8
            },
            pwdcon: {
                required: true,
                minlength: 8,
                equalTo: "#pwd"
            },
            email: "required",
            username: {
                required: true,
                minlength: 10
            },
        },

        messages: {
            pwd: {
                required: "Ingrese su contraseña",
                minlength: "Ingrese mas de 8 caracteres"
            },
            pwdcon: {
                required: "debe reingresar la contraseña",
                equalTo: "Debe ser igual a la contraseña"
            },
            username: {
                required: "Ingrese su nombre de usuario",
                minlength: "Ingrese mas de 10 caracteres"
            },
            email: {
                required: "Ingrese un valor para el email",
                email: "Porfavor ingresa un correo valido"
            }
        }
    })

});