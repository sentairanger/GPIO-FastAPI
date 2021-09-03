$('#red').on('mousedown', function(){
	$.get('/red');
	});
$('#yellow').on('mousedown', function(){
	$.get('/yellow');
	});
$('#green').on('mousedown', function(){
	$.get('/green');
	});
$('#min').on('mousedown', function(){
	$.get('/min');
	});
$('#mid').on('mousedown', function(){
	$.get('/mid');
	});
$('#max').on('mousedown', function(){
	$.get('/max');
	});
$('#up').on('mousedown', function(){
	$.get('/up');
	});
$('#up').on('mouseup', function(){
	$.get('/stop');
	});
$('#down').on('mousedown', function(){
	$.get('/down');
	});
$('#down').on('mouseup', function(){
	$.get('/stop');
	});
$('#left').on('mousedown', function(){
	$.get('/left');
	});
$('#left').on('mouseup', function(){
	$.get('/stop');
	});
$('#right').on('mousedown', function(){
	$.get('/right');
	});
$('#right').on('mouseup', function(){
	$.get('/stop');
	});
