function test() {
    var tabsNewAnim = $('#navbarSupportedContent');
    var activeItemNewAnim = tabsNewAnim.find('.active');
    var activeWidthNewAnimHeight = activeItemNewAnim.innerHeight();
    var activeWidthNewAnimWidth = activeItemNewAnim.innerWidth();
    var itemPosNewAnimTop = activeItemNewAnim.position();
    var itemPosNewAnimLeft = activeItemNewAnim.position();

    $(".hori-selector").css({
        "top": itemPosNewAnimTop.top + "px",
        "left": itemPosNewAnimLeft.left + "px",
        "height": activeWidthNewAnimHeight + "px",
        "width": activeWidthNewAnimWidth + "px"
    });

    $("#navbarSupportedContent").on("click", "li", function(e) {
        $('#navbarSupportedContent ul li').removeClass("active");
        $(this).addClass('active');

        var activeWidthNewAnimHeight = $(this).innerHeight();
        var activeWidthNewAnimWidth = $(this).innerWidth();
        var itemPosNewAnimTop = $(this).position();
        var itemPosNewAnimLeft = $(this).position();

        $(".hori-selector").css({
            "top": itemPosNewAnimTop.top + "px",
            "left": itemPosNewAnimLeft.left + "px",
            "height": activeWidthNewAnimHeight + "px",
            "width": activeWidthNewAnimWidth + "px"
        });
    });
}
 const element_one =  document.getElementById('attemps_one')
 const element_two =  document.getElementById('attemps_two')
 const element_three = document.getElementById('attemps_three')
function view(id)
{
 const element_one =  document.getElementById('attemps_one')
 const element_two =  document.getElementById('attemps_two')
 const element_three = document.getElementById('attemps_three')

  if(id == "attemps_one"){
    if(element_two == null){
      const element_two = document.getElementById('active_view')
      element_two.id = 'attemps_two'
    }else if(element_three == null){
      const element_three = document.getElementById('active_view')
      element_three.id = 'attemps_three'
    }
    element_one.id = 'active_view'

  }else if(id =="attemps_two"){
    if(element_three == null)
    {
      const element_three =  document.getElementById('active_view')
      element_three.id = 'attemps_three'
    }else if(element_one == null){
      const element_one = document.getElementById('active_view')
      element_one.id= 'attemps_one'
    }
    element_two.id = 'active_view'
   
  }else if(id == "attemps_three")
  {
    if(element_one == null){
      const element_one = document.getElementById('active_view')
      element_one.id = 'attemps_one'
    }else if(element_two== null){
      const element_two =  document.getElementById('active_view')
      element_two.id = 'attemps_two'
    }
    element_three.id ='active_view'
  }
}

$(document).ready(function() {
    test();
    $(window).on('resize', function() {
        test();
    });
    $(".navbar-toggler").click(function() {
        $(".navbar-collapse").slideToggle(300);
        test();
    });

    // Add active class to current page link
    var path = window.location.pathname.split("/").pop();
    if (path === '') {
        path = 'itdex.html';
    }
    var target = $('#navbarSupportedContent ul li a[href="' + path + '"]');
    target.parent().addClass('active');
});
