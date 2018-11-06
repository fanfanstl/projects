import uuid

from flask import Blueprint, render_template, redirect, url_for, request, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from app.ext import photos, cache
from app.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, FoodType, Goods, AXFUser, Order, Cart, \
    OrderGoods
from app.views_constant import ALL_TYPE, ORDER_TOTAL, ORDER_PRICE_UP, ORDER_PRICE_DOWN, ORDER_SALE_UP, ORDER_SALE_DOWN, \
    ORDER_STATUS_NOT_RECEIVE, ORDER_STATUS_NOT_SEND, ORDER_STATUS_NOT_PAY, HTTP_OK, HTTP_USER_EXIST

# from app.views_helper import get_total_price
from app.views_helper import send_email_activate, get_total_price

blue = Blueprint("blue", __name__, url_prefix="/axf/")


def init_blue(app):
    app.register_blueprint(blue)


# url(r'^home/', views.home, name='home'),
@blue.route("/home/")
def home():
    main_wheels = MainWheel.query.all()

    main_navs = MainNav.query.all()

    main_mustbuys = MainMustBuy.query.all()

    main_shops = MainShop.query.all()

    main_shop0_1 = main_shops[0:1]

    main_shop1_3 = main_shops[1:3]

    main_shop3_7 = main_shops[3:7]

    main_shop7_11 = main_shops[7:11]

    main_shows = MainShow.query.all()

    # data = {
    #
    #     "main_wheels": main_wheels,
    #     'main_navs': main_navs,
    #     'main_mustbuys': main_mustbuys,
    #     'main_shop0_1': main_shop0_1,
    #     'main_shop1_3': main_shop1_3,
    #     'main_shop3_7': main_shop3_7,
    #     'main_shop7_11': main_shop7_11,
    #     'main_shows': main_shows,
    # }

    return render_template('main/home.html', title="首页", main_wheels=main_wheels, main_namvs=main_navs,
                           main_mustbuys=main_mustbuys, main_shop0_1=main_shop0_1, main_shop1_3=main_shop1_3,
                           main_shop3_7=main_shop3_7, main_shop7_11=main_shop7_11, main_shows=main_shows)


#
# # url(r'^market/', views.market, name='market'),
@blue.route("/market/")
def market():
    return redirect(url_for('blue.market_with_params',
                            typeid=104749,
                            childcid=0,
                            order_rule=0
                            ))


# # url(r'^marketwithparams/(?P<typeid>\d+)/(?P<childcid>\d+)/(?P<order_rule>\d+)/', views.market_with_params, name='market_with_params'),
@blue.route("/marketwithparams/<int:typeid>/<string:childcid>/<string:order_rule>/")
def market_with_params(typeid, childcid, order_rule):
    foodtypes = FoodType.query.all()

    goods_list = Goods.query.filter(Goods.categoryid == typeid)

    if childcid == ALL_TYPE:
        pass
    else:
        goods_list = goods_list.filter(Goods.childcid == childcid)

    if order_rule == ORDER_TOTAL:
        pass
    elif order_rule == ORDER_PRICE_UP:
        goods_list = goods_list.order_by("price")
    elif order_rule == ORDER_PRICE_DOWN:
        goods_list = goods_list.order_by("-price")
    elif order_rule == ORDER_SALE_UP:
        goods_list = goods_list.order_by("productnum")
    elif order_rule == ORDER_SALE_DOWN:
        goods_list = goods_list.order_by("-productnum")

    foodtype = FoodType.query.filter(FoodType.typeid == typeid).first()

    """
        全部分类:0#进口水果:103534#国产水果:103533
        切割  #
            ['全部分类:0', '进口水果:103534', '国产水果:103533']
        切割  :
            [[全部分类, 0], [进口水果, 103534], [国产水果, 103533]]

    """
    foodtypechildnames = foodtype.childtypenames

    foodtypechildname_list = foodtypechildnames.split("#")

    foodtype_childname_list = []

    for foodtypechildname in foodtypechildname_list:
        foodtype_childname_list.append(foodtypechildname.split(":"))

    order_rule_list = [
        ['综合排序', ORDER_TOTAL],
        ['价格升序', ORDER_PRICE_UP],
        ['价格降序', ORDER_PRICE_DOWN],
        ['销量升序', ORDER_SALE_UP],
        ['销量降序', ORDER_SALE_DOWN],
    ]

    # data = {
    #     "title": "闪购",
    #     'foodtypes': foodtypes,
    #     'goods_list': goods_list,
    #     'typeid': int(typeid),
    #     'foodtype_childname_list': foodtype_childname_list,
    #     'childcid': childcid,
    #     'order_rule_list': order_rule_list,
    #     'order_rule_view': order_rule
    # }

    return render_template('main/market.html', title="闪购", foodtypes=foodtypes, goods_list=goods_list, typeid=typeid,
                           foodtype_childname_list=foodtype_childname_list, childcid=childcid,
                           order_rule_list=order_rule_list,
                           order_rule=order_rule)


# # url(r'^cart/', views.cart, name='cart'),
@blue.route("/cart/")
def cart():
    user = request.user

    carts = Cart.query.filter(Cart.c_user_id == user.id)

    # is_all_select = not carts.filter(Cart.c_is_select==False).exists()
    is_all_select = not carts.filter(Cart.c_is_select == False).first()

    title = '购物车'
    carts = carts
    carts_goods = [1,]
    for cart in carts:
        good = Goods.query.get(cart.c_goods_id)
        carts_goods.append(good)
    is_all_select = is_all_select
    total_price = get_total_price()

    return render_template('main/cart.html', title=title, carts=carts, is_all_select=is_all_select,
                           total_price=total_price,carts_goods=carts_goods)


# # url(r'^mine/', views.mine, name='mine'),
@blue.route("/mine/")
def mine():
    user_id = session.get('user_id')

    title = '我的'
    is_login = False

    if user_id:
        user = AXFUser.query.get(user_id)
        is_login = True
        username = user.u_username
        icon = user.u_icon
        order_not_pay = Order.query.filter(Order.o_user_id == user_id).filter(
            Order.o_status == ORDER_STATUS_NOT_PAY).count()
        order_not_receive = Order.query.filter(Order.o_user_id == user_id).filter(
            Order.o_status.in_([ORDER_STATUS_NOT_RECEIVE, ORDER_STATUS_NOT_SEND])).count()
        return render_template("main/mine.html", is_login=is_login, username=username, icon=icon,
                               order_not_pay=order_not_pay, order_not_receive=order_not_receive, title=title)

    return render_template('main/mine.html', title=title, is_login=is_login)


# # url(r'^register/', views.register, name='register'),

@blue.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        title = "注册"
        return render_template('user/register.html', title=title)
    elif request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        icon = request.files.get("icon")
        filename = photos.save(icon, folder="static/uploads/icons", name=icon.filename)
        icon = photos.url(filename)

        # password = hash_str(password)
        password = generate_password_hash(password)

        user = AXFUser()
        user.u_username = username
        user.u_password = password
        user.u_email = email
        user.u_icon = icon

        user.save()

        u_token = uuid.uuid4().hex

        cache.set(u_token, user.id, timeout=60 * 60 * 24)

        send_email_activate(username, email, u_token)

        # return redirect(reverse("axf:login"))
        return redirect(url_for("blue.login"))


# # url(r'^login/', views.login, name='login'),
@blue.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":

        error_message = session.get('error_message')

        title = "登录"

        if error_message:
            del session['error_message']
            error_message = error_message

        return render_template('user/login.html', title=title, error_message=error_message)

    elif request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = AXFUser.query.filter(AXFUser.u_username == username).first()

        if user:

            if check_password_hash(user.u_password, password):

                if user.is_active:

                    session['user_id'] = user.id

                    return redirect(url_for('blue.mine'))
                else:
                    print('not activate')
                    session['error_message'] = 'not activate'
                    return redirect(url_for('blue.login'))
            else:
                print('密码错误')
                session['error_message'] = 'password error'
                return redirect(url_for('blue.login'))
        print('用户不存在')
        session['error_message'] = 'user does not exist'
        return redirect(url_for('blue.login'))


# # url(r'^checkuser/', views.check_user, name='check_user'),
@blue.route("/checkuser/")
def check_user():
    username = request.args.get("username")

    user = AXFUser.query.filter(AXFUser.u_username == username).first()

    data = {
        "status": HTTP_OK,
        "msg": 'user can use'
    }

    if user:
        data['status'] = HTTP_USER_EXIST
        data['msg'] = 'user already exist'
    else:
        pass

    return jsonify(data=data)


# # url(r'^logout/', views.logout, name='logout'),
@blue.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for('blue.mine'))


# # url(r'^activate/', views.activate, name='activate'),
@blue.route("/activate/")
def activate():
    u_token = request.args.get('u_token')

    user_id = cache.get(u_token)

    if user_id:
        cache.delete(u_token)

        user = AXFUser.query.get(user_id)

        user.is_active = True

        user.save()

        return redirect(url_for('blue.login'))

    return render_template('user/activate_fail.html')


# #
# # url(r'^addtocart/', views.add_to_cart, name='add_to_cart'),
@blue.route("/addtocart/")
def add_to_cart():
    goodsid = request.args.get('goodsid')

    cart = Cart.query.filter(Cart.c_user_id == request.user.id).filter(Cart.c_goods_id == goodsid).first()
    if cart:
        cart_obj = cart
        cart_obj.c_goods_num = cart_obj.c_goods_num + 1
    else:
        cart_obj = Cart()
        cart_obj.c_goods_id = goodsid
        cart_obj.c_user_id = request.user.id

    cart_obj.save()

    data = {
        'status': 200,
        'msg': 'add success',
        'c_goods_num': cart_obj.c_goods_num
    }

    return jsonify(data=data)


# # url(r'^changecartstate/', views.change_cart_state, name='change_cart_state'),
@blue.route("/changecartstate/")
def change_cart_state():
    cart_id = request.args.get('cartid')

    cart_obj = Cart.query.get(cart_id)

    cart_obj.c_is_select = not cart_obj.c_is_select

    cart_obj.save()

    is_all_select = not Cart.query.filter(Cart.c_user_id == request.user.id).filter(Cart.c_is_select == False).first()

    data = {
        'status': 200,
        'msg': 'change ok',
        'c_is_select': cart_obj.c_is_select,
        'is_all_select': is_all_select,
        'total_price': get_total_price()
    }

    return jsonify(data=data)


# #
# # url(r'^subshopping/', views.sub_shopping, name='sub_shopping'),
@blue.route("/subshopping/")
def sub_shopping():
    cartid = request.args.get("cartid")

    cart_obj = Cart.query.get(cartid)

    data = {
        'status': 200,
        'msg': 'ok',
    }

    if cart_obj.c_goods_num > 1:
        cart_obj.c_goods_num = cart_obj.c_goods_num - 1
        cart_obj.save()
        data['c_goods_num'] = cart_obj.c_goods_num
    else:
        cart_obj.delete()
        data['c_goods_num'] = 0

    data['total_price'] = get_total_price()

    return jsonify(data=data)


# #
# # url(r'^allselect/', views.all_select, name='all_select'),
@blue.route("/allselect/")
def all_select():
    cart_list = request.args.get('cart_list')

    cart_list = cart_list.split("#")

    carts = Cart.query.filter(Cart.id.in_(cart_list))

    for cart_obj in carts:
        cart_obj.c_is_select = not cart_obj.c_is_select
        cart_obj.save()

    data = {
        'status': 200,
        'msg': 'ok',
        'total_price': get_total_price()
    }

    return jsonify(data=data)


# #
# # url(r'^makeorder/', views.make_order, name='make_order'),
@blue.route("/makeorder/")
def make_order():

    carts = Cart.query.filter(Cart.c_user_id == request.user.id).filter(Cart.c_is_select == True)

    order = Order()

    order.o_user_id = request.user.id

    order.o_price = get_total_price()

    order.save()

    order = Order.query.order_by("-id").first()

    for cart_obj in carts:
        ordergoods = OrderGoods()
        ordergoods.o_order = order.id
        ordergoods.o_goods_num = cart_obj.c_goods_num
        ordergoods.o_goods_id = cart_obj.c_goods_id
        ordergoods.save()
        cart_obj.delete()

    data = {
        "status": 200,
        "msg": 'ok',
        'order_id': order.id
    }

    return jsonify(data)


# #
# # url(r'^orderdetail/', views.order_detail, name='order_detail'),
@blue.route("/orderdetail/")
def order_detail():
    order_id = request.args.get('orderid')

    order = Order.query.get(order_id)
    o_goods = OrderGoods.query.filter(OrderGoods.o_order_id==order.id)
    goods_id = []
    for g in o_goods:
        goods_id.append(g.o_goods_id)
    goods = Goods.query.filter(Goods.id.in_(goods_id))
    print(goods_id)

    title = "订单详情"
    order = order

    return render_template('order/order_detail.html', title=title, order=order,goods=goods)


# #
# # url(r'^orderlistnotpay/', views.order_list_not_pay, name='order_list_not_pay'),
@blue.route("/orderlistnotpay/")
def order_list_not_pay():
    orders = Order.query.filter(Order.o_user_id==request.user.id).filter(Order.o_status==ORDER_STATUS_NOT_PAY)

    title = '订单列表'
    orders = orders

    return render_template('order/order_list_not_pay.html',title=title,orders=orders)
