from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title="HomePage")

@app.route("/login/",methods=["POST"])
def login():
    data = {
    'username' : request.form['name'],
    'password' : request.form['password'], } 
    return render_template('login.html',title='login',data=data)

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
    return render_template('login.html',title='Profile',data=data)



if __name__ == "__main__" : 

    app.run(debug=True)