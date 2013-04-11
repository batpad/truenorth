    $(document).ready(function(){
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

    $( '.datepicker' ).pickadate();
    
});
