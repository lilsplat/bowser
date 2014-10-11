$(document).ready(function() {
	$("#my_courses").on("click", ".delete_review", function() {
		var id = $(this).attr('id');
		$.ajax({
            type: "POST",
            url: "/courses/mycourses/delete_course/",
            data: { 'code':id },
            success: function(response){
				$("#"+id).css("display", "none");
            }
        });
        return false;
    });
	
	$('#my_courses').on('click', '.edit_review', function() {
		var id = $(this).attr('id');
		id= "#" + id + "_comment";
		$(id).attr('contentEditable', true);
		$(id).css("border", "10px 10px 5px #888888");
		id += "save";
		$(id).css("display", "block");	
		});

	$('#my_courses').on('click', '.save_review', function() {
		var id = $(this).attr('id');
		id = id.split("_")[0];
		textbox = "#" +  id + "_comment";
		savebutton = "#" + id+ "_commentsave"; 
		$(textbox).attr('contentEditable', false);
		$(savebutton).css("display", "none");	
		newcomment = $(textbox).text();
		alert(newcomment);
		$.ajax({
            type: "POST",
            url: "/courses/mycourses/save_review/",
            data: { 'review': newcomment,
					'code': id},
            success: function(response){
            }
        });

		});


});
