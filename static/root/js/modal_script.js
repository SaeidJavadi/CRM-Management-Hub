const openBtn = document.querySelector("[data-open]");
const closeBtn = document.querySelector("[data-close]");
const modal = document.querySelector("#modal");

// Open the modal when the button is clicked
openBtn.addEventListener("click", () => {
  modal.showModal();
  modal.
});

// Close the modal when the close button is clicked
closeBtn.addEventListener("click", () => {
  modal.close();
});

// Print Function 
function printdiv(elem) {
  var header_str = '<html><head><title>' + document.title  + '</title></head><body>';
  var footer_str = '</body></html>';
  var new_str = document.getElementById(elem).innerHTML;
  var old_str = document.body.innerHTML;
  document.body.innerHTML = header_str + new_str + footer_str;
  window.print();
  document.body.innerHTML = old_str;
  return false;
}