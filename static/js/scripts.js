
   (function($) {
    "use strict"; // Start of use strict
  
    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
      if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
          $('html, body').animate({
            scrollTop: (target.offset().top - 72)
          }, 1000, "easeInOutExpo");
          return false;
        }
      }
    });
  
    // Closes responsive menu when a scroll trigger link is clicked
    $('.js-scroll-trigger').click(function() {
      $('.navbar-collapse').collapse('hide');
    });
  
    // Activate scrollspy to add active class to navbar items on scroll
    $('body').scrollspy({
      target: '#mainNav',
      offset: 75
    });
  
    // Collapse Navbar
    var navbarCollapse = function() {
      if ($("#mainNav").offset().top > 100) {
        $("#mainNav").addClass("navbar-scrolled");
      } else {
        $("#mainNav").removeClass("navbar-scrolled");
      }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);
  
    // Magnific popup calls
    $('#portfolio').magnificPopup({
      delegate: 'a',
      type: 'image',
      tLoading: 'Loading image #%curr%...',
      mainClass: 'mfp-img-mobile',
      gallery: {
        enabled: true,
        navigateByImgClick: true,
        preload: [0, 1]
      },
      image: {
        tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
      }
    });  

    
      $.ajax({
          type: 'GET',
          url: 'https://graph.facebook.com/v3.0/17841445506131034?fields=name%2Cmedia.limit(9)%7Bcaption%2Clike_count%2Cmedia_url%2Cpermalink%2Ctimestamp%2Cusername%7D&access_token=EAAGFMIrkxXQBAMRsLd31BQZCXgwMPl8jrdOZCwPkrqa2PAayZBqYMHCcuFe6GLFsIe8pPqP9rvQ6iP55K8I3M1EIhmHcAcTvUVJKTUJ29o7YTFETZCuQIJCZBXJuOkYXlr5BQXCsTKzdbtouaeovG9AHlZC2ka8SH3T28FBlrtcsNz7lwJc93L',
          dataType: 'json',
          success: function(json) {
              var html = '';
              var insta = json.media.data;
              for (var i = 0; i < insta.length; i++) {
                  html += '<a href="' + insta[i].permalink + '" target="_blank"><img width="300" height="300" src="' + insta[i].media_url + '"></a>';
              }
                $("#insta").append(html);			
          },
          error: function() {
   
          }
      });

      window.onload = function() {
        const spinner = document.getElementById('loading');

        // Add .loaded to .loading
        spinner.classList.add('loaded');
}


  })(jQuery); // End of use strict
  