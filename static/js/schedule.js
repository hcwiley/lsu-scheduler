function filterCollege(col) {
	var colValue = col.value;
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
	$('#id_college option[value=' + id + ']').attr('selected', 'selected');
	$.post('/allCollegeForm', $('#allCollegeForm').serialize(), function(data) {
		console.log(data);
		$('#course-columns > div:first-child').html(data);
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
	$.post('/allCollegeForm', $('#allCollegeForm').serialize(), function(data) {
		$('#course-columns > div:first-child').html(data);
	});
}

function filterMajor(maj) {
	var deptValue = maj.value;
	var id = $('#majorSelect option')[maj.selectedIndex];
	id = $(id).attr('pk');
	$('#id_major option[selected=selected]').removeAttr('selected');
	$('#id_major option[value=' + id + ']').attr('selected', 'selected');
	$.post('/allCollegeForm', $('#allCollegeForm').serialize(), function(data) {
		$('#course-columns > div:first-child').html(data);
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
	$('.courseNeeded, .allCourse').each(function() {
		var stime = $(this).attr('start');
		if (stime !== 'None' && stime !== undefined) {
			if (stime.match(':')) {
				var sh = parseInt(stime.split(":")[0]);
				var sm = stime.split(":")[1];
				sm = parseInt(sm);
			}
			var sd = new Date(2012, 1, 1, sh, sm, 0, 0);
			if (sd < startDate || sd > endDate)
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
	$('.courseNeeded, .allCourse').each(function() {
		var stime = $(this).attr('start');
		if (stime !== 'None' && stime !== undefined) {
			if (stime.match(':')) {
				var sh = parseInt(stime.split(":")[0]);
				var sm = stime.split(":")[1];
				sm = parseInt(sm);
			}
			var sd = new Date(2012, 1, 1, sh, sm, 0, 0);
			if (sd < startDate || sd > endDate)
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
		if (Number(numb.charAt(0)) * 1000 == Number(newValue)) {
			$(this).removeClass('hidden');
		} else {
			$(this).addClass('hidden');
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
	$('.courseNeeded,.allCourse').each(function() {
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
						toHide  = false;
					}
				}
				if (toHide)
					$(this).removeClass('hidden');
			}
		}
	});
}
function addClick() {
	document.getElementById("addButton").style.visibility = "hidden";
	document.getElementById("removeButton").style.visibility = "visible";
}
function removeClick() {
	document.getElementById("removeButton").style.visibility = "hidden";
	document.getElementById("addButton").style.visibility = "visible";
}

function possibleClick(element) {
	neededClick(element);
}
function neededClick(element) {
	var days = $(element).attr('days');
	var time = $(element).attr('start');
	days = days.split(' ');
	for ( var i = 0; i < days.length; i++) {
		console.log("|" + days[i] + "|");
		console.log("|" + time + "|");
		console.log($('table [day="' + days[i] + '"][time="' + time + '"]'));
		$('table [day="' + days[i] + '"][time="' + time + '"]').text(
				$(element).text());
	}
}
