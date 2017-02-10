
(function () {
	$(function () {
		socialHover();
		stickyNav();
	});

	function socialHover() {

		$(".share").on({
			mouseenter: function () {
				$(this).children('ul').addClass('display');
			},
			mouseleave: function () {
				$(this).children('ul').removeClass('display');
			}
		});
	}


	function stickyNav(){

		$(window).scroll(function() {
			if ($(this).scrollTop() > 1){
			    $('nav').addClass("sticky");
			  }
		  else{
		    $('nav').removeClass("sticky");
		  }
		});

	}

})(jQuery);
