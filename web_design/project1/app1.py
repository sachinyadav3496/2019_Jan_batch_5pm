from flask import Flask,render_template 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
def hello():
    return render_template('one.html')
if __name__ == "__main__" : 

    app.run('localhost',5000,debug=True)