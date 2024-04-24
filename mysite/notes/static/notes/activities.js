let modal_edit = document.getElementById('modal_edit')
let btn_edit = document.getElementById('btn_notes_edit')

let span = document.getElementsByClassName('close')[0]

btn_edit.onclick = function(){
  modal_edit.style.display = "block"
}


span.onclick = function(){
  modal_edit.style.display = "none"
}

window.onclick = function(event){

  if(event.target == modal_edit){
    modal_edit.style.display = "none"
  }
}

// --------------------------------------------

let modal_02 = document.getElementById("modal_02")
let btn_02 = document.getElementById("btn_notes_02")

btn_02.onclick = function(){
  modal_02.style.display = "block"
}

span.onclick = function(){
  modal_02.style.display = "none"
}


window.onclick = function(event){
  if(event.target == modal_02){
    modal_02.style.display = "none"
  }
}