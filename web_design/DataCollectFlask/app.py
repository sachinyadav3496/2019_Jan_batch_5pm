from flask import Flask,render_template,request,redirect
import csv
import socket
myapp = Flask(__name__)

@myapp.route('/')
def index():
    return render_template('index.html')
@myapp.route('/data')
def data():
    f = open('C:/users/hp/desktop/student.csv')
    data = f.read()
    data = data.split('\n')
    new_data = [ var.split(',') for var in data ]
    s = [ '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp'.join(var) for var in new_data ] 
    s = '<br />'.join(s)
    return s

@myapp.route('/update',methods=['GET','POST'])
def update():
    f = open('c:/users/hp/desktop/student.csv','a',newline='')
    name  = request.form.get('name')
    language = request.form.get('language')
    email  = request.form.get('email')
    ph_no  = request.form.get('ph_no')
    college_name = request.form.get('college_name')
    batch_date = request.form.get('date')
    
    d = (name,language,email,ph_no,college_name,batch_date)
    writer = csv.writer(f)
    writer.writerow(d)
    f.close()
    return "Sucessfully added your data</br><a href='/'>Home</a>"
    #return redirect('/')


myapp.run(host="192.168.1.112",port=5000,debug=True)

