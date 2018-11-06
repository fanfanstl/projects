import hashlib

from django.core.mail import send_mail
from django.template import loader

from flask import render_template
from flask_mail import Message

from app.ext import mail
from app.models import Cart, Goods
from settings import SERVER_HOST, SERVER_PORT


def hash_str(source):
    return hashlib.new('sha512', source.encode('utf-8')).hexdigest()


def send_email_activate(username, receive, u_token):
    subject = '%s AXF Activate' % username

    recipient_list = [receive, ]

    username = username,
    activate_url = 'http://{}:{}/axf/activate/?u_token={}'.format(SERVER_HOST, SERVER_PORT, u_token)

    html_message = render_template('user/activate.html', username=username, activate_url=activate_url)
    msg = Message(recipients=recipient_list, html=html_message, subject=subject)
    mail.send(msg)


def get_total_price():
    carts = Cart.query.filter(Cart.c_is_select==True)

    total = 0

    for cart in carts:
        good = Goods.query.get(cart.c_goods_id)
        total += cart.c_goods_num * good.price

    return "{:.2f}".format(total)
