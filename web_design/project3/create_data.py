data1 = { 
        'email' : 'sachin@grras.com',
        'password': 'hello@123',
        'first_name' : 'sachin',
        'last_name' : 'yadav',
        }

data2 = { 
        'email' : 'rajat@gmail.com',
        'password': 'redhat',
        'first_name' : 'rajat',
        'last_name' : 'goyal',
        }


import json 
import os
BASE_DIR = os.getcwd()

name = data1['email']
fp = open(os.path.join(BASE_DIR,f"static\\data\\{name}"),"w")
json.dump(data1,fp)
fp.close()


name = data2['email']
fp = open(os.path.join(BASE_DIR,f"static\\data\\{name}"),"w")
json.dump(data2,fp)
fp.close()

