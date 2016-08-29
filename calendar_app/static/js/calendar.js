$(document).ready(function() {

	var dict = {};
	  var months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
  ];


	$('#calendar').datepicker({
			inline: true,
			firstDay: 0,
			showOtherMonths: true,
			dayNamesMin: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
		});

	


	function onChangeMonthYear(year, month) { 

		
		$.ajax({

			url: '/query',
			data: {month: month, year: year},
			method: "GET",
			success: function(data){
				dict = {};
				data = JSON.parse(data);
				if(data.length === 0){
					return;
				}
				for(var index in data){
					var item = data[index];
					var date = parseInt(item['fields']['start_date'].split('-')[2]);

					if(dict[date] === undefined){
						dict[date] = [];
					}

					dict[date].push(item);
				}

				//console.log(dict);

				$.each($("a.ui-state-default"), function(){

					var date = parseInt($(this).text());
					//console.log(date);
					if(dict[date]!==undefined){
						//alert(date);
						var main = $();
						for(var index in  dict[date]){
							var item = dict[date][index];
							main = main.add($("<a class='event_link' href = "+ date +";" + index +">" + item['fields']['event_name'] + "</a>"));
						};

						$(this).html(main);
					}
				})

				//console.log(dict);
				$('.event_link').on('click',function(e){
					var pk = $(this).attr('href');
					var date = pk.split(";")[0];
					var index = pk.split(";")[1];
					var p = $("<p></p>");

					var fields = dict[date][index]['fields'];
					p.append($("<h4>" +	fields['event_name']  + "</h4>"));
					delete fields["event_name"];
					for(var key in fields){
						p.append($("<h6 style='display:inline;'>" + key.replace("_"," ") + "</h6>&nbsp;&nbsp;&nbsp; <span>" + fields[key] + "</span><br/>"));
					}
					//console.log(p);
					$(".event_modal_body").html(p);
					$("#myModal").modal('toggle');
					e.preventDefault();
					e.stopPropagation();
					return false;
				});
			}
		});
	}

	$('#calendar').datepicker('option', 'onChangeMonthYear', onChangeMonthYear);
	var date = $("#calendar").datepicker( 'getDate' );
	onChangeMonthYear(date.getFullYear(), date.getMonth() + 1);

	$(document).on('click', 'a.ui-state-default',function(e){
		e.preventDefault();
		return false;
	});

	$('#calendar').datepicker('option', 'onSelect', function(){
			var date = $("#calendar").datepicker( 'getDate' );
			onChangeMonthYear(date.getFullYear(), date.getMonth() + 1);
	});	
});