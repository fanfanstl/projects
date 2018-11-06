# 项目根路径
import os

import redis

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000

def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE")
    driver = dbinfo.get("DRIVER")
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    DEBUG = False
    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "fanding"

    # 将session存储在redis中
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.Redis(host="www.fand.wang", port=6379, password="fanding")

    # 配置文件上传
    UPLOADED_PHOTOS_DEST = BASE_DIR

    # 缓存配置
    CACHE_REDIS_HOST = "www.fand.wang"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_PASSWORD = "fanding"
    CACHE_REDIS_DB = "3"

    # 发送邮件配置
    MAIL_SERVER = "smtp.163.com"
    MAIL_PORT = 25
    # MAIL_USE_SSL = True
    MAIL_USERNAME = "fand1024@163.com"
    MAIL_PASSWORD = "fand102487"
    MAIL_DEFAULT_SENDER = MAIL_USERNAME


class DevelopEnv(Config):
    DEBUG = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "102487",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "NAME": "AXFFLASK",
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo=dbinfo)


class TestingEnv(Config):
    TESTING = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "102487",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "NAME": "AXFFLASK",
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo=dbinfo)


class Staging(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "102487",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "NAME": "AXFFLASK",
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo=dbinfo)


class ProductEnv(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "fanfan",
        "PASSWORD": "102487aa",
        "HOST": "www.fand.wang",
        "PORT": 3306,
        "NAME": "AXFFLASK",
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo=dbinfo)


envs = {
    "develop": DevelopEnv,
    "testing": TestingEnv,
    "staging": Staging,
    "product": ProductEnv,
    "default": DevelopEnv
}
