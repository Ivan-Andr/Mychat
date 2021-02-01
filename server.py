from flask import Flask, jsonify, request, abort
import time
from datetime import datetime

app = Flask(__name__)
# база данных с сообщениями
db = [
    {
        'text': 'Hello',
        'time': time.time(),  # возвращает количество секунд с 1 января 1970, 00:00:00 (UTC)
        'name': 'Ivan'
    },
    {
        'text': 'Hi, Ivan',
        'time': time.time(),
        'name': 'Ann'
    }
]


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


@app.route("/send", methods=['POST'])
def send_messages():
    if not isinstance(request.json, dict):
        return abort(400)

    name = request.json.get('name')
    text = request.json.get('text')

    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)
    if name == '' or text == '':
        return abort(400)

    message = {  # формируем сообщение
        'text': text,
        'time': time.time(),
        'name': name
    }
    db.append(message)
    return {'ok': True}


@app.route("/messages")
def get_messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)
    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return {'messages': messages[:100]}


app.run()
