function timeSliderChange(newValue) {
	var time = 7;
	time += newValue * .5;
	var ampm = "am";
	if (time >= 12) {
		// if(time != 12.5) {
		// time = ((time == 12) ? 12 : time - 12);
		// }
		ampm = "pm";
	}
	var hour = parseInt(time);
	var minute = (time - hour) * 60;
	var d = new Date(2012, 1, 1, hour, minute, 0, 0);
	document.getElementById("endRange").innerHTML = d.toTimeString().substring(
			0, 5)
			+ " " + ampm;
	$('.courseNeeded,.allCourse').each(function() {
		var stime = $(this).attr('start');
		if (stime !== 'None' && stime !== undefined) {
			if (stime.match(':')) {
				var sh = parseInt(stime.split(":")[0]);
				var sm = stime.split(":")[1];
				sm = parseInt(sm);
			}
			var sd = new Date(2012, 1, 1, sh, sm, 0, 0);
			if (sd > d)
				$(this).addClass('hidden');
			else
				$(this).removeClass('hidden');
		}
	});
}

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
	$('#id_college option[value='+id+']').attr('selected', 'selected');
	$.post('/allCollegeForm', $('#allCollegeForm').serialize(), function(data){
		console.log('from te server');
		console.log(data);
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
	$('#id_department option[value='+id+']').attr('selected', 'selected');
	$.post('/allCollegeForm', $('#allCollegeForm').serialize(), function(data){
		console.log('from te server');
		console.log(data);
	});
}

function filterMajor(maj) {
	var deptValue = maj.value;
	var id = $('#majorSelect option')[maj.selectedIndex];
	id = $(id).attr('pk');
	$('#id_major option[selected=selected]').removeAttr('selected');
	$('#id_major option[value='+id+']').attr('selected', 'selected');
	$.post('/allCollegeForm', $('#allCollegeForm').serialize(), function(data){
		console.log('from te server');
		console.log(data);
	});
}

function startSliderChange(newValue) {
	var time = 7;
	time += newValue * .5;
	var ampm = "am";
	if (time >= 12) {
		// if(time != 12.5) {
		// time = ((time == 12) ? 12 : time - 12);
		// }
		ampm = "pm";
	}
	var hour = parseInt(time);
	var minute = (time - hour) * 60;
	var d = new Date(2012, 1, 1, hour, minute, 0, 0);
	document.getElementById("startRange").innerHTML = d.toTimeString()
			.substring(0, 5)
			+ " " + ampm;
	$('.courseNeeded,.allCourse').each(function() {
		var stime = $(this).attr('start');
		if (stime !== 'None' && stime !== undefined) {
			if (stime.match(':')) {
				var sh = parseInt(stime.split(":")[0]);
				var sm = stime.split(":")[1];
				sm = parseInt(sm);
			}
			var sd = new Date(2012, 1, 1, sh, sm, 0, 0);
			if (sd < d)
				$(this).addClass('hidden');
			else
				$(this).removeClass('hidden');
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
function booleanDay(input) {
	$('.courseNeeded,.allCourse').each(function() {
		var days = $(this).attr('days');
		if (days !== 'None' && days !== undefined) {
			if ($(input).attr('checked')) {
				if (days.match($(input).attr('name'))) {
					$(this).addClass('hidden');
				} else {
					$(this).removeClass('hidden');
				}
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
	;
}
