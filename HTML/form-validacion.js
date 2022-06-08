<script src="js/form-validation.js"></script>
$(function() {
 
    $("formulario_registro").validate({
      rules: {
        nombre: {
          required: true,
          minlength: 3
        },
        email: {
          required: true,
          email: true
        },
  
        password: {
  
          required: true,
  
          minlength: 5
  
        }
  
      },
  
      // Specify validation error messages
  
      messages: {
  
        nombre: "introduzca su nombre completo porfavor",

        password: {
  
          required: "INGRESE UNA CONTRASEÑA PORFAVOR",
  
          minlength: "Su contraseña debe tener al menos 5 caracteres."
  
        },
  
        email: "Por favor, introduce una dirección de correo electrónico válida"
  
      },
  
      submitHandler: function(form) {
  
        form.submit();
  
      }
  
    });
  
  });