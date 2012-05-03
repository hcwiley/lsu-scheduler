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
		var stime = $(this).attr('end');
		if (stime !== 'None' && stime !== undefined) {
			if (stime.match(':')) {
				var sh = parseInt(stime.split(":")[0]);
				var sm = stime.split(":")[1];
				var sampm = sm.split(" ")[1];
				sm = parseInt(sm.split(" ")[0]);
			} else if (stime == 'noon') {
				var sh = 12;
				var sm = 0;
				var sampm = 'pm';
			} else {
				var sh = parseInt(stime.split(" ")[0]);
				var sm = 0;
				var sampm = stime.split(" ")[1];
			}
			if (sampm.match('p')) {
				sh += 12;
			}
			var sd = new Date(2012, 1, 1, sh, sm, 0, 0);
			if (sd > d)
				$(this).addClass('hidden');
			else
				$(this).removeClass('hidden');
		}
	});
}

function filterDepartment(deptValue) {
	document.getElementById("filterText").innerHTML = deptValue;
	$('.majors').each(function(){
		if ($(this).attr('dept') == deptValue){
			$(this).css("display", "inline");
			document.getElementById("majorSelect").setAttribute("selected", "selected");
		} else {
			$(this).css("display", "none");
		}
	});
	/*
	$('.allCourse').each(function() {
		document.getElementById("filterText").innerHTML = $(this).attr('dept');
		if ($(this).attr('dept') != deptValue){
			$(this).css("visibility", "hidden"); //bangarang, muthafucka
		} else {
			$(this).css("visibility", "visible"); //reverse bangarang, muthafucka
		}
	});*/
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
				var sampm = sm.split(" ")[1];
				sm = parseInt(sm.split(" ")[0]);
			} else if (stime == 'noon') {
				var sh = 12;
				var sm = 0;
				var sampm = 'pm';
			} else {
				var sh = parseInt(stime.split(" ")[0]);
				var sm = 0;
				var sampm = stime.split(" ")[1];
			}
			if (sampm.match('p')) {
				sh += 12;
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
}
function booleanDay(input) {
	$('.courseNeeded,.allCourse').each(function() {
		var days = $(this).attr('days');
		if (days !== 'None' && days !== undefined) {
			if($(input).attr('checked')){
				if(days.match($(input).attr('name'))){
					$(this).addClass('hidden');
				}
				else{
					$(this).removeClass('hidden');
				}
			}
		}
	});
}
function addClick(){
	document.getElementById("addButton").style.visibility="hidden";
	document.getElementById("removeButton").style.visibility="visible";
}
function removeClick(){
	document.getElementById("removeButton").style.visibility="hidden";
	document.getElementById("addButton").style.visibility="visible";
}
