from flask import Flask,render_template


app = Flask(__name__)

import random

@app.route('/')
def index():
    pat = []
    for var in range(1,random.randint(5,11)+1):
        pat.append("*"*var)
    print(pat)
    return render_template('index.html',pattern=pat)

@app.route('/data/')
@app.route('/data/<string:name>/')
def data(name=None):
    print(name)
    return render_template('data.html',username=name)


if __name__ == "__main__" : 

    app.run('192.168.1.114',5000,debug=True)