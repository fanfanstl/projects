import uuid

from alipay import AliPay
from flask_restful import Resource, reqparse

from App.settings import APP_ID, APP_PRIVATE_KEY, ALIPAY_PUBLIC_KEY

parse = reqparse.RequestParser()
parse.add_argument("money", type=int, required=True, help="请提供购票金额")


class AliPayResource(Resource):
    def post(self):
        args = parse.parse_args()
        money = args.get("money")
        # 构建支付的客户端  AlipayClient

        alipay_client = AliPay(
            appid=APP_ID,
            app_notify_url=None,  # 默认回调url
            app_private_key_string=APP_PRIVATE_KEY,  # app私钥
            alipay_public_key_string=ALIPAY_PUBLIC_KEY,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            sign_type="RSA",  # RSA 或者 RSA2
            debug=False  # 默认False
        )
        # 使用Alipay进行支付请求的发起

        # 支付主题
        subject = "i9 20核系列 RTX2080"

        order_string = alipay_client.api_alipay_trade_page_pay(
            out_trade_no=uuid.uuid4().hex,
            total_amount=money,
            subject=subject,
            return_url="http://www.1000phone.com",  # 处理支付成功接口
        )

        # 客户端操作
        data = {
            "status": 200,
            "msg": "alipay ok",
            "url": "https://openapi.alipaydev.com/gateway.do?" + order_string
        }
        return data
