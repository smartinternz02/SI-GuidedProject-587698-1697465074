from flask import Flask, render_template, request


heart = Flask(__name__)


@heart.route('/')
def helloworld():
    return render_template("index.html")     

if __name__ == '__main__':
    heart.run(debug = False, port = 8000)