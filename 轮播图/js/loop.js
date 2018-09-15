window.onload = function(){
	var box = document.getElementById("box");
	var ul = document.getElementById("list");
	var img = document.getElementById("pic");
	var leftBtn = document.getElementById("left");
	var rightBtn = document.getElementById("right");
	var allLi = document.getElementsByTagName("li")
	
	//1第一个li设置为红色
	allLi[0].style.backgroundColor = "red";
	
	//2让图片循环改变
	var currentNum = 1;
	var timer = setInterval(startLoop, 1000);
	function startLoop(){
		currentNum++;
		changeImg();
	}
	function changeImg(){
		if (currentNum == 9){
			currentNum = 1;
		} else if (currentNum == 0) {
			currentNum = 8;
		}
		img.src = "img/" + currentNum + ".jpg";
		//清空小圆点颜色
		for (var i = 0; i < allLi.length; i++){
			allLi[i].style.backgroundColor = "#aaa";
		}
		//修改小圆点颜色
		allLi[currentNum - 1].style.backgroundColor = "red";
	}
	
	//3鼠标进入box
	//4鼠标离开box
	box.addEventListener("mouseover",function(){
		//停定时器
		clearInterval(timer);
		//显示左右按钮
		leftBtn.style.display = "block";
		rightBtn.style.display = "block";
	},false);
	box.addEventListener("mouseout",function(){
		//重启定时器
		timer = setInterval(startLoop, 1000);
		//隐藏左右按钮
		leftBtn.style.display = "none";
		rightBtn.style.display = "none";
	},false);
	
	//5点击左右按钮
	leftBtn.addEventListener("mouseover", deep,false);
	rightBtn.addEventListener("mouseover", deep,false);
	function deep(){
		this.style.backgroundColor = "rgba(0,0,0,0.6)";
	}
	leftBtn.addEventListener("mouseout", nodeep,false);
	rightBtn.addEventListener("mouseout", nodeep,false);
	function nodeep(){
		this.style.backgroundColor = "rgba(0,0,0,0.2)";
	}
	leftBtn.addEventListener("click", function(){
		currentNum--;
		changeImg();
	},false);
	rightBtn.addEventListener("click", function(){
		currentNum++;
		changeImg();
	},false);
	
	
	//6进入小圆点
	for (var i = 0; i < allLi.length; i++){
		allLi[i].index = i + 1;
		allLi[i].addEventListener("mouseover", function(){
			currentNum = this.index;
			changeImg();
		}, false);
	}
}
