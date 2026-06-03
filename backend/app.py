from flask import Flask

app = Flask(__name__)


@app.route('/')
def iniciar():
    return 'Está funcionado'


if __name__ == '__main__':
    app.run(debug=True)
