var init = function() {
  $('nav').animate({'opacity': '1'}, 0);
};

//BEGIN DOCUMENT.READY FUNCTION
$(document).ready(function()
{
  init();



/* SKILL BARS */
$('.skillbar').each(function(){
    dataperc = $(this).attr('data-perc'),
    $(this).find('.skill-percentage').animate({ "width" : dataperc + "%"}, dataperc*10);
});

/* ------------------------------------------------------------------------ */
/* STICKY NAVIGATION */
/* ------------------------------------------------------------------------ */
	$("nav").sticky({
     topSpacing: 0, className: 'sticky', wrapperClassName: 'main-menu-wrapper'
  });
/* ------------------------------------------------------------------------ */
/* SELECTNAV - A DROPDOWN NAVIGATION FOR SMALL SCREENS */
/* ------------------------------------------------------------------------ */
	selectnav('nav', {
		nested: true,
		indent: '-'
	});

});
