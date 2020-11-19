var metas = document.getElementsByTagName('meta');
var i;
if (navigator.userAgent.match(/iPhone/i)) {
  for (i=0; i<metas.length; i++) {
    if (metas[i].name == "viewport") {
      metas[i].content = "width=device-width, minimum-scale=1.0, maximum-scale=1.0";
    }
  }
  document.addEventListener("gesturestart", gestureStart, false);
}
function gestureStart() {
  for (i=0; i<metas.length; i++) {
    if (metas[i].name == "viewport") {
      metas[i].content = "width=device-width, minimum-scale=0.25, maximum-scale=1.6";
    }
  }
}
function toggleCollapsibleSectionWithAnimation() {
  this.classList.toggle("collapsible-active");
  var buttonId = this.id;
  var sectionId = buttonId.replace("button","section");
  var content = document.getElementById(sectionId);
  var mHeight = window.getComputedStyle(content).maxHeight;
  if (mHeight !== "0px"){
    content.style.maxHeight = "0px";
  } else {
    content.style.maxHeight = "100%";
  }
}