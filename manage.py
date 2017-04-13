#!flask/bin/python
import os
from flask_script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db


aapp.config.from_object('config')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
