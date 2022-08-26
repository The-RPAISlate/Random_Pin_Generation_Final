from heapq import merge
from this import d
import tkinter as tk
from tkinter import filedialog
# from win10toast import ToastNotifier
import sys
from tkinter import *
import random
import shutil
import os
# import os.path

var = ""
merged_list = ""

class Main:
    classno = {}
    
    def __init__(self):
        list_of_file = os.listdir("./")
        if("readme.txt" in list_of_file):
            pass
        else:
            self.jsontotxtconverter()
        
    def jsontotxtconverter(self):
        base = os.path.splitext("./readme.json")[0]
        os.rename("./readme.json",base + '.txt')
        
    def Exit():
        sys.exit()

    def texttojsonconverter(self):
        list_of_txt_file = ["./readme.txt"]
        for ele in list_of_txt_file:
            base = os.path.splitext(ele)[0]
            os.rename(ele,base + '.json')
        # sys.exit(0)
        self.final()
    
    def final(self):
        f=open('record.txt','r+')
        temp=f.readlines()
        for i in temp:
            temp_list=i.split(",")
            res = [*set(temp_list)]
            for ele in res:
                f.write(ele+",")

    
    #-----------------------------------------------------------------------------#
    def write_details(self):
        # lines = ['RPAISlate', 'Storing the data in the text file']
        f = open('readme.txt', 'r+')
        temp = f.readlines()
        if (len(temp) == 0):
            f.write("\n{\n")
            f.write("\t{")
            f.write("\n\t\t \"Employee Id\""+ ": "+ teachers_id.get()+","+"\n")
            f.write("\t\t \"Teacher's Designation\"" + ": \"" + teachers_designation.get()+"\","+"\n")
            f.write("\t\t \"Username\"" + ": \"" + user_name.get()+"\","+"\n")
            if(len(user_password.get()) < 4):
                f.write("\t\t \"User Password\"" + ":\"" + var +"\","+"\n")
            else:
                f.write("\t\t \"User Password\"" + ":\"" + user_password.get()+"\","+"\n")  
            f.write("\t}")#replaced by niche walla code         
            f.write("\n}")
        else:
            lines = f.readlines()
            # move file pointer to the beginning of a file
            f.seek(0)
            # truncate the file
            f.truncate()

            # start writing lines except the first line
            # lines[1:] from line 2 to last line
            # print(temp)
            f.writelines(temp[:-2])
            f.write("\t},")
            f.write("\n\t{")
            f.write("\n\t\t \"Employee Id\""+ ": "+ teachers_id.get()+","+"\n")
            f.write("\t\t \"Teacher's Designation\"" + ": \"" + teachers_designation.get()+"\","+"\n")
            f.write("\t\t \"Username\"" + ": \"" + user_name.get()+"\","+"\n")
            if(len(user_password.get()) < 4):
                f.write("\t\t \"User Password\"" + ":\"" + var +"\","+"\n")
            else:
                f.write("\t\t \"User Password\"" + ":\"" + user_password.get()+"\","+"\n")  
            f.write("\t}")#replaced by niche walla code         
            f.write("\n}")

    def detailschecker(self,var):
        
        
        if(len(teachers_id.get()) <= 0):
            error_teacherid = tk.Label(
                win,
                text="Please Enter Teacher's id Before Submiting",
                bg = "light grey",
                fg= "red", 
                width= 36,
                height= 0,
                bd=5,
                font=("times", 12, "bold"),
                borderwidth=1,
                relief="groove"
            )
            error_teacherid.place(x=110, y=110)
            return -1
        
        elif(len(teachers_designation.get()) <= 0):
            error_teacherdesignation = tk.Label(
                win,
                text="Please Fill Teacher's Designation Before Submitting",
                bg="light grey",
                fg="red",
                width=36,
                height=0,
                bd=5,
                font=("time",12,"bold"),
                borderwidth=1,
                relief="groove"
            )
            error_teacherdesignation.place(x=110, y=110)
            return -1
            
        elif(len(user_name.get()) <= 0):
            error_username = tk.Label(
                win,
                text="Please Fill User Name Before Submitting",
                bg="light grey",
                fg="red",
                width=36,
                height=0,
                bd=5,
                font=("time",12,"bold"),
                borderwidth=1,
                relief="groove"
            )
            error_username.place(x=110, y=110)
            return -1
        
        elif(len(user_password.get()) < 4 and len(var) <= 0):
            
            # error_password = tk.Label(
            #     win,
            #     text="Please Fill/Genrate Before Submitting",
            #     bg="light grey",
            #     fg="red",
            #     width=36,
            #     height=0,
            #     bd=5,
            #     font=("time",12,"bold"),
            #     borderwidth=1,
            #     relief="groove"
            # )
            # error_password.place(x=110, y=110)
            return -1
        else:
            return 0
    #-----------------------------------------------------------------------------#

def call():
    global merged_list
    obj = Main()
    # global merged_list

    test1=''
    test2=''
    if(len(merged_list)>0 and len(user_password.get())==0):
        test1=teachers_id.get() + ":" + merged_list
        print(test1)
    
    if(len(user_password.get())>0 and len(merged_list)==0):
        test2=teachers_id.get() + ":" + user_password.get()
        print(test2)
    
    if(os.path.exists('record.txt')==False):
        print("Hi")
        f=open('record.txt','w')
        if(len(user_password.get())>0 and len(merged_list)==0):
            f.write(test2)
            f.write(",")
        else:
            f.write(test1)
            f.write(",")
        f.close()
        
    else:
        f=open('record.txt','r')
        for i in f.readlines():
            for k in i.split(","):
                if(k==test1 or k==test2):
                    print("ji")
                    exists = tk.Label(
                        win,
                        text="Record already Exists",
                        bg="light grey",
                        fg="red",
                        width=36,
                        height=0,
                        bd=5,
                        font=("time",12,"bold"),
                        borderwidth=1,
                        relief="groove"
                    )
                    exists.place(x=110, y=110)
                    f.close()
                
                else: 
                    f.close()
                    f=open('record.txt','a')
                    print("In else")
                    if(len(merged_list)>0 and len(user_password.get())==0):
                        f.write(test1)
                        f.write(",")
                    else:
                        f.write(test2)
                        f.write(",")
                    
        
    if(obj.detailschecker(var) == 0):
        obj.write_details()
        obj.texttojsonconverter()
        


def pin_generator():
    
    global merged_list
    merged_list = ""
    
    pin = random.sample(range(10), 4)
    #print (pin)
     
    for ele in pin:
        merged_list += str(ele)
    # print(merged_list)
    
    notify = tk.Label(
        win,
        text="Randomly generated pin is: " + merged_list,
        bg = "light grey",
        fg= "black", 
        width= 26,
        height= 0,
        bd=5,
        font=("times", 12, "bold"),
        borderwidth=1,
        relief="groove"
     )

    notify.place(x=160, y=360)
    global var
    if len(user_password.get())>0: 
        var = user_password.get()
    else:
        var = merged_list

    # print(var)
    # notify.configure(text="Randomly generated pin is: "+ merged_list,width=25

if __name__ == "__main__" :    
    root = tk.Tk()
    win = Tk()
    # toaster = ToastNotifier()
    root.withdraw()
    obj = Main()
    
 
    
    #tk.Entry(root).pack()
    
    ##GUI
    titl = tk.Label(win, bg="black", relief="flat", bd=10, font=("arial", 35))
    titl.pack(fill=X)

    title1=tk.Label(win, text = "Enter", bg = "black", fg = "dark orange", font=("arial", 27),borderwidth=0)
    title1.place(x=115,y=12)

    title2=tk.Label(win, text = "your", bg = "black", fg = "white", font=("arial", 27),borderwidth=0)
    title2.place(x=212,y=12)

    title3=tk.Label(win, text = "Details", bg = "black", fg = "green", font=("arial", 27),borderwidth=0)
    title3.place(x=290,y=12)

    #Set the geometry of Tkinter frame

    #------- J's edit later------------#
    # width,height=autopy.screen.size()
    win.geometry("500x500")
    # win.pack_propagate(0)
    win.resizable(0, 0)

    #Create an Entry widget to accept User Input
    #------- J's edit------------#
    user_name = tk.Label(
        win,
        text="User Name",
        width=13,
        height=2,
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="white",
        borderwidth=0,

    )
    user_name.place(x=50, y=250)

    user_name= Entry(win,
            width=15,
            bd=5,
            validate="key",
            bg="grey",
            fg="white",
            # relief=RIDGE,
            font=("times", 25, "bold"),
            borderwidth=1,
            relief="groove")
    user_name.focus_set()
    user_name.place(x=200,y=250)

    user_password = tk.Label(
        win,
        text="User Pin",
        width=13,
        height=2,
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="green",
        borderwidth=0,

    )
    user_password.place(x=50, y=300)

    user_password= Entry(win,
            width=11,
            bd=5,
            validate="key",
            bg="grey",
            fg="white",
            # relief=RIDGE,
            font=("times", 25, "bold"),
            borderwidth=1,
            relief="groove")
    user_password.focus_set()
    user_password.place(x=200,y=300)

    #To create a submit button for random pin

    #-----------------------------------------------------------------------------#
    #tk.Entry(root).pack()
    # tk.Label(root, text=" ").pack()

#     button_border = tk.Frame(root, highlightbackground = "black", 
#                             highlightthickness = 2, bd=0)
#     button_border.pack()
    #-----------------------------------------------------------------------------#
    random_pin = tk.Button(
            win,
            #button_border,
            text="Random Pin",
            command=pin_generator,
            bd=11,
            font=("times new roman", 12),
            bg="white",
            fg="black",
            height=0,
            width=8,
            # relief=RIDGE,
            borderwidth=6
        )

    random_pin.place(x=370, y=300)

    ##For Inputing Class Teachers Designation
    teachers_designation = tk.Label(
        win,
        text="Designation",
        width=13,
        height=2,
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="white",
        borderwidth=0,

    )
    teachers_designation.place(x=50, y=200)

    teachers_designation =  Entry(win,
            width=15,
            bd=5,
            validate="key",
            bg="grey",
            fg="white",
            # relief=RIDGE,
            font=("times", 25, "bold"),
            borderwidth=1,
            relief="groove")
    teachers_designation.focus_set()
    teachers_designation.place(x=200,y=200)

    teachers_id = tk.Label(
        win,
        text="Teacher Id",
        width=13,
        height=2,
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="dark orange",
        borderwidth=0,

    )
    teachers_id.place(x=50, y=150)

    teachers_id =  Entry(win,
            width=15,
            bd=5,
            validate="key",
            bg="grey",
            fg="white",
            # relief=RIDGE,
            font=("times", 25, "bold"),
            borderwidth=1,
            relief="groove")
    teachers_id.focus_set()
    teachers_id.place(x=200,y=150)
    

    #Create a Button to validate Entry Widget

    submit = tk.Button(
            win,
            text="Submit",
            command=call,
            bd=10,
            font=("times new roman", 18),
            bg="black",
            fg="red",
            height=0,
            width=10,
            # relief=RIDGE,
            borderwidth=0
        )
    submit.place(x=290, y=400)
    
    
    exit = tk.Button(
            win,
            text="Exit",
            command= quit,
            bd=10,
            font=("times new roman", 18),
            bg="black",
            fg="red",
            height=0,
            width=10,
            borderwidth=0
        )
    exit.place(x=90, y=400)


    win.mainloop()