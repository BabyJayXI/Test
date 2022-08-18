from flask import Flask, render_template

app = Flask("JayWebApp")


@app.route('/')
def hello():
    return render_template('homepage.html')


@app.route('/Shoes')
def shoe_page():
    return render_template('sass.html')


@app.route('/Clothes')
def clothes_page():
    return render_template('badges.html')


@app.route('/Music')
def music_page():
    return render_template('collapsible.html')

# This run my webapp and it starts it with my compatur as the server.
app.run(host="0.0.0.0",port=5000,debug=True)