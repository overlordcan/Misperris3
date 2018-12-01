$(document).ready(function(){
    
    $("#cboRegion").change(function(){
        var regionId = $("#cboRegion").val();

        if(regionId == ""){
            $("#cboCiudad").prop("disabled", true);
            $("#cboCiudad").val("");
            return;
        }
        $.get("combo.php", {id:regionId}, function(respuesta){

            $("#cboCiudad").html(respuesta);
            $("#cboCiudad").prop("disabled",false);
        });
    });
});