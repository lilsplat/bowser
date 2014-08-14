$(document).ready(function(){
	$('#completed_dists').on('click', '.completed_dist', function(){
		if ( $('.course_title').css('display') == 'none' )
    		$('.course_title').css('display','block');
  		else
    		$('.course_title').css('display','none');
	//	$('#completed_dists').click(function() {
        });
	$('#incomplete_dists').on('click', '.incomplete_dist', function(){
		if ( $('.recommended_course').css('display') == 'none' )
    		$('.recommended_course').css('display','block');
  		else
    		$('.recommended_course').css('display','none');
	//	$('#completed_dists').click(function() {
        });




});
