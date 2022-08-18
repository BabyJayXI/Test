
from flask import Flask, render_template

app = Flask("JayWebApp")


@app.route('/')
def hello():
    return 'Love'   



@app.route('/Shoes')
def hello():
    return render_template('sass.html')
