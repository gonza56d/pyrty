$('.delete_comment').click(function() {
	var id = $(this).attr('id').replace('delete_comment_', '');
	$.post({
		'url': $('#delete_comment').attr('class'),
		data: {
			'id': id,
			'csrftoken': csrftoken
		},
		dataType: 'json',
		success: function(data) {
			if (data.status === 200) {
				Swal.fire(
					'Success!', data.message, 'success'
				).then((value) => {
					window.location.reload();
				});
			} else {
				Swal.fire('Error!', data.message, 'error');
			}
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
