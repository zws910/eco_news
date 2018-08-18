import logging

from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from info import db, creat_app

app = creat_app('development')


@app.route('/')
def index():
    # 测试打印日志
    logging.debug('测试debug')
    logging.warning('测试warning')
    logging.error('测试error')
    logging.fatal('测试fatal')

    # flask中用如下方法打印日志
    # current_app.logger.error('测试error')

    return 'Hello World!'


manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
