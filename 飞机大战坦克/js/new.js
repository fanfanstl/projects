window.onload = function(){
	var startDiv = document.getElementById("start");
	var score = 0;
	//开始游戏
	function play(){
		var box = document.getElementById("box");
		//创建声音标签
		var redio = document.createElement("audio");
		redio.src = "img/game_music.mp3";
		redio.autoplay="autoplay";
		redio.loop ="loop";
		box.appendChild(redio);
		//删除开始游戏
		if(startDiv != null){
			box.removeChild(startDiv);
			startDiv = null;
		}
		//1背景动起来
		var bg1 = document.getElementById("bg1");
		var bg2 = document.getElementById("bg2");
		var bgTimer = setInterval(function(){
			//背景动起来
			bg1.style.top = bg1.offsetTop + 1 + "px";
			bg2.style.top = bg2.offsetTop + 1 + "px";
			if(bg1.offsetTop >= 768){
				bg1.style.top = "-768px";
			}
			if(bg2.offsetTop >= 768){
				bg2.style.top = "-768px";
			}
		},300);
		
		
		//2飞机可拖拽
		var plane = document.getElementById("airplane");
		//鼠标移动执行
		function boxMove(e){
				movex = e.pageX - basex;
				basex = e.pageX;
				movey = e.pageY - basey;
				basey = e.pageY;
				plane.style.top = movey + plane.offsetTop + "px";
				plane.style.left = movex + plane.offsetLeft + "px";
			}
		plane.addEventListener("click",function(e){
			//飞机点击事件
			basex = e.pageX;
			basey = e.pageY;
			//box鼠标移动事件
			box.addEventListener("mousemove",boxMove,false);		
		},false);
		
		
		//3敌人落下
		var tkTimer = setInterval(function(){
			var tank = document.createElement("div");
			tank.classList = "tk";
			box.appendChild(tank);
			tank.style.left = (Math.random() * 413 + 2) + "px";
			tank.style.top = "-50px";
			//坦克移动定时器
			var tkMoveTimer = setInterval(function(){
				tank.style.top = tank.offsetTop + 5 + "px";
				if(tank.offsetTop >= 818){
					box.removeChild(tank);
					clearInterval(tkMoveTimer);
				}
			},100);
			tank.time = tkMoveTimer;
		},800);
		
		
		
		
		//4射击子弹
		//射击子弹定时器
		var bulltTimer = setInterval(function(){
			var bullt = document.createElement("div");
			bullt.className = "zidan";
			bullt.style.top = plane.offsetTop - 10 + "px";
			bullt.style.left = plane.offsetLeft + 54.5 + "px";
			box.appendChild(bullt);
			//创建声音标签
			var redio = document.createElement("audio");
			redio.src = "img/bullet.mp3";
			redio.autoplay="autoplay";
			box.appendChild(redio);
			//子弹移动定时器
			var bulltMoveTimer = setInterval(function(){
				bullt.style.top = bullt.offsetTop - 20 + "px";
				if(bullt.offsetTop <= 0){
					box.removeChild(bullt);
					clearInterval(bulltMoveTimer);
				}
			},100);
			bullt.time = bulltMoveTimer;
		},100);
		
		//分数处理函数
		function countScore(obj){
			var sstr = obj.innerText;
			s = sstr.substring(3,4);
			score ++;
			obj.innerHTML = "分数："+ score;

			
		}
		//5击落敌人和游戏结束
		var shootTimer = setInterval(function(){
			var tkLists = document.getElementsByClassName("tk");
			var zidanLists = document.getElementsByClassName("zidan");
			var scorDiv = document.getElementById("score");
			for(var i = 0;i<tkLists.length;i++){
				for(var j=0;j<zidanLists.length;j++){
					a = zidanLists[j];
					b = tkLists[i];
					if(pzjcFunc(a,b)){
						//碰撞了
						box.removeChild(a);
						box.removeChild(b);
						clearInterval(a.time);
						clearInterval(b.time);
						countScore(scorDiv);
						//创建声音标签
						var redio = document.createElement("audio");
						redio.src = "img/enemy3_down.mp3";
						redio.autoplay="autoplay";
						box.appendChild(redio);
						
					}
				}
				//游戏结束
				if(pzjcFunc(tkLists[i],plane)){
					gameOver();
				}
			}
		},100);
		function gameOver(){
			//创建重新开始标签
			var replayDiv = document.createElement("div");
			replayDiv.id = "end";
			box.appendChild(replayDiv);
			replayDiv.addEventListener("click",function(){
				window.location.reload();
			},false);
			//创建游戏结束图标
			var gameover = document.createElement("div");
			gameover.id = "gameover";
			box.appendChild(gameover);
			//创建声音标签
			var redio = document.createElement("audio");
			redio.src = "img/game_over.mp3";
			redio.autoplay="autoplay";
			box.appendChild(redio);
			//清除box中的鼠标移动事件
			box.removeEventListener("mousemove",boxMove,false);
			//清除所有计时器
			for(var i = 0;i<200;i++){
				clearInterval(i);
			}
		}
		
		//检测两个物体是否发生碰撞方法
		function pzjcFunc(obj1, obj2){
				var obj1Left = obj1.offsetLeft;
				var obj1Width = obj1Left + obj1.offsetWidth;
				var obj1Top = obj1.offsetTop;
				var obj1Height = obj1Top + obj1.offsetHeight;
	
				var obj2Left = obj2.offsetLeft;
				var obj2Width = obj2Left + obj2.offsetWidth;
				var obj2Top = obj2.offsetTop;
				var obj2Height = obj2Top + obj2.offsetHeight;
				
	
				if ( !(obj1Left > obj2Width || obj1Width < obj2Left || obj1Top > obj2Height || obj1Height < obj2Top) ) {
					return true;
				} else {
					return false;
				}
			}	
	}
	startDiv.addEventListener("click",play,false);
	
}
