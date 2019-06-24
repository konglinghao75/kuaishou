$(function () {
	$.ajax({
		url: '../data.json',
		type: 'get',
		error: function (err) {
			if(err) console.log(err);;
		},
		success: function (ret) {
			console.table(ret);

			fn(ret)
			
			// var tempCont = $('#movie-temp').html();
			// var htmlText = _.template(tempCont);
			// var NewHtml = htmlText({data: ret});
			// $("#movie-row").html(NewHtml);
		}
	})

	function fn(arr) {

		var tempCont = $('#movie-temp').html();
		var htmlText = _.template(tempCont);
		var NewHtml = htmlText({data: arr});
		$("#movie-row").html(NewHtml);

		// var wap = $('.main');
		var offTop = function (ele) {
			var top = null;
			var eleTop = ele.offsetTop;
			var eleParent = ele.offsetParent;
			top += eleTop;
			while (eleParent) {
				top += eleParent.offsetTop;
				eleParent = eleParent.offsetParent;
			}
			return top;
		}

		function loadimg(img) {

			var winTop = $(window).height() + $(window).scrollTop();
			var imgTop = offTop(img) + img.offsetHeight;
			if (winTop > imgTop) {
				if (img.isload == true) {
					return
				}
				var imgs = new Image;
				imgs.src = img.getAttribute("data-src")
				imgs.onload = function () {
					img.src = this.src;
				}
				img.isload = true;
			}
		}


		var imgs = $('img');
		console.log(imgs);
		function allload() {

			$.each(imgs, function (index, value) {

				if (imgs[index].isload) {
					return;
				}

				loadimg(imgs[index])
			})
		}

		setTimeout(function () {
			allload()
		}, 1000)

		$(window).scroll(function () {
			allload()
		})
	}

	
})
