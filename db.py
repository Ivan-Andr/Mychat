import time
import datetime

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


# функция для печати каждого сообщения в заданном формате
def print_message(message):
    #    message [{'time': time.ctime()}]
    print(message['time'], message['name'])
    print(message['text'])
    print()


# фукция для печати всей бд
def print_messages(db):
    for message in db:
        print_message(message)


# функция отправки сообщений
def send_message(name, text):
    message = {  # формируем сообщение
        'text': text,
        'time': time.time(),
        'name': name
    }
    db.append(message)


# функция получения сообщений
def get_messages(after):
    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return messages


send_message('Ivan', 'Привет')
messages = get_messages(0)
print_messages(messages)
send_message('Ann', 'Привет, привет!')
messages = get_messages(messages[-1]['time'])
print_messages(messages)