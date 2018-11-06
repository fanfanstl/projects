$(function () {



});

function check_addgood() {
           // 所有内容不允许为空
        if (!$("#goodname_input").val().trim().length) {
            $("#goodname_input_info").html("请输入商品名称").css("color", "red");
            return false;
        }else{
             $("#goodname_input_info").html("");
        }
        if (!$("#phone_input").val().length) {
            $("#phone_input_info").html("请输入手机号").css("color", "red");
            return false;
        }else{
             $("#phone_input_info").html("");
        }
        if (!$("#addr_input").val().length) {
            $("#addr_input_info").html("请输入商品所在地").css("color", "red");
            return false;
        }else{
             $("#addr_input_info").html("");
        }
        if (!$("#des_area").val().length) {
            $("#des_area_info").html("请输入商品描述").css("color", "red");
            return false;
        }else{
             $("#des_area_info").html("");
        }
        if (!$("#img1_input").val().length) {
            $("#img1_input_info").html("请选择商品图片").css("color", "red");
            return false;
        }else{
             $("#img1_input_info").html("");
        }
        if (!$("#img2_input").val().length) {
            $("#img2_input_info").html("请选择商品图片").css("color", "red");
            return false;
        }else{
             $("#img2_input_info").html("");
        }
        if (!$("#price_input").val().length) {
            $("#price_input_info").html("请输入价钱").css("color", "red");
            return false;
        }else{
             $("#price_input_info").html("");
        }
        return true;

    }
