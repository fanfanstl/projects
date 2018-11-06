$(function () {
    //表单提交事件
    $("#reg_form").submit(function (e) {
        if (!check()) {
            e.preventDefault()
        }
        else {
            var $passwd = $("#passwd_input");
            var passwd = $passwd.val().trim();
            $passwd.val(md5(passwd));
        }
    });

    function check() {
        //    检查用户名、密码、手机号、是否为空
        if (!$("#username_input").val().trim().length) {
            $("#username_info").html("请输入用户名").css("color", "red");
            return false;
        }
        if (!$("#passwd_input").val().length) {
            $("#passwd_info").html("密码不能为空").css("color", "red");
            return false;
        }
        return true;

    }

});