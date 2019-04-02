from flask import Flask,render_template,request,session,redirect,url_for
import os,json
BASE_DIR = os.getcwd()

app = Flask(__name__)

app.secret_key = "toencryptyoursessiondata"

@app.route("/")
def index():
    if 'email' in session :
        name = session['email'] 
        path = os.path.join(BASE_DIR,"static\\data")
        fname = os.path.join(path,name)
        fp = open(fname)
        data = json.load(fp)
        fp.close()
        info = { 
                'Email' : data.get('email'),
                'First Name' : data.get('first_name'),
                'Last Name' : data.get('last_name')
                }
        return render_template("profile.html",title='Profile',data=info,email=True)
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
            #login confirm 
            session['email'] = name 
            return render_template("profile.html",title='Profile',data=info,email=True)
        else : 
            error = "Invalid Password Try Again"
            return render_template("index.html",title="Main",error=error)

    else : 
        error = "No such User Exists"
        return render_template("index.html",title="Main",error=error)




@app.route("/mk_signup/",methods=["GET","POST"]) 
def mk_signup():

    if request.method == "POST" : 
        email = request.form['email']
        fname = request.form['fname']
        lname = request.form['lname']
        password = request.form['password']
        path = os.path.join(BASE_DIR,"static\\data")
        files = os.listdir(path)
        if email not in files : 
            #{"email": "sachin@grras.com", "password": "hello@123", "first_name": "sachin", "last_name": "yadav"}
            data = { 
                'email':email,
                'first_name':fname,
                'last_name':lname,
                'password':password,
            }
            path = os.path.join(path,email)
            f = open(path,'w')
            json.dump(data,f)
            error = "Account Sucessfully Created Please Login"
            return render_template("index.html",title="Main",error=error)
        else : 
            error = "User Already Exists... Login into account"
            return render_template("index.html",title="Main",error=error)

    else : 
         error = "GET Method Not Allowed Please Click Signup to create account"
         return render_template("index.html",title="Main",error=error)


@app.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__" : 

    #app.run('localhost',5000,debug=True)
    app.run("192.168.1.100",5000,debug=True)