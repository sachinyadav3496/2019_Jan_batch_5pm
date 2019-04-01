from flask import Flask,render_template,request 
import os,json
BASE_DIR = os.getcwd()

app = Flask(__name__)


@app.route("/")
def index():
    #print(f"\n\n{BASE_DIR}\n\n")
    return render_template("index.html",title='HomePage')
@app.route('/signup/')
def signup():
    return render_template("signup.html",title='signup')

@app.route('/login/',methods=["POST"])
def login():
    name  = request.form['email']
    upass = request.form['password']
    path = os.path.join(BASE_DIR,"static\\data")
    files = os.listdir(path)
    #print(f"\n\n {name} \n\n")
    #print(f"\n\n {files} \n\n")
    if name in files : 
        fname = os.path.join(path,name)
        fp = open(fname)
        data = json.load(fp)
        fp.close()
        if data.get('password') == upass : 
            info = { 
                'Email' : data.get('email'),
                'First Name' : data.get('first_name'),
                'Last Name' : data.get('last_name')
                }
            return render_template("profile.html",title='Profile',data=info)
        else : 
            error = "Invalid Password Try Again"
            return render_template("index.html",title="Main",error=error)

    else : 
        error = "No such User Exists"
        return render_template("index.html",title="Main",error=error)



if __name__ == "__main__" : 

    app.run('localhost',5000,debug=True)