from flask import Flask, jsonify
import time
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/status")
def status():
    stat = {'status': True,
            'Name': 'Mychat',
            'Time1': time.time(),
            'Time2': time.asctime(),
            'Time3': datetime.now(),
            'Time4': str(datetime.now()),
            'Time5': datetime.now().isoformat(),
            'Time6': datetime.now().strftime('%Y/%m/%d %H:%M:%S now on server')

            }
    return jsonify(stat)


app.run()
