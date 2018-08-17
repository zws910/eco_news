import redis


class Config():
    """ 项目配置信息 """
    SECRET_KEY = "\xdf\xf4\xaa\x82&QeX\x0f'jQ\x89b\xff\x11MAC\x8bI\x86d\xc1\xd4X\xe3|\xa7\xbfo\xaa7\xb4A\xda \x11\x7f\xba\x1253\x9e\x91%\xb4\x16"

    # 数据库MySQL相关设置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/eco_news"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Redis相关设置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = '6379'
    # flask_session的配置信息
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400 * 2


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
