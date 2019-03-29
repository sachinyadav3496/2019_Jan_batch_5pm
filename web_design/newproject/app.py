from flask import Flask,render_template,request
import json
import os
app = Flask(__name__)

location = "C:\\Users\\hp\\Desktop\\batch5pm\\web_design\\newproject\\static\\data"
@app.route('/')
def index():
    return render_template('index.html',title="HomePage")

@app.route("/login/",methods=["POST"])
def login():
    
    uname = request.form['name'].strip().lower()
    password = request.form['password']
    for user in os.listdir(location) : 
        if user == uname : 
            data = json.load(open(os.path.join(location,uname)))
            if data['Password'] == password : 
                return render_template('login.html',title='login',data=data)
            else : 
                error = "Invalid Password Try Again"
                return render_template('index.html',title='error',error=error)


    else : 
        error = "No such User Exists in Our Database"
        return render_template('index.html',title='error',error=error)

    
@app.route("/signup/")
def signup_page():
    return render_template('signup.html',title='signup')


@app.route('/mk_signup/',methods=['POST'])
def signup():
    data = {
    "First Name"  : request.form['fname'],
    "Last Name" :  request.form['lname'],
    "UserName" : request.form['name'],
    "Password": request.form['password'],
    "Email" :  request.form['email'],
    "Phone Number" : request.form['ph_no'],
    "Date of Birth" : request.form['dob'],
    }
    for user in os.listdir(location) : 
        if data["UserName"] == user : 
            error = "User Already Exists Please Try Again"
            return render_template('index.html',title='error',error=error)
    else : 
        fp  = open(os.path.join(location,data["UserName"]),"w")
        json.dump(data,fp)
        fp.close()
        return render_template('login.html',title='Profile',data=data)
    #print(type(request.form['dob']))
    #print(request.form['dob'])
    



if __name__ == "__main__" : 

    app.run(debug=True)