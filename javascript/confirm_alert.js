function message(id){
	bootbox.dialog({
  		message: "Do you want to delete this?",
  		title: "Delete Confirmation",
  		buttons: {
    		main: {
          label: "Delete",
          className: "btn-primary",
          callback: function() {
            var code = $("#" + id).html()
            $ ("." + id).remove();
            $.ajax({
              url: '/booktypeEdit?code=' + code,
              type:'DELETE'
            });
          }
        }
      }
  });
}



