function parseUrl(url){
	if(url.indexOf("?") == -1) {
		return {};
	}
	var query = url.split("?")[1];
	var queryArr = query.split("&");
	var obj = {};
	queryArr.forEach(function(item){
		var key = item.split("=")[0];
		var value = item.split("=")[1];
		obj[key] = decodeURIComponent(value);
	});
	return obj;
}
function play(url) {
	if(Hls.isSupported()) {
		var hls = new Hls();
		// hls.loadSource('https://www.697313.com:65/20190516/Y4xV3No4/index.m3u8');
		hls.loadSource(url);
		hls.attachMedia(video);
		hls.on(Hls.Events.MANIFEST_PARSED,function() {
			video.play();
		});
	}
}
$(function () {
	var video = document.getElementById('video');
	video.style.width = document.documentElement.clientWidth + 'px'
	$.ajax({
		url: '../data.json',
		type: 'get',
		error: function (err) {
			if(err) throw err;
		},
		success: function (ret) {
			console.log(ret);

			for (var key in ret) {
				if (ret[key].name == parseUrl(location.search).name) {
					var current = ret[key]
					$("#cont_jianj_name").html(current.name)
					$("#cont_jianj_text").html(current.jie_shao)
					console.log(current.jieshao);

					play(current.show_url[0][0])
				}
			}
		}
	})
})