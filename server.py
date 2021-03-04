from flask import Flask, url_for

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


@app.route('/image_mars')
def image_mars():
    return f'''
    <!DOCTYPE html> 
    <html>
        <head>
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <img src="{url_for('static', filename='img/mars.png')}" alt="Mars">
            <p>Вот она какая, красная планета.</p>
        </body>
    </html>
    '''


@app.route('/promotion_image')
def promotion_image():
    return f'''
    <!DOCTYPE html> 
    <html>
        <head>
            <meta charset="utf-8">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
            rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
            crossorigin="anonymous">
            <link href="{url_for('static', filename='css/style.css')}"
            rel="stylesheet">
            <title>Колонизация</title>
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <img src="{url_for('static', filename='img/mars.png')}" alt="Mars">
            <div class="alert alert-dark">Человечество вырастает из детства.</div>
            <div class="alert alert-success">Человечеству мала одна планета.</div>
            <div class="alert alert-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</div>
            <div class="alert alert-warning">И начнем с Марса!</div>
            <div class="alert alert-danger">Присоединяйся!</div>
        </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
