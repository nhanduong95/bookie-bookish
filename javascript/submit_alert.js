function submit(){
	bootbox.dialog({
  		message: "You have registered successfully. Do you want to return to our home page?",
  		buttons: {
    		main: {
        		label: "OK",
        		className: "btn-primary",
        		callback: function() {
            		window.open('http://bookie-bookish-new.appspot.com');
          		}
        	}
        }
  	});
}

