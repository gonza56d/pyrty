$("#btn_edit_profile").click(function(){

    $(this).attr("style", "display:none;");
    $("#btn_confirm_edit_profile").attr("style", "display:;");
    $("#btn_cancel_edit_profile").attr("style", "display:;");

    $("#id_first_name").removeAttr("disabled");
    $("#id_last_name").removeAttr("disabled");
    $("#id_first_name").focus();

});