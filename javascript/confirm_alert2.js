function message2(id){
	bootbox.dialog({
  		message: "Do you want to delete this?",
  		title: "Delete Confirmation",
  		buttons: {
    		main: {
            label: "Delete",
            className: "btn-primary",
            callback: function() {
               var code = $("." + id).html()
               $ ("#"+ id).remove();
               $.ajax({
                  url: '/bookdetailsEdit?code=' + code,
                  type:'DELETE'
               });
            }
         }
      }
  });
}



