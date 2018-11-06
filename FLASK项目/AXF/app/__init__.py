from flask import Flask

from app.ext import db, init_ext
from app.views import init_blue
from middleware.middleware import add_app_middleware
from settings import envs


def create_app(env):
    app = Flask(__name__,static_folder="../static", template_folder="../templates")

    # 添加路由
    init_blue(app)

    # 从配置文件导入配置
    app.config.from_object(envs.get(env))

    # 初始化三方插件
    init_ext(app)

    # 添加中间件
    add_app_middleware(app)

    return app
