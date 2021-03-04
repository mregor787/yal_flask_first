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


@app.route('/astronaut_selection')
def astronaut_selection():
    return f'''
        <!DOCTYPE html> 
        <html>
            <head>
                <meta charset="utf-8">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" 
                rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" 
                crossorigin="anonymous">
                <link href="{url_for('static', filename='css/style_form.css')}"
                rel="stylesheet">
                <title>Отбор астронавтов</title>
            </head>
            <body>
                <h1>Анкета претендента</h1>
                <h2>на участие в миссии</h2>
                <form class="reg_form">
                    <input type="text" placeholder="Введите фамилию" id="surname" name="surname">
                    <input type="text" placeholder="Введите имя" id="name" name="name">
                    <div style="width: 20px;"></div>
                    <br>
                    <input type="email" placeholder="Введите адрес почты" id="email" name="email">
                    <div class="form-group">
                        <label for="eduSelect">Какое у вас образование?</label>
                        <select class="form-control" id="eduSelect" name="education">
                          <option>Начальное общее</option>
                          <option>Основное общее</option>
                          <option>Среднее общее</option>
                          <option>Среднее профессиональное</option>
                          <option>Высшее</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="form-check">Какие у вас есть профессии?</label>
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="researchEngineerJob">
                            <label class="form-check-label" for="researchEngineerJob">Инженер-исследователь</label>
                        </div>
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="buildingEngineerJob">
                            <label class="form-check-label" for="buildingEngineerJob">Инженер-строитель</label>
                        </div>
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="pilotJob">
                            <label class="form-check-label" for="pilotJob">Пилот</label>
                        </div>
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="meteorologistJob">
                            <label class="form-check-label" for="meteorologistJob">Метеоролог</label>
                        </div>
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="lifeSupportEngineerJob">
                            <label class="form-check-label" for="lifeSupportEngineerJob">Инженер по жизнеобеспечению</label>
                        </div>
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="radiationProtectionEngineerJob">
                            <label class="form-check-label" for="radiationProtectionEngineerJob">Инженер по радиационной защите</label>
                        </div>
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="doctor">
                            <label class="form-check-label" for="doctor">Врач</label>
                        </div>
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="exobiologistJob">
                            <label class="form-check-label" for="exobiologistJob">Экзобиолог</label>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="form-check">Укажите пол</label>
                        <div class="form-check">
                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                          <label class="form-check-label" for="male">
                            Мужской
                          </label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                          <label class="form-check-label" for="female">
                            Женский
                          </label>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="photo">Приложите фотографию</label>
                        <input type="file" class="form-control-file" id="photo" name="file">
                    </div>
                    <div class="form-group form-check">
                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                    </div>
                    <button type="submit" class="btn btn-primary">Отправить</button>
                </form>
            </body>
        </html>
        '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
