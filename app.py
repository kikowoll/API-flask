import flask
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

@app.route('/')
def hola_mundo():
    return '<h1>hola kiko wapoooooo</h1>'

if __name__ == '__main__':
    app.run()