from flask import Flask
from ora_core.ora_checks import Checks, Database
from NoJoy_DI.di import DI
from NoJoy_DI.patterns import DefaultPattern, SingletonPattern

import cx_Oracle

app = Flask(__name__)
di = DI()
di.attempt(Database)

@app.route('/')
def hello_world():
    return

if __name__ == '__main__':
    app.run(threaded=True)
