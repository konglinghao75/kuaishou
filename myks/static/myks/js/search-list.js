$(function () {
	$.ajax({
		url: '../data.json',
		type: 'get',
		error: function (err) {
			if(err) throw err;
		},
		success: function (ret) {
			console.table(ret);

			var tempCont = $('#video-temp').html();
			var htmlText = _.template(tempCont);
			var NewHtml = htmlText({data: ret});
			$(".search-list >.list-wrap").html(NewHtml);
		}
	})
})