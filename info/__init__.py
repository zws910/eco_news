import redis
from flask import Flask
from flask.ext.session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from config import Config

db = SQLAlchemy()
redis_store = None

def creat_app(config_name):
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)
    # 用来存储redis数据
    global redis_store
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDES_PORT)
    # 配置CSRF
    CSRFProtect(app)

    Session(app)

    return app
