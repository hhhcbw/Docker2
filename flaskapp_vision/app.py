from flask import Flask

app = Flask(__name__)


@app.route('/vision')
def main():
    return '机器视觉图形化应用'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
