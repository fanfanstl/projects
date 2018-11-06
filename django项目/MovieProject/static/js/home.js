$(function() {
	var swiper = new Swiper('.swiper-container', {
		pagination: '.swiper-pagination',
		paginationClickable: true,
		nextButton: '.swiper-button-next',
		prevButton: '.swiper-button-prev',
		spaceBetween: 30,
		effect: 'fade'
	});

     //收藏
	 $("#box").on("click","#xin",function() {
	     var $spanObj = $(this);
        var color = $(this).css("color");
        var postid = $(this).attr('postid');
        console.log(color);
        //颜色返回rgb格式
        if (color == "rgb(255, 0, 0)") {
            //    取消收藏
            $.ajax({
                    type:"POST",
                    url:"http://127.0.0.1:8000/app/collect/",
                    data:{postid:postid,flag:"cancel"},
                    dataType:"json",
                    success:function(data,textStatus){
                            $spanObj.css("color","grey");
                            console.log(data);
                        }
				});
        }
        else{
            //    添加收藏
            $.ajax({
                type:"POST",
                url:"http://127.0.0.1:8000/app/collect/",
                data:{postid:postid,flag:"add"},
                dataType:'json',
                success:function (data,textStauts) {
                    $spanObj.css("color","red");
                }
            });
        }

    });








});
