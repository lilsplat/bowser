$(document).ready(function() {
    $("#my_courses").on('click', '.added_course_with_review a', function() {
        var id = $('.added_course_with_review').attr('id');
        $.ajax({
            type: "POST",
            url: "/courses/mycourses/delete_course/",
            data: { 'code':id },
            success: function(response){
            }
        });
        return false;
    });
});
/*
$(document).click(function(){
    alert('You clicked me!');
});
*/
