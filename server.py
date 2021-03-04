from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return '''
    <!DOCTYPE html> 
    <html>
        <head></head>
        <body>
            <p>Человечество вырастает из детства.</p>
            <p>Человечеству мала одна планета.</p>
            <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
            <p>И начнем с Марса!</p>
            <p>Присоединяйся!</p>
        </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
