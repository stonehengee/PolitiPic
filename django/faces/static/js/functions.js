
 // Sticky Header

 (function () {
  "use strict";

  var nav = $('.navbar');
  var scrolled = false;

  $(window).scroll(function () {

    if (300 < $(window).scrollTop() && !scrolled) {
      nav.addClass('bg-change animated');
      scrolled = true;
    }

    if (300 > $(window).scrollTop() && scrolled) {
      nav.removeClass('bg-change animated');
      scrolled = false;
    }
  });

}());




 jQuery(window).on('scroll', function($){
  "use strict";

  /*------------- Scroll to Top -----------------*/

  if (jQuery(this).scrollTop() > 100) {
    jQuery('#scroll-to-top').fadeIn('slow');
  } else {
    jQuery('#scroll-to-top').fadeOut('slow');
  }
});


 $('#scroll-to-top').click(function(){
  "use strict";

  $("html,body").animate({ scrollTop: 0 }, 1500);
  return false;
});


 jQuery(window).load(function(){
  "use strict";
// Stellar parallax

$(window).stellar({
  horizontalScrolling: false,
  responsive: true
});

});



 jQuery(document).ready(function() {

  "use strict";


  $('.counter').counterUp({
    delay: 10,
    time: 3000
  });



  // Project Gallery        

  $('.image-popup-vertical-fit').magnificPopup({ 
    type: 'image',
    gallery:{
      enabled:true
    }
  });


// WOW Animate

var wow = new WOW(
{
  boxClass:     'wow',       
  animateClass: 'animated',  
  offset:       0,           
  mobile:       false        
}
);
wow.init();


/*----------- NiceScroll -----------*/
    //Check IE11
    function IEVersion() {
      if (!!navigator.userAgent.match(/Trident\/7\./)) {
        return 11;
      }
    }

    if (IEVersion() != 11) 
    {
      $('html').niceScroll({
        cursorcolor: "#e74c3c",
        zindex: '99999',
        cursorminheight: 60,
        scrollspeed: 80,
        cursorwidth: 10,
        autohidemode: true,
        background: "#aaa",
        cursorborder: 'none',
        cursoropacitymax: 0.7,
        cursorborderradius: 0,
        horizrailenabled: false
      });
    }





    /*-------------------------- Latest Project Item Filter -----------------------*/

    var $projectItems = $('#project-items'),
    colWidth = function () {
      var w = $projectItems.width(), 
      columnNum = 1,
      columnWidth = 0;
      if (w > 960) {
        columnNum  = 4;
      } 
      else if (w > 640) {
        columnNum  = 2;
      } 
      else if (w > 480) {
        columnNum  = 2;
      }  
      else if (w > 360) {
        columnNum  = 1;
      } 
      columnWidth = Math.floor(w/columnNum);
      $projectItems.find('.item').each(function() {
        var $item = $(this),
        multiplier_w = $item.attr('class').match(/item-w(\d)/),
        multiplier_h = $item.attr('class').match(/item-h(\d)/),
        width = multiplier_w ? columnWidth*multiplier_w[1] : columnWidth,
        height = multiplier_h ? columnWidth*multiplier_h[1]*0.7-10 : columnWidth*0.7-10;
        $item.css({
          width: width,
          height: height
        });
      });
      return columnWidth;
    },
    isotope = function () {
      $projectItems.isotope({
        resizable: true,
        itemSelector: '.item',
        masonry: {
          columnWidth: colWidth(),
          gutterWidth: 10
        }
      });
    };
    isotope();
    $(window).smartresize(isotope);

    $('.itemFilter a').click(function(){
      $('.itemFilter .current').removeClass('current');
      $(this).addClass('current');

      var selector = $(this).attr('data-filter');
      $projectItems.isotope({
        filter: selector,
        animationOptions: {
          duration: 750,
          easing: 'linear',
          queue: false
        }
      });
      return false;
    }); 



  });




// Overwriting IE AddEventListener

function addEvent( obj, type, fn ) {
  if ( obj.attachEvent ) {
    obj['e'+type+fn] = fn;
    obj[type+fn] = function(){obj['e'+type+fn]( window.event );}
    obj.attachEvent( 'on'+type, obj[type+fn] );
  } else
  obj.addEventListener( type, fn, false );
}
function removeEvent( obj, type, fn ) {
  if ( obj.detachEvent ) {
    obj.detachEvent( 'on'+type, obj[type+fn] );
    obj[type+fn] = null;
  } else
  obj.removeEventListener( type, fn, false );
}


/* =================================
===  Bootstrap Internet Explorer 10 in Windows 8 and Windows Phone 8 FIX
=================================== */
if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
  var msViewportStyle = document.createElement('style')
  msViewportStyle.appendChild(
    document.createTextNode(
      '@-ms-viewport{width:auto!important}'
      )
    )
  document.querySelector('head').appendChild(msViewportStyle)
}



// Avoid `console` errors in browsers that lack a console.
(function() {
  var method;
  var noop = function () {};
  var methods = [
  'assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'error',
  'exception', 'group', 'groupCollapsed', 'groupEnd', 'info', 'log',
  'markTimeline', 'profile', 'profileEnd', 'table', 'time', 'timeEnd',
  'timeline', 'timelineEnd', 'timeStamp', 'trace', 'warn'
  ];
  var length = methods.length;
  var console = (window.console = window.console || {});

  while (length--) {
    method = methods[length];

        // Only stub undefined methods.
        if (!console[method]) {
          console[method] = noop;
        }
      }
    }());

// Place any jQuery/helper plugins in here.
