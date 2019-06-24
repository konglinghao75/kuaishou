!(function () {
	var styleN = document.createElement('style');
	var w = document.documentElement.clientWidth/16;
	styleN.innerHTML = "html{font-size:"+ w +"px!important;}";
	document.head.appendChild(styleN);
})()
// 阻止默认行为
// document.addEventListener('touchstart', function (ev) {
// 	ev = ev || event;
// 	ev.preventDefault();
// }, {passive: true})
