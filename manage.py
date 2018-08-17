import redis
from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session

from config import Config

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


app.config.from_object(Config)
db = SQLAlchemy(app)
# 用来存储redis数据
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDES_PORT)
# 配置CSRF
CSRFProtect(app)

Session(app)

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
