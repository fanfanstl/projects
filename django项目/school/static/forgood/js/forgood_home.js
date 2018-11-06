//轮播图
$(function () {

    var mySwiper = new Swiper('.swiper-container', {
        loop: true,
        // 如果需要前进后退按钮
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        effect: 'cube',
        cubeEffect: {
            slideShadows: true,
            shadow: true,
            shadowOffset: 100,
            shadowScale: 0.6
        },
    });

//    详情按钮事件绑定
    $(".more").click(function () {
        var $goodid = $(this).parent().find(".goodid").text();
        $.getJSON("/forgood/querygood/", {"gid": $goodid}, function (data) {
            // console.log(data);
            if (data.stat_code === 901) {
                window.open("/forclass/login/",target="_self");
            } else {
                $(".temp").html(data["g_name"]);
                $("#myModal").modal();
            }
        });
    });

});

