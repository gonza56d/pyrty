$('#dropdown-notifications').click(function() {

	if ($('#dropdown-notifications').attr('class') === 'btn btn-warning dropdown-toggle') {

		$.post({
			'url': $('#update_notifications').attr('class'),
			data: {
				'csrftoken': csrftoken
			},
			dataType: 'json'
		});

		$('#dropdown-notifications').attr('class', 'btn btn-info dropdown-toggle');

	}

});