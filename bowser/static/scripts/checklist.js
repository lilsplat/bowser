$(document).ready(function(){
	$('#completed_dists').on('click', '.completed_dist', function(){
		if ( $('.course_title').css('display') == 'none' )
    		$('.course_title').css('display','block');
  		else
    		$('.course_title').css('display','none');
	//	$('#completed_dists').click(function() {
        });
	$('#incomplete_dists').on('click', '.incomplete_dist', function(){
			element = event.target.id;
			element = "#" + element;
			alert(element);
			if ($(element).css('display') == 'none' )
				$(element).css('display', 'block');
			else
				$(element).css('display', 'none');
				
		/*if ( $('.recommended_course').css('display') == 'none' )
    		$('.recommended_course').css('display','block');
  		else
    		$('.recommended_course').css('display','none'); */
	//	$('#completed_dists').click(function() {
        });




});
