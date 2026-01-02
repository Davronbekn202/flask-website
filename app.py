from flask import Flask, render_template, url_for
from link import *
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('link.html')


@app.route('/main')
def main():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
