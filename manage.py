from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config():
    """ 项目配置信息 """
    DEBUG = True

    # 数据库MySQL相关设置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/eco_news"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


@app.route('/')
def hello_world():
    return 'Hello World!'


app.config.from_object(Config)
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run()
