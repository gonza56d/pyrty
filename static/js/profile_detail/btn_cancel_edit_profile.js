$("#btn_cancel_edit_profile").click(function(){

    $(this).attr("style", "display:none;");
    $("#btn_confirm_edit_profile").attr("style", "display:none;");
    $("#btn_edit_profile").attr("style", "display:;");

    $("#id_first_name").attr("disabled", "");
    $("#id_last_name").attr("disabled", "");

});