from flask_bootstrap import Bootstrap
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES, configure_uploads

db = SQLAlchemy()
migrate = Migrate()
photos = UploadSet('photos', IMAGES)
cache = Cache(config={'CACHE_TYPE': 'redis'})
mail = Mail()


def init_ext(app):
    db.init_app(app)
    migrate.init_app(db=db, app=app)
    DebugToolbarExtension(app)
    Bootstrap(app)
    Session(app)
    configure_uploads(app, photos)
    cache.init_app(app)
    mail.init_app(app)

