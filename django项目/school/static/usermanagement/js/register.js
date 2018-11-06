$(function () {

    var $username = $("#username_input");
    var $phone = $("#phone_input");
    var $passwd = $("#passwd_input");
    var $confirm_passwd = $("#confirm_passwd_input");

    //检查用户名
    $username.change(function () {
        var user_name = $(this).val().trim()
        if (user_name.length) {
            $.getJSON('/forclass/checkusername/', {"user_name": user_name}, function (data) {
                if (data["code"] == '900') {
                    //    用户已存在
                    $("#username_info").html("该用户已存在").css("color", "red");
                } else if (data["code"] == '200') {
                    //    用户不存在
                    $("#username_info").html("用户名可用").css("color", "green");
                }
            });
        }
    });

    //检查密码是否一致
    $confirm_passwd.change(function () {
        var passwd = $passwd.val();
        var confirm_passwd = $(this).val();
        if (passwd != confirm_passwd) {
            $("#confirm_passwd_info").html("两次密码输入不一致").css("color", "red");
        } else {
            $("#confirm_passwd_info").html("密码可用").css("color", "green");
        }
    });

    //检查手机号
    $phone.change(function () {
        var phone = $(this).val().trim()
        if (phone.length) {
            $.getJSON('/forclass/checkphone/', {"phone": phone}, function (data) {
                if (data["code"] == '900') {
                    //    用户已存在
                    $("#phone_info").html("该手机号已注册").css("color", "red");
                } else if (data["code"] == '200') {
                    //    用户不存在
                    $("#phone_info").html("手机号输入成功").css("color", "green");
                }
            });
        }
    });

    //表单提交事件
    $("#reg_form").submit(function (e) {
        if (!check()) {
            e.preventDefault()
        }
        else {
            var $passwd = $("#passwd_input");
            var passwd = $passwd.val().trim();
            var $confirm_passwd = $("#confirm_passwd_input");
            var confirm_passwd = $confirm_passwd.val().trim();
            $confirm_passwd.val(md5(confirm_passwd));
            $passwd.val(md5(passwd));
        }
    });

    function check() {
        //    检查用户名、密码、手机号、是否为空
        if (!$("#username_input").val().trim().length) {
            $("#username_info").html("请输入用户名").css("color", "red");
            return false;
        } else if ($("#username_info").css("color") == 'rgb(255, 0, 0)') {
            return false;
        }
        if (!$("#phone_input").val().length) {
            $("#phone_info").html("请输入手机号").css("color", "red");
            return false;
        } else if ($("#phone_info").css("color") == 'rgb(255, 0, 0)') {
            return false;
        }
        if (!$("#passwd_input").val().length) {
            $("#passwd_info").html("密码不能为空").css("color", "red");
            return false;
        }
        if (!$("#confirm_passwd_input").val().length) {
            $("#confirm_passwd_info").html("确认密码不能为空").css("color", "red");
            return false;
        } else if ($("#confirm_passwd_info").css("color") == 'rgb(255, 0, 0)') {
            return false;
        }
        return true;

    }


});