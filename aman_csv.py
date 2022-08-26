import csv  
import os 
import pandas as pd


user_input_exists=[]
if(os.path.exists('logs.csv')==False):
    header = ['name',"emp_id","title","time"]
    f=open('logs.csv','w')
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()
    
    name="Bokade"
    emp_id=70
    title="maths"
    time="12"

    user_input_exists.append(name)
    user_input_exists.append(emp_id)
    user_input_exists.append(title)
    user_input_exists.append(time)
    with open('logs.csv','a') as f:
        writer_obj = csv.writer(f)
        writer_obj.writerow(user_input_exists)
        user_input_exists.clear()
        f.close()

else:
    name="Bokade"
    emp_id=70
    title="maths"
    time="12"

    user_input_exists.append(name)
    user_input_exists.append(emp_id)
    user_input_exists.append(title)
    user_input_exists.append(time)
    with open('logs.csv','a') as f:
        writer_obj = csv.writer(f)
        writer_obj.writerow(user_input_exists)
        user_input_exists.clear()
        f.close()
   