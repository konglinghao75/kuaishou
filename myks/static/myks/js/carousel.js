+(function (w) {
	w.zm = {};
	// 获取/设置 translate
	// 节点, 类型, 值
	w.zm.css = function (node, type, val) {
		if (typeof node === "object" && typeof node["transform"] === "undefined") {
			node["transform"] = {};
		}

		if (arguments.length >= 3) {
			//设置
			var text = "";
			node["transform"][type] = val;

			for (item in node["transform"]) {
				if (node["transform"].hasOwnProperty(item)) {
					switch (item) {
						case "translateX":
						case "translateY":
							text += item + "(" + node["transform"][item] + "px)";
							break;
						case "scale":
							text += item + "(" + node["transform"][item] + ")";
							break;
						case "rotate":
							text += item + "(" + node["transform"][item] + "deg)";
							break;
					}
				}
			}
			node.style.transform = node.style.webkitTransform = text;
		} else if (arguments.length == 2) {
			//读取
			val = node["transform"][type];
			if (typeof val === "undefined") {
				switch (type) {
					case "translateX":
					case "translateY":
					case "rotate":
						val = 0;
						break;
					case "scale":
						val = 1;
						break;
				}
			}
			return val;
		}
	}
	// arr ->图片数组
	w.zm.carousel = function (arr, time=2000) {
		
		/** carousel {arr} 生成结构 */
		/** @type {HTMLCanvasElement} */
		var carouselWrap = document.querySelector('.carousel-wrap');
		if (carouselWrap) {
			// 保存原始的小圆点个数
			var pointsLen = arr.length;
			// 无缝
			var needCarousel = carouselWrap.getAttribute('needCarousel');
			needCarousel = needCarousel == null ? false : true;
			if (needCarousel) {
				// 为实现无缝 复制一份数组
				arr = arr.concat(arr);
			}

			var ulN = document.createElement('ul');
			var styleN = document.createElement('style');
			ulN.classList.add('list')
			for (var i = 0; i < arr.length; i++) {
				ulN.innerHTML += '<li><a href="javascript:;"><img src="'+ arr[i] +'" alt=""></a></li>'
			}
			styleN.innerHTML = '.carousel-wrap >.list >li{ width: '+ (1/arr.length*100) +'%;}.carousel-wrap > .list{ width: '+ (arr.length*100) +'%;}'
			carouselWrap.appendChild(ulN);
			document.head.appendChild(styleN);

			// carousel-wrap高度解决
			/** @type {HTMLCanvasElement} */
			var imgN = document.querySelector('.carousel-wrap >.list >li >a >img');
			setTimeout(function() {
				carouselWrap.style.height = imgN.offsetHeight + 'px';
			}, 100);

			// 判断是否有小圆点结构
			/** @type {HTMLCanvasElement} */
			var pointsWrap = document.querySelector('.carousel-wrap >.points-wrap');
			if (pointsWrap) {

				for (var i = 0; i < pointsLen; i++) {
					if (i == 0) {
						pointsWrap.innerHTML += '<span class="active"></span>';							
					}else {
						pointsWrap.innerHTML += '<span></span>';
					}
				}
				/** @type {HTMLCanvasElement} */
				var points = document.querySelectorAll('.carousel-wrap >.points-wrap >span');

			}
		}
		var startX = 0; // 手指开始的位置
		var elementX = 0; // 元素开始的位置
		var translateX = 0;
		var index = 0; // 图片下标
		carouselWrap.addEventListener('touchstart', function (ev) {
			ev = ev || event
			var TouchC = ev.changedTouches[0];
			ulN.style.transition = 'none';

			// 无缝
			if (needCarousel) {
				// 点击第一组的第一张 跳到第二组的第一张
				// 点击第二组的最后一张 跳到第一组的最后一张
				// index代表ul的位置
				var index = zm.css(ulN, 'translateX') / document.documentElement.clientWidth
				if (-index === 0) {
					index = -pointsLen
				}else if (-index == arr.length - 1) {
					index = -(pointsLen - 1)
				}
				zm.css(ulN, 'translateX', index * document.documentElement.clientWidth)
			}

			startX = TouchC.clientX;
			elementX = zm.css(ulN, 'translateX');
			clearInterval(timer); // 关闭自动
		})
		carouselWrap.addEventListener('touchmove', function (ev) {
			ev = ev || event
			var TouchC = ev.changedTouches[0];
			var nowX = TouchC.clientX;
			var disX = nowX - startX; // 滑动的距离
			zm.css(ulN, 'translateX', elementX + disX)
		})
		carouselWrap.addEventListener('touchend', function (ev) {
			ev = ev || event
			// index 抽象了 ul 的实时位置
			index = zm.css(ulN, 'translateX') / document.documentElement.clientWidth

			index = Math.round(index); // 滑动一半
			// 超出控制
			index > 0 ? index = 0:false
			index < 1 - arr.length ? index = 1 - arr.length : false
			// 设置圆点
			setPoints(index)

			ulN.style.transition = '.6s transform';
			zm.css(ulN, 'translateX', index*(document.documentElement.clientWidth))
			if (needAuto) {
				auto() // 开启自动轮播
			}
		})

		/**
		* auto 自动轮播
		*/
		var timer = 0;
		var needAuto = carouselWrap.getAttribute('needAuto');
		needAuto = needAuto == null ? false : true;
		if (needAuto) {
			auto()
		}

		function auto() {
			clearInterval(timer);
			timer = setInterval(function() {
				if (index == 1 - arr.length) {
					ulN.style.transition = 'none';
					index = 1 - arr.length/2;
					zm.css(ulN, 'translateX', index * document.documentElement.clientWidth)
				}
				setTimeout(function() {
					index--;
					ulN.style.transition = '1s transform';
					setPoints(index);
					zm.css(ulN, 'translateX', index * document.documentElement.clientWidth)
				}, 50);
			}, time);
		}

		/**
		* 圆点
		*/
		function setPoints(index) {
			if (!pointsWrap) {
				return;
			}
			for (var i = 0; i < points.length; i++) {
				points[i].classList.remove('active');
			}
			points[-index % pointsLen].classList.add('active');
		}

	}

})(window)
