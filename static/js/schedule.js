$(document).ready(function() {
	applyFilters();
});
function filterCollege(col) {
	var colValue = col.value;
	if (colValue == 'Select a college to filter') {
		$('#possibleCourses > div.courses')
				.html(
						'<h4 onmouseover="highlightFilter()">Apply a College Filter to see possible courses</h4>');
		return;
	}
	var id = $('#collegeSelect option')[col.selectedIndex];
	id = $(id).attr('pk');
	$('.department').each(function() {
		if ($(this).attr('college') == colValue) {
			$('#departmentSelect').append(this);
		} else {
			$('#noneDepartments').append(this);
		}
	});
	$('#id_college option[selected=selected]').removeAttr('selected');
	$('#id_department option[selected=selected]').removeAttr('selected');
	$('#id_major option[selected=selected]').removeAttr('selected');
	$('#majorSelect > *').html('<input> ---- </input>');
	$('#id_college option[value=' + id + ']').attr('selected', 'selected');
	$('#possibleTitle').text(colValue + " courses");
	$('#collegeSelect').css('background', '#fff');
	$.post('/allCollegeForm', $('#allCollegeForm').serialize(), function(data) {
		$('#possibleCourses > div.courses').html(data);
		applyFilters();
	});
}

function filterDepartment(dept) {
	var deptValue = dept.value;
	var id = $('#departmentSelect option')[dept.selectedIndex];
	id = $(id).attr('pk');
	$('.major').each(function() {
		if ($(this).attr('department') == deptValue) {
			$('#majorSelect').append(this);
		} else {
			$('#noneMajor').append(this);
		}
	});
	$('#id_department option[selected=selected]').removeAttr('selected');
	$('#id_major option[selected=selected]').removeAttr('selected');
	$('#id_department option[value=' + id + ']').attr('selected', 'selected');
	$('#possibleTitle').text(deptValue + ' department courses');
	$.post('/allCollegeForm', $('#allCollegeForm').serialize(), function(data) {
		$('#possibleCourses > div.courses').html(data);
		applyFilters();
	});
}

function displayInfo(element) {
	$('#course-info').html($(element).next('.course-info').html());
}

function filterMajor(maj) {
	var majValue = maj.value;
	var id = $('#majorSelect option')[maj.selectedIndex];
	id = $(id).attr('pk');
	$('#id_major option[selected=selected]').removeAttr('selected');
	$('#id_major option[value=' + id + ']').attr('selected', 'selected');
	$('#possibleTitle').text(majValue + " required courses");
	$.post('/allCollegeForm', $('#allCollegeForm').serialize(), function(data) {
		$('#possibleCourses > div.courses').html(data);
		applyFilters();
	});
}
var startDate = new Date(2012, 1, 1, 12, 0, 0, 0);
var endDate = new Date(2012, 1, 1, 12, 0, 0, 0);
function startSliderChange(newValue) {
	var time = 7;
	time += newValue * .5;
	var ampm = "am";
	if (time >= 12) {
		ampm = "pm";
	}
	var hour = parseInt(time);
	var minute = (time - hour) * 60;
	startDate = new Date(2012, 1, 1, hour, minute, 0, 0);
	document.getElementById("startRange").innerHTML = startDate.toTimeString()
			.substring(0, 5)
			+ " " + ampm;
	$('.neededCourse, .allCourse').each(function() {
		var stime = $(this).attr('start');
		if (stime !== 'None' && stime !== undefined) {
			if (stime.match(':')) {
				var sh = parseInt(stime.split(":")[0]);
				var sm = stime.split(":")[1];
				sm = parseInt(sm);
			}
			var sd = new Date(2012, 1, 1, sh, sm, 0, 0);
			if ($('#startB').attr('checked') && (sd < startDate || sd > endDate))
				$(this).addClass('hidden');
			else
				$(this).removeClass('hidden');
			if (startDate >= endDate) {
				var i = newValue;
				if (newValue < 24)
					i++;
				$('#endSlider').val(i);
				endSliderChange(i);
			}
		}
	});
}

function applyFilters() {
	booleanDay();
	levelSliderChange($('#levelSlider').val());
	startSliderChange($('#startSlider').val());
	endSliderChange($('#endSlider').val());
}

function endSliderChange(newValue) {
	var time = 7;
	time += newValue * .5;
	var ampm = "am";
	if (time >= 12) {
		ampm = "pm";
	}
	var hour = parseInt(time);
	var minute = (time - hour) * 60;
	endDate = new Date(2012, 1, 1, hour, minute, 0, 0);
	document.getElementById("endRange").innerHTML = endDate.toTimeString()
			.substring(0, 5)
			+ " " + ampm;
	$('.neededCourse, .allCourse').each(function() {
		var stime = $(this).attr('start');
		if (stime !== 'None' && stime !== undefined) {
			if (stime.match(':')) {
				var sh = parseInt(stime.split(":")[0]);
				var sm = stime.split(":")[1];
				sm = parseInt(sm);
			}
			var sd = new Date(2012, 1, 1, sh, sm, 0, 0);
			if ($('#endB').attr('checked') && (sd < startDate || sd > endDate))
				$(this).addClass('hidden');
			else
				$(this).removeClass('hidden');
			if (startDate >= endDate) {
				var i = newValue;
				if (newValue > 0)
					i--;
				$('#startSlider').val(i);
				startSliderChange(i);
			}
		}
	});
}

function levelSliderChange(newValue) {
	document.getElementById("levelRange").innerHTML = newValue;
	$('.allCourse').each(function() {
		var numb = $(this).attr('num');
		// document.getElementById("levelRange").innerHTML = numb.charAt(0);
		if (parseInt(numb.charAt(0)) * 1000 == parseInt(newValue)) {
			if ($(this).hasClass('leveled')) {
				$(this).removeClass('hidden');
				$(this).removeClass('leveled');
			}
		} else {
			$(this).addClass('hidden');
			$(this).addClass('leveled');
		}
	});
}
var selectedDays = [];
function booleanDay(input) {
	var day = $(input).attr('name');
	if ($(input).attr('checked')) {
		if (selectedDays.indexOf(day) == -1)
			selectedDays.push(day);
	} else {
		var i = selectedDays.indexOf(day);
		selectedDays.pop(i);
	}
	$('.neededCourse,.allCourse').each(function() {
		var days = $(this).attr('days');
		if (days !== 'None' && days !== undefined) {
			if ($(input).attr('checked')) {
				if (days.match(day)) {
					$(this).addClass('hidden');
				}
			} else {
				var toHide = true;
				for ( var i = 0; i < selectedDays.length; i++) {
					if (days.match(selectedDays[i])) {
						toHide = false;
					}
				}
				if (toHide)
					$(this).removeClass('hidden');
			}
		}
	});
}

function possibleClick(element) {
	neededClick(element);
}
function removeCourse(element) {
	$('#coursesWanted [value=' + $(element).attr('pk') + ']').removeAttr(
			'selected');
	$(element).remove();
	$('#id_student_pk').val($("#STUDENT").attr('pk'));
	$.post('/coursesWanted', $('#coursesWanted').serialize(), function(data) {
		$('#schedule').html($(data));
		var num = $(data).attr('id');
		fillSchedule(num);
	});
}
function neededClick(element) {
	$('#courses-wanted > .courses').append(
			$(element).clone().removeAttr('class').attr('onclick',
					'removeCourse(this)').addClass('wantedCourse'));
	$('#coursesWanted [value=' + $(element).attr('pk') + ']').attr('selected',
			'selected');
	$('#id_student_pk').val($("#STUDENT").attr('pk'));
	$.post('/coursesWanted', $('#coursesWanted').serialize(), function(data) {
		$('#schedule').html($(data));
		var num = $(data).attr('id');
		fillSchedule(num);
	});
}

function fillSchedule(num) {
	$('.scheduledCourse').each(
			function() {
				course = this;
				var days = $(course).attr('days');
				var time = $(course).attr('start');
				days = days.split(' ');
				for ( var i = 0; i < days.length; i++) {
					// console.log($('table [day="' + days[i] + '"][time="' +
					// time
					// + '"]'));
					$(
							'#' + num + ' table [day="' + days[i] + '"][time="'
									+ time + '"]').text($(course).text());
				}
			});
}

function highlightFilter() {
	$('#collegeSelect').css('background', '#efcdcd');
}
