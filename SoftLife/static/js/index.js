$(function () {
	'use strict';


	$('.form-control').on('input', function () {
		var $field = $(this).closest('.form-group');
		if (this.value) {
			$field.addClass('field--not-empty');
		} else {
			$field.removeClass('field--not-empty');
		}
	});

});
for (var i = 1; i <= 4; i++) {
	var ctx = document.getElementById('myChart'+i);
	var ctx = document.getElementById('myChart'+i).getContext('2d');
	var ctx = $('#myChart'+i);
	var ctx = 'myChart'+i;

}