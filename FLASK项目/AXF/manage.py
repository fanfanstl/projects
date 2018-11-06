import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from app import create_app

os.environ["FLASK_ENV"] = "develop"
env = os.environ.get("FLASK_ENV","default")
app = create_app(env)


manage = Manager(app=app)
manage.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manage.run()
