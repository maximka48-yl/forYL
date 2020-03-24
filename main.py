import flask

app = flask.Flask(__name__)


@app.route('/')
def a():
    return """<!doctype html>
                    <html lang="en">
                      <body>
                        Миссия Колонизация Марса
                      </body>
                    </html>"""


@app.route('/index')
def index():
    return """<!doctype html>
                <html lang="en">
                  <body>
                    И на Марсе будут яблони цвести!
                  </body>
                </html>"""


@app.route('/promotion')
def promotion():
    return """<!doctype html>
                <html lang="en">
                  <body>
                    Человечество вырастает из детства.</br>
                    Человечеству мала одна планета.</br>
                    Мы сделаем обитаемыми безжизненные пока планеты.</br>
                    И начнем с Марса!</br>
                    Присоединяйся!
                  </body>
                </html>"""


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/img/mars.jpg"></br>
                    Вот она какая, красная планета.
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run()
