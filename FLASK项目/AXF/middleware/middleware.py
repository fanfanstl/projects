from flask import request, session, jsonify, redirect, url_for

from app.models import AXFUser

REQUIRE_LOGIN_JSON = [
    '/axf/addtocart/',
    '/axf/changecartstate/',
    '/axf/makeorder/',
]

REQUIRE_LOGIN = [
    '/axf/cart/',
    '/axf/orderdetail/',
    '/axf/orderlistnotpay/',
    "/axf/selectaddress/",
    "/axf/addaddress/",
]


def add_app_middleware(app):
    @app.before_request
    def before_request():
        if request.path in REQUIRE_LOGIN_JSON:

            user_id =session.get('user_id')

            if user_id:
                try:
                    user = AXFUser.query.get(user_id)

                    request.user = user
                except:
                    # return redirect(reverse('axf:login'))
                    data = {
                        'status': 302,
                        'msg': 'user not avaliable'
                    }

                    return jsonify(data=data)
            else:
                # return redirect(reverse('axf:login'))

                data = {
                    'status': 302,
                    'msg': 'user not login'
                }

                return jsonify(data=data)

        if request.path in REQUIRE_LOGIN:
            user_id = session.get('user_id')

            if user_id:
                try:
                    user = AXFUser.query.get(user_id)

                    request.user = user
                except:
                    return redirect(url_for('blue.login'))

            else:
                return redirect(url_for('blue.login'))


# class LoginMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#
#         if request.path in REQUIRE_LOGIN_JSON:
#
#             user_id = request.session.get('user_id')
#
#             if user_id:
#                 try:
#                     user = AXFUser.objects.get(pk=user_id)
#
#                     request.user = user
#                 except:
#                     # return redirect(reverse('axf:login'))
#                     data = {
#                         'status': 302,
#                         'msg': 'user not avaliable'
#                     }
#
#                     return JsonResponse(data=data)
#             else:
#                 # return redirect(reverse('axf:login'))
#
#                 data = {
#                     'status': 302,
#                     'msg': 'user not login'
#                 }
#
#                 return JsonResponse(data=data)
#
#         if request.path in REQUIRE_LOGIN:
#             user_id = request.session.get('user_id')
#
#             if user_id:
#                 try:
#                     user = AXFUser.objects.get(pk=user_id)
#
#                     request.user = user
#                 except:
#                     return redirect(reverse('axf:login'))
#
#             else:
#                 return redirect(reverse('axf:login'))
