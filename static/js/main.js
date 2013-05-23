    $(document).ready(function(){
	if ($('#calendar').length === 0)
	    return;
		
	    var cal = $('#calendar').calendario({
		displayWeekAbbr : true,
	    });
	
       var $month = $( '#custom-month' ).html( cal.getMonthName() ),
            $year = $( '#custom-year' ).html( cal.getYear() );

            $( '#custom-next' ).on( 'click', function() {
                cal.gotoNextMonth( updateMonthYear );
            });
            $( '#custom-prev' ).on( 'click', function() {
                cal.gotoPreviousMonth( updateMonthYear );
            });
            
            $('#custom-current').on( 'click', function() {
					cal.gotoNow( updateMonthYear );
			});

            function updateMonthYear() {				
                $month.html( cal.getMonthName() );
                $year.html( cal.getYear() );
            }
            
            
            
/*         function stickFooter() {
    var $content = $('.ui-content');
    var $footer = $('.ui-footer');
    var $header = $('.ui-header');
    var footerHeight = $footer.height();
    var $headerHeight = $header.height();
    $content.css("overflow", "auto");
    var contentHeight = $content.outerHeight();
    var viewportHeight = $(window).height();
    if ((contentHeight + footerHeight + headerHeight) > viewportHeight) {
        $footer.css({
            'position': 'static',
            'bottom': 'inherit',
            'left': 'inherit',
            'right': 'inherit'
        });
    } else {
        $footer.css({
            'position': 'absolute',
            'bottom': '0px',
            'left': '0px',
            'right': '0px'
        });
    }
    $content.css("overflow", "visible");
}*/
       
/*    var $page = $('.ui-page');
    var viewportHeight = $(window).height();

    if ($page.height() > viewportHeight) {
        $footer.css({
            'position': 'static',
            'bottom': 'inherit',
            'left': 'inherit',
            'right': 'inherit'
        });
    } else {
        $footer.css({
            'position': 'absolute',
            'bottom': '0px',
            'left': '0px',
            'right': '0px'
        });
    }
    $content.css("overflow", "visible");
    });*/

	$('.markAttendanceBtn').click(function(e) {
	    e.preventDefault();
	    var $that = $(this);
	    var id = $that.closest('li').attr('data-id');
	    var date = $('#attendanceDate').val();
	    $.getJSON("/has_attendance/", {id:id, date:date}, function(response) {
            if (response.error) {
                alert(response.error);
                return;
            }
            
            if (response.success !== 'no') {
                var startTime = response.checkin.time_in,
                    endTime = response.checkin.time_out == '' ? response.now : response.checkin.time_out;
                $('#attendanceform').find('.presentCheckbox').attr("checked", "checked").checkboxradio('refresh');
            } else {
                var startTime = response.now;
                var endTime = '';
                $('#attendanceform').find('.presentCheckbox').removeAttr("checked").checkboxradio('refresh');
            }
            $('#attendanceform').find('.startTime').val(startTime);
            $('#attendanceform').find('.endTime').val(endTime);

            $('#studentAttPopup').popup('open');
            $('#attendanceform').bind('submit', function(e) {
            e.preventDefault();
            var time_in = $(this).find('.startTime').val();
            var time_out = $(this).find('.endTime').val();
            var isPresent = $(this).find('.presentCheckbox').is(":checked");
            
            $.getJSON("/checkin/", {
                user: id,
                time_in: time_in,
                time_out: time_out,
                is_present: isPresent,
                date: date,
                centre: 1 //FIXME: get centre from page
            }, function(response) {
                if (response.error) {
                alert(response.error);
                } else {
                $('#attendanceform').unbind("submit");
                $('#studentAttPopup').popup('close');
                var $tickmark = $that.closest('li').find('.presentIcon');
                if (isPresent) {
                    $tickmark.removeClass('none').addClass('presentIconGreen');
                    }    else {
                    $tickmark.removeClass('presentIconGreen').addClass('none');
                    }
                     }

            
            });
	    });
	    return false;
	});
	});
	$( '.datepicker' ).pickadate().on("change", function() {
	    var date = $(this).val();
	    //var url = "/view_attendance/";
        var url = location.pathname;
	    if (date) {
            url += "?date=" + date;
	    }
	    location.href = url;
	});

	$('.viewAttendanceBtn').click(function(e) {
		e.preventDefault();
		var $this = $(this);
		//$this.hide();
		
		
		var $li = $this.closest('li');
		if (!$li.find('.attendance_detail').is(":visible")) {
			var id = $li.attr("data-id");
			$this.find('.ui-btn-text').text("Loading...");		
			var url = "/attendance_detail_ajax/" + id + "/";
			$.get(url, {}, function(html) {
				$li.find('.attendance_detail').html(html).show();
				$this.find('.ui-btn-text').text("Hide Attendance Detail");
			});
		} else {
			$li.find('.attendance_detail').hide();
			$this.find('.ui-btn-text').text("View Attendance Detail");

		}
	});
/*
    $('#attendanceform').submit(function (event) {
     event.preventDefault();
     alert("You submitted, you fool !");
 });
*/    
});
