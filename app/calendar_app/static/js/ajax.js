function auto_load(){
        $.ajax({
          url: "",
          cache: false,
          success: function(data){
             $("#calendar").calendar(data);
          } 
        });
}

$(document).ready(function(){

auto_load(); //Call auto_load() function when DOM is Ready

});

//Refresh auto_load() function after 10000 milliseconds
setInterval(auto_load,10000);