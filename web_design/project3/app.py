from flask import Flask,render_template,request,session,redirect,url_for
import os,json
BASE_DIR = os.getcwd()

app = Flask(__name__)

app.secret_key = "toencryptyoursessiondata"

def connect(host,port,user,password,dbname=None):
    try : 
        import MySQLdb as sql 
        db = sql.connect(host=host,port=port,user=user,password=password,database=dbname)
        cursor = db.cursor()
        return db,cursor 
    except Exception as e : 
        print("!!!Errror!!",e)
        exit(2)


@app.route("/all_users/")
def all_users():
    db,cursor = connect("localhost",3306,'root',"","dubela")
    cursor.execute("select * from user")
    data = []
    all_data = cursor.fetchall()
    for each_data in all_data : 
        d_data = { 
            'Email' : each_data[0],
            'First Name' : each_data[1],
            'Last Name' : each_data[2],
        }
        data.append(d_data)
    return render_template("all_users.html",data=data)

@app.route("/")
def index():
    if 'email' in session :
        email = session['email'] 
        #path = os.path.join(BASE_DIR,"static\\data")
        #fname = os.path.join(path,name)
        #fp = open(fname)
        #data = json.load(fp)
        #fp.close()
        db,cursor = connect("localhost",3306,'root',"","dubela")
        cursor.execute(f"select * from user where email='{email}'")
        data = cursor.fetchone()
        #info = { 
         #       'Email' : data.get('email'),
          #      'First Name' : data.get('first_name'),
           #     'Last Name' : data.get('last_name')
            #    }
        info = { 
                'Email' : data[0],
                'First Name' : data[1],
                'Last Name' : data[2],
                }
        
        cursor.close()
        db.close()
        return render_template("profile.html",title='Profile',data=info,email=True)
    #print(f"\n\n{BASE_DIR}\n\n")
    return render_template("index.html",title='HomePage')
@app.route('/signup/')
def signup():
    return render_template("signup.html",title='signup')

@app.route('/login/',methods=["POST"])
def login():
    email  = request.form['email']
    upass = request.form['password']
    #path = os.path.join(BASE_DIR,"static\\data")
    #files = os.listdir(path)
    #print(f"\n\n {name} \n\n")
    #print(f"\n\n {files} \n\n")
    db,cursor = connect("localhost",3306,'root',"","dubela")
    print("\n\nConnected to database \n\n")
    cursor.execute(f"select * from user where email='{email}'")
    data = cursor.fetchone()
    #if email in os.listdir(path):
    if data : 
        #fname = os.path.join(path,email)
        #fp = open(fname)
        #data = json.load(fp)
        #fp.close()
        #if data.get('password') == upass : 
        if data[3] == upass :  
            """info = { 
                'Email' : data.get('email'),
                'First Name' : data.get('first_name'),
                'Last Name' : data.get('last_name')
                }"""
            info = { 
                'Email' : data[0],
                'First Name' : data[1],
                'Last Name' : data[2]
                }
            #login confirm 
            session['email'] = email
            cursor.close()
            db.close()
            return render_template("profile.html",title='Profile',data=info,email=True)
        else : 
            cursor.close()
            db.close()
            error = "Invalid Password Try Again"
            return render_template("index.html",title="Main",error=error)

    else : 
        cursor.close()
        db.close()
        error = "No such User Exists"
        return render_template("index.html",title="Main",error=error)




@app.route("/mk_signup/",methods=["GET","POST"]) 
def mk_signup():

    if request.method == "POST" : 
        email = request.form['email']
        fname = request.form['fname']
        lname = request.form['lname']
        password = request.form['password']
        #path = os.path.join(BASE_DIR,"static\\data")
        #files = os.listdir(path)
        db,cursor = connect("localhost",3306,'root',"","dubela")
    
        #if email not in files :
        if not cursor.execute(f"select email from user where email='{email}'") :  
            #{"email": "sachin@grras.com", "password": "hello@123", "first_name": "sachin", "last_name": "yadav"}
            #data = { 
             #   'email':email,
              #  'first_name':fname,
               # 'last_name':lname,
                #'password':password,
            #}
            #path = os.path.join(path,email)
            #f = open(path,'w')
            #json.dump(data,f)
            cmd = f"insert into user values('{email}','{fname}','{lname}','{password}')"
            cursor.execute(cmd)
            db.commit()
            error = "Account Sucessfully Created Please Login"
            cursor.close()
            db.close()
            return render_template("index.html",title="Main",error=error)
        else : 
            cursor.close()
            db.close()
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
    
    app.run('localhost',5000,debug=True)
    #app.run("192.168.1.100",5000,debug=True)
