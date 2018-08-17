from flask import Flask

app = Flask(__name__)


class Config():
    """ 项目配置信息 """
    DEBUG = True


@app.route('/')
def hello_world():
    return 'Hello World!'


app.config.from_object(Config)

if __name__ == '__main__':
    app.run()
