$(document).ready(function() {


	function create_event() {
	    console.log("create post is working!");

	};

	$('#form').on('submit', function(event){
	    //event.preventDefault();
	    console.log("form submitted!");
	    create_post();
	});


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