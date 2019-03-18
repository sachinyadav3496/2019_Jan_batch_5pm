
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index2.html")

@app.route('/contact/')
def contact():
    return render_template('contact.html')

if __name__ == "__main__": 
    app.run('localhost',5000,debug=True)