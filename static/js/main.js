let requestAdeviceButton = document.querySelector('#parent')
let parentRequestForm = document.querySelector('#parentrequestform')
let donorRequestForm = document.querySelector('#donorrequestform')



requestAdeviceButton.addEventListener('click', function(event){
  if (requestAdeviceForm.style.display === 'none'){
    requestADeviceForm.style.display = 'block'
    event.target.innerText = "Cancel"
  }
  else {
    requestAdeviceForm.style.display = 'none'
    event.target.innerText = "Add New Parent"
  }
})

donorFormButton.addEventListener('click', function(event){
  if (donorForm.style.display === 'none'){
    donorForm.style.display = 'block'
    event.target.innerText = "Cancel"
  }
  else {
    donorForm.style.display = 'none'
    event.target.innerText = "Add New Donor"
  }
})




// document.addEventListener('DOMContentLoaded', function () {
//   let btn = document.querySelector('.button'),
//       loader = document.querySelector('.loader'),
//       check = document.querySelector('.check');
  
//   btn.addEventListener('click', function () {
//     loader.classList.add('active');    
//   });
 
//   loader.addEventListener('animationend', function() {
//     check.classList.add('active'); 
//   });
// });
