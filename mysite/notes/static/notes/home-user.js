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

  $("#navbarSupportedContent").on("click", "li", function (e) {
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

const element_one = document.getElementById('attemps_one')
const element_two = document.getElementById('attemps_two')
const element_three = document.getElementById('attemps_three')
const home =  document.getElementById('home')
function view(id) {
  const element_one = document.getElementById('attemps_one')
  const element_two = document.getElementById('attemps_two')
  const element_three = document.getElementById('attemps_three')
  const home =  document.getElementById('home')

  if (id == "attemps_one") {
    if (element_two == null) {
      const element_two = document.getElementById('active_view')
      element_two.id = 'attemps_two'
    } else if (element_three == null) {
      const element_three = document.getElementById('active_view')
      element_three.id = 'attemps_three'
    } else if(home != null){
      const home = document.getElementById('home')
      home.id = 'home_desactive'
    }
    element_one.id = 'active_view'

  } else if (id == "attemps_two") {
    if (element_three == null) {
      const element_three = document.getElementById('active_view')
      element_three.id = 'attemps_three'
    } else if (element_one == null) {
      const element_one = document.getElementById('active_view')
      element_one.id = 'attemps_one'
    }else if(home != null ){
      const home = document.getElementById('home')
      home.id = 'home_desactive'
    }
    element_two.id = 'active_view'

  } else if (id == "attemps_three") {
    if (element_one == null) {
      const element_one = document.getElementById('active_view')
      element_one.id = 'attemps_one'
    } else if (element_two == null) {
      const element_two = document.getElementById('active_view')
      element_two.id = 'attemps_two'
    } else if(home != null){
      const home = document.getElementById('home')
      home.id = 'home_desactive'
    }
    element_three.id = 'active_view'
  } else if(id == 'home')
  {
    if (element_one == null) {
      const element_one = document.getElementById('active_view')
      element_one.id = 'attemps_one'
    } else if (element_two == null) {
      const element_two = document.getElementById('active_view')
      element_two.id = 'attemps_two'
    } else if(home != null){
      const home = document.getElementById('home')
      home.id = 'home_desactive'
    }
  }

}

$(document).ready(function () {
  test();
  $(window).on('resize', function () {
    test();
  });
  $(".navbar-toggler").click(function () {
    $(".navbar-collapse").slideToggle(300);
    test();
  });

  // Add active class to current page link
  var path = window.location.pathname.split("/").pop();
  if (path === '') {
    path = 'index.html';
  }
  var target = $('#navbarSupportedContent ul li a[href="' + path + '"]');
  target.parent().addClass('active');
});


//model create activitie

(() => {
  // state variables
  let toDoListArray = [];
  // ui variables
  const form = document.querySelector(".form");
  const input = form.querySelector(".form__input");
  const ul = document.querySelector(".toDoList");

  // event listeners
  form.addEventListener('submit', e => {
    // prevent default behaviour - Page reload
    e.preventDefault();
    // give item a unique ID
    let itemId = String(Date.now());
    // get/assign input value
    let toDoItem = input.value;
    //pass ID and item into functions
    addItemToDOM(itemId, toDoItem);
    addItemToArray(itemId, toDoItem);
    // clear the input box. (this is default behaviour but we got rid of that)
    input.value = '';
  });

  ul.addEventListener('click', e => {
    let id = e.target.getAttribute('data-id')
    if (!id) return // user clicked in something else      
    //pass id through to functions
    removeItemFromDOM(id);
    removeItemFromArray(id);
  });

  // functions 
  function addItemToDOM(itemId, toDoItem) {
    // create an li
    const li = document.createElement('li')
    li.setAttribute("data-id", itemId);
    // add toDoItem text to li
    li.innerText = toDoItem
    // add li to the DOM
    ul.appendChild(li);
    console.log(toDoItem, itemId);
  }

  function addItemToArray(itemId, toDoItem) {
    // add item to array as an object with an ID so we can find and delete it later
    toDoListArray.push({ itemId, toDoItem });
    console.log(toDoListArray)
  }

  function removeItemFromDOM(id) {
    // get the list item by data ID
    var li = document.querySelector('[data-id="' + id + '"]');
    // remove list item
    ul.removeChild(li);
  }

  function removeItemFromArray(id) {
    // create a new toDoListArray with all li's that don't match the ID
    toDoListArray = toDoListArray.filter(item => item.itemId !== id);
    console.log(toDoListArray);
  }

})();





