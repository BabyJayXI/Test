from flask import Flask

app = Flask("JayWebApp")


@app.route('/')
def hello():
    return 'Something Light'