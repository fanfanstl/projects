from app import db

# class Main(models.Model):
#     img = models.CharField(max_length=255)
#     name = models.CharField(max_length=64)
#     trackid = models.IntegerField(default=1)
#
#     class Meta:
#         abstract = True
from app.views_constant import ORDER_STATUS_NOT_PAY


class Main(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(255))
    name = db.Column(db.String(64))
    trackid = db.Column(db.Integer, default=1)


# class MainWheel(Main):
#     """
#     axf_wheel(img,name,trackid)
#     """
#
#     class Meta:
#         db_table = 'axf_wheel'

class MainWheel(Main):
    __tablename__ = 'axf_wheel'


# class MainNav(Main):
#     """
#     axf_nav(img,name,trackid)
#     """
#
#     class Meta:
#         db_table = 'axf_nav'

class MainNav(Main):
    __tablename__ = "axf_nav"


# class MainMustBuy(Main):
#     """
#     axf_mustbuy(img,name,trackid)
#     """
#     class Meta:
#         db_table = 'axf_mustbuy'

class MainMustBuy(Main):
    __tablename__ = 'axf_mustbuy'


# class MainShop(Main):
#     """
#     axf_shop(img,name,trackid)
#     """
#
#     class Meta:
#         db_table = "axf_shop"

class MainShop(Main):
    __tablename__ = "axf_shop"


# class MainShow(Main):
#     """
#     axf_mainshow(trackid,name,img,categoryid,brandname,img1,childcid1,productid1,longname1,price1,marketprice1,
#     img2,childcid2,productid2,longname2,price2,marketprice2,img3,childcid3,productid3,longname3,price3,marketprice3)
#     """
#     categoryid = models.IntegerField(default=1)
#     brandname = models.CharField(max_length=64)
#     img1 = models.CharField(max_length=255)
#     childcid1 = models.IntegerField(default=1)
#     productid1 = models.IntegerField(default=1)
#     longname1 = models.CharField(max_length=128)
#     price1 = models.FloatField(default=1)
#     marketprice1 = models.FloatField(default=0)
#     img2 = models.CharField(max_length=255)
#     childcid2 = models.IntegerField(default=1)
#     productid2 = models.IntegerField(default=1)
#     longname2 = models.CharField(max_length=128)
#     price2 = models.FloatField(default=1)
#     marketprice2 = models.FloatField(default=0)
#     img3 = models.CharField(max_length=255)
#     childcid3 = models.IntegerField(default=1)
#     productid3 = models.IntegerField(default=1)
#     longname3 = models.CharField(max_length=128)
#     price3 = models.FloatField(default=1)
#     marketprice3 = models.FloatField(default=0)
#
#     class Meta:
#         db_table = 'axf_mainshow'

class MainShow(Main):
    __tablename__ = "axf_mainshow"

    categoryid = db.Column(db.Integer, default=1)
    brandname = db.Column(db.String(64))
    img1 = db.Column(db.String(255))
    childcid1 = db.Column(db.Integer, default=1)
    productid1 = db.Column(db.Integer, default=1)
    longname1 = db.Column(db.String(128))
    price1 = db.Column(db.Float, default=1)
    marketprice1 = db.Column(db.Float, default=0)
    img2 = db.Column(db.String(255))
    childcid2 = db.Column(db.Integer, default=1)
    productid2 = db.Column(db.Integer, default=1)
    longname2 = db.Column(db.String(128))
    price2 = db.Column(db.Float, default=1)
    marketprice2 = db.Column(db.Integer, default=0)
    img3 = db.Column(db.String(255))
    childcid3 = db.Column(db.Integer, default=1)
    productid3 = db.Column(db.Integer, default=1)
    longname3 = db.Column(db.String(128))
    price3 = db.Column(db.Float, default=1)
    marketprice3 = db.Column(db.Float, default=0)


# class FoodType(models.Model):
#     """
#     axf_foodtype(typeid,typename,childtypenames,typesort)
#     """
#
#     typeid = models.IntegerField(default=1)
#     typename = models.CharField(max_length=32)
#     childtypenames = models.CharField(max_length=255)
#     typesort = models.IntegerField(default=1)
#
#     class Meta:
#         db_table = 'axf_foodtype'

class FoodType(db.Model):
    __tablename__ = "axf_foodtype"

    id = db.Column(db.Integer, primary_key=True)
    typeid = db.Column(db.Integer, default=1)
    typename = db.Column(db.String(32))
    childtypenames = db.Column(db.String(255))
    typesort = db.Column(db.Integer, default=1)


# class Goods(models.Model):
#     """
#     axf_goods(productid,productimg,productname,productlongname,isxf,pmdesc,specifics,price,marketprice,categoryid,
#     childcid,childcidname,dealerid,storenums,productnum) values("11951","http://img01.bqstatic.com/upload/goods/000/001/1951/0000011951_63930.jpg@200w_200h_90Q",
#     "","乐吧薯片鲜虾味50.0g",0,0,"50g",2.00,2.500000,103541,103543,"膨化食品","4858",200,4)
#
#     """
#     productid = models.IntegerField(default=1)
#     productimg = models.CharField(max_length=255)
#     productname = models.CharField(max_length=128)
#     productlongname = models.CharField(max_length=255)
#     isxf = models.BooleanField(default=False)
#     pmdesc = models.BooleanField(default=False)
#     specifics = models.CharField(max_length=64)
#     price = models.FloatField(default=0)
#     marketprice = models.FloatField(default=1)
#     categoryid = models.IntegerField(default=1)
#     childcid = models.IntegerField(default=1)
#     childcidname = models.CharField(max_length=128)
#     dealerid = models.IntegerField(default=1)
#     storenums = models.IntegerField(default=1)
#     productnum = models.IntegerField(default=1)
#
#     class Meta:
#         db_table = 'axf_goods'


class Goods(db.Model):
    __tablename__ = "axf_goods"

    id = db.Column(db.Integer, primary_key=True)
    productid = db.Column(db.Integer, default=1)
    productimg = db.Column(db.String(255))
    productname = db.Column(db.String(128))
    productlongname = db.Column(db.String(255))
    isxf = db.Column(db.Boolean, default=False)
    pmdesc = db.Column(db.Boolean, default=False)
    specifics = db.Column(db.String(64))
    price = db.Column(db.Float, default=0)
    marketprice = db.Column(db.Float, default=1)
    categoryid = db.Column(db.Integer, default=1)
    childcid = db.Column(db.Integer, default=1)
    childcidname = db.Column(db.String(128))
    dealerid = db.Column(db.Integer, default=1)
    storenums = db.Column(db.Integer, default=1)
    productnum = db.Column(db.Integer, default=1)
    carts = db.relationship("Cart", backref="Goods", lazy=True)


# class AXFUser(models.Model):
#     u_username = models.CharField(max_length=32, unique=True)
#     u_password = models.CharField(max_length=256)
#     u_email = models.CharField(max_length=64, unique=True)
#     u_icon = models.ImageField(upload_to='icons/%Y/%m/%d/')
#     is_active = models.BooleanField(default=False)
#     is_delete = models.BooleanField(default=False)
#
#     class Meta:
#         db_table = 'axf_user'

class AXFUser(db.Model):
    __tablename__ = "axf_user"

    id = db.Column(db.Integer, primary_key=True)
    u_username = db.Column(db.String(32), unique=True)
    u_password = db.Column(db.String(256))
    u_email = db.Column(db.String(64), unique=True)
    u_icon = db.Column(db.String(256))
    is_active = db.Column(db.Boolean, default=False)
    is_delete = db.Column(db.Boolean, default=False)

    carts = db.relationship("Cart", backref="AXFUser", lazy=True)
    orderes = db.relationship("Order", backref="AXFUser", lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()


# class Cart(models.Model):
#     c_user = models.ForeignKey(AXFUser)
#     c_goods = models.ForeignKey(Goods)
#
#     c_goods_num = models.IntegerField(default=1)
#     c_is_select = models.BooleanField(default=True)
#
#     class Meta:
#         db_table = 'axf_cart'


class Cart(db.Model):
    __tablename__ = "axf_cart"

    id = db.Column(db.Integer, primary_key=True)
    c_user_id = db.Column(db.Integer, db.ForeignKey(AXFUser.id))
    c_goods_id = db.Column(db.Integer, db.ForeignKey(Goods.id))

    c_goods_num = db.Column(db.Integer, default=1)
    c_is_select = db.Column(db.Boolean, default=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


# class Order(models.Model):
#     o_user = models.ForeignKey(AXFUser)
#     o_price = models.FloatField(default=0)
#     o_time = models.DateTimeField(auto_now=True)
#     o_status = models.IntegerField(default=ORDER_STATUS_NOT_PAY)
#
#     class Meta:
#         db_table = 'axf_order'

class Order(db.Model):
    __tablename__ = "axf_order"

    id = db.Column(db.Integer, primary_key=True)
    o_user_id = db.Column(db.Integer, db.ForeignKey(AXFUser.id))
    o_price = db.Column(db.Float, default=0)
    o_time = db.Column(db.DateTime)
    o_status = db.Column(db.Integer, default=ORDER_STATUS_NOT_PAY)
    ordergoods = db.relationship("OrderGoods", backref="Order", lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()


# class OrderGoods(models.Model):
#     o_order = models.ForeignKey(Order)
#     o_goods = models.ForeignKey(Goods)
#     o_goods_num = models.IntegerField(default=1)
#
#     class Meta:
#         db_table = 'axf_ordergoods'

class OrderGoods(db.Model):
    __tablename__ = "axf_ordergoods"

    id = db.Column(db.Integer, primary_key=True)
    o_order_id = db.Column(db.Integer, db.ForeignKey(Order.id))
    o_goods_id = db.Column(db.Integer, db.ForeignKey(Goods.id))
    o_goods_num = db.Column(db.Integer, default=1)


    def save(self):
        db.session.add(self)
        db.session.commit()

# class Address(models.Model):
#     a_province = models.CharField(max_length=128)
#     a_city = models.CharField(max_length=256)
#     a_county = models.CharField(max_length=256)
#     a_detailed_address = models.CharField(max_length=256)
#     a_phone = models.CharField(max_length=16, default=123)
#     a_username = models.CharField(max_length=32, default="")
#     a_user = models.ForeignKey(AXFUser)

# class Address(db.Model):
#     a_province =
#     a_city =
#     a_county =
#     a_detailed_address =
#     a_phone =
#     a_username =
#     a_user =

# class OrderAddress(models.Model):
#     o_address = models.ForeignKey(Address, default=None)
#     o_order = models.OneToOneField(Order)
