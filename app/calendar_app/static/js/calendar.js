$(document).ready(function() {
	$('#calendar').datepicker({
			inline: true,
			firstDay: 0,
			showOtherMonths: true,
			dayNamesMin: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
		});

	$("#calendar a").click(function(){
		alert("fds");
	});
});