from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    page = """
    <h1 style='color:red'>
    Welcome To First Flask Powered Web Page  
    Fun Right
    </h1>
    <a href='/data/'>Click Me!</a>
    <a href='http://grras.com'>Grras Solutions</a>
    """
    return page 

@app.route('/data/')
def data():
    page = """
    <h1> ohh you are at data page </h1>
    <a href='/'>Click Me!</a>
     """
    return page 


if __name__ == "__main__" : 

    app.run('localhost',8080,debug=True)