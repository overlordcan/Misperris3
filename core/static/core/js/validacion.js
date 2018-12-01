

$(document).ready(function(){
    $("#formularioPostulante").validate({
        rules:{
            txtRun:{
                required:true,
                minlength:9,
                maxlength:10
            },
            NombreCompleto:{
                required:true,
                minlength:5,
                maxlength:50
            },
            cboRegion:{
                required: true
            },
            cbociudad:{
                required: true
            },
            cboCiudad:{
                required: true
            },
            cboVivienda:{
                required: true
            },
            txtTelefono:{
                required:true,
                number:true,
                minlength:9,
                maxlength:9
            }
        },
        messages:{
            txtRun:{
                required:"Este campo es requerido...",
                minlength:"Minimo 9 caracteres",
                maxlength:"Maximo 10 caracteres"
            },
            cboRegion:{
                required:"Seleccione una Región"
            },
            cboCiudad:{
                required:"Seleccione una Ciudad"
            },
            cboVivienda:{
                required:"Seleccione una Vivienda"
            }      }
    });
})