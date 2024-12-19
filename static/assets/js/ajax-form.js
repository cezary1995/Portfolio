$(function () {

	// Get the form.
	var form = $('#contact-form');

	// Get the messages div.
	var formMessages = $('.ajax-response');

	// Set up an event listener for the contact form.
	$(form).submit(function (e) {
		// Stop the browser from submitting the form.
		e.preventDefault();

		// Serialize(change f.: JS -> string(format: URL-encoded)) the form data.
		var formData = $(form).serialize();

		// Submit the form using AJAX.
		$.ajax({
			type: 'POST',
			url: $(form).attr('action'),
			data: formData
		})
			.done(function (response) {
				// Make sure that the formMessages div has the 'success' class.
				$(formMessages).removeClass('error');
				$(formMessages).addClass('success');

				// Set the message text.
				$(formMessages).text(response.responseText);

				// Clear the form.
				$('#contact-form input,#contact-form textarea').val('');
				$('#contact-form select[name="budget"]').prop('selectedIndex', 0);
				// Remove success message after 5 seconds
				setTimeout(function () {
					$(formMessages).empty().removeClass('success');
				}, 5000);
			})
			.fail(function (response) {

				// Make sure that the formMessages div has the 'error' class.
				$(formMessages).removeClass('success');
				$(formMessages).addClass('error');
				
				if (response.responseJSON && response.responseJSON.responseText){
					$(formMessages).text(response.responseJSON.responseText);
				} else {
					$(formMessages).text('Oops! An error occurred and your message could not be sent.');
				}

				// Remove error message after 5 seconds
				setTimeout(function () {
					$(formMessages).empty().removeClass('error');
				}, 5000);
			});
	});

});


