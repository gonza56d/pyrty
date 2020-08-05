$('#new_private_message').submit(function(e) {

	e.preventDefault();

	$.post({
		'url': $('#new_private_message').attr('action'),
		data: {
			'target_user': $('#id_target_user').val(),
			'message': $('#id_message').val(),
			'csrftoken': csrftoken
		},
		dataType: 'json',
		success: function(data) {
			Swal.fire(
				'Success!', data.message, 'success'
			).then((value) => {
				window.location.reload();
			});
		}
	});

});


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


var csrftoken = getCookie('csrftoken');


function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
