from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from info import db, creat_app

app = creat_app('development')


@app.route('/')
def hello_world():
    return 'Hello World!'


manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
