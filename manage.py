import redis
from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session

app = Flask(__name__)


class Config():
    """ 项目配置信息 """
    DEBUG = True

    SECRET_KEY = ""

    # 数据库MySQL相关设置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/eco_news"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Redis相关设置
    REDIS_HOST = '127.0.0.1'
    REDES_PORT = '6379'
    # flask_session的配置信息
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDES_PORT)
    PERMANENT_SESSION_LIFETIME = 86400 * 2


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
