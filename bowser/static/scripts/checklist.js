$(document).ready(function(){
	$('#incomplete_dists a').on('click', function() {
		var id = $(this).attr('id');
		originalid = '#' + id;
		id = '#' + id + 'div';
		alert(id);
		$(id).toggle('slow', function() {
			})
		});

});
