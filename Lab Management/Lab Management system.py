from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
import time
from PIL import Image, ImageTk
from num2words import num2words
import math
import time

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="USERNAME",
    password="PASSWORD",
    database="DATABASE_NAME",
    charset="utf8")

mycursor = mydb.cursor()

root = tk.Tk()
root.title("Lab Management System")
root.geometry("350x250")
root.config(bg = "cyan")

project = tk.StringVar()
pr = tk.StringVar()

name =tk.StringVar()
email =tk.StringVar()
pas =tk.StringVar()
repas =tk.StringVar()
coun =tk.StringVar()
state =tk.StringVar()
city =tk.StringVar()
code =tk.StringVar()
n =tk.StringVar()

lis = []

query = """SELECT LABNAME FROM LAB"""
mycursor.execute(query)

myresult = mycursor.fetchall()

for x in myresult:
    lis.append(x)

#Forget Password

def co(Email):
    global lab_em
    global lab_pa
    global newWindow
    global submit
    global date
    global ent_pa
    print("Yeh")
    lab_em.config(text = "New Pass")
    lab_pa.config(text = "Confirm Pass")
    newWindow.title("Change Password")
    submit.config(command = lambda : chan(Email))
    date.place_forget()
    ent_pa.place(x = 125, y = 100, anchor = W)

def chan(Email):
    global button
    np = email.get()
    cp = pas.get()
    email.set("")
    pas.set("")
    print(np)
    print(cp)
    if np == cp:
        sql = "UPDATE credentials SET PASSWORD = %s WHERE EMAIL = %s"
        mycursor.execute(sql, (np, Email))
        mydb.commit()
        messagebox.showinfo("Welcome to our community", "Password changed Successful!")
        button.place(x=110, y = 160, anchor = CENTER)
    else:
        messagebox.showerror("Wrong Entry", "Password not matching with confirm password")
        captcha()
        cap_ca.config(text = CAP)

def he():
    global newWindow
    newWindow.destroy()
    
def aam():
    he()
    Log()
        
def w():
    messagebox.showerror("Wrong DOB", "Invalid DOB entered for this email")

def wr():
    messagebox.showerror("No account", "No account exists for this email")
    
def for_sub():
    global z
    if z != 2:
        messagebox.showerror("No Input!", "Please select Date of Birth")
    else:
        global DOB
        Email = email.get()
        email.set("")
        pas.set("")
        cap.set("")
        print(Email)
        print(DOB)
        
        query = """SELECT count(*) FROM credentials where EMAIL = %s"""
        mycursor.execute(query, (Email,))
        result=mycursor.fetchone()
        number_of_rows=result[0]
        if number_of_rows == 0:
            wr()
        else:
            query = """SELECT count(*) FROM credentials where EMAIL = %s and DOB = %s"""
            mycursor.execute(query, (Email, DOB))
            result=mycursor.fetchone()
            number_of_rows=result[0]
            if number_of_rows == 0:
                w()
            else:
                co(Email)

        print("")

def lad(event):
    global z
    global submit
    global ent_em
    cal.place(x= 217, y=105, anchor = CENTER)
    sub_dob.place(x = 238, y = 25, anchor = CENTER)
    ent_em.place_forget()
    submit.place_forget() 
    z = 1

def dobed(event):
    global DOB
    global z
    global submit
    global ent_em
    DOB = cal.get_date()
    date.config(text = DOB)
    cal.place_forget()
    sub_dob.place_forget()
    ent_em.place(x = 125, y = 60, anchor = W)
    submit.place(x = 270, y = 160, anchor = CENTER) 
    z = 2

def For():
    global d
    global cap_ca
    global newWindow
    global lab_em
    global ent_em
    global lab_pa
    global ent_pa
    global label
    global submit
    global button

    global date
    global cal
    global sub_dob

    d.set("")
    newWindow = Toplevel(root)
    newWindow.title("Forgot Password")
    newWindow.geometry("350x210")
    newWindow.config(bg = "cyan")
    newWindow.iconphoto(False, tk.PhotoImage(file="D:\Mayank\Tinkering\Coding\Python\Icon\globe.png"))
    captcha()
    button = Button(newWindow, text = "Move to Login", fg = "white", bg = "blue", font = ("Comic Sans MS", 13, "bold"), command = aam)

    lab_em = Label(newWindow, text = "Email", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_em.place(x = 20, y = 60, anchor = W)
    ent_em = Entry(newWindow, textvariable = email, width = 25, font = ("Comic Sans MS", 10, "bold"))
    ent_em.place(x = 125, y = 60, anchor = W)

    lab_pa = Label(newWindow, text = "DOB", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_pa.place(x = 20, y = 100, anchor = W)

    ent_pa = Entry(newWindow, textvariable = pas, width = 25, font = ("Comic Sans MS", 10, "bold"))

    date = Label(newWindow, text = " Click to Select DOB ", fg = "white", bg = "blue", font = ("Comic Sans MS", 12, "bold"))
    date.place(x = 227, y = 100, anchor = CENTER)
    date.bind("<Button-1>", lad)
    cal = Calendar(newWindow, selectmode = 'day', year = 2020, month = 5, day = 22)
    sub_dob = Label(newWindow, text = "Submit", fg = "white", bg = "blue", font = ("Comic Sans MS", 8, "bold"))
    sub_dob.bind("<Button-1>", dobed)

    submit = Button(newWindow, text = "Submit", fg = "white", bg = "blue", font = ("Comic Sans MS", 13, "bold"), command = for_sub)
    submit.place(x = 270, y = 160, anchor = CENTER) 
    
#Login 
cap =tk.StringVar()
d = tk.StringVar()

CAP = ""

def captcha():
    global CAP
    import random
    import array
    MAX_LEN = 7
     
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']
     
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']
     
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '>',
               '*', '(', ')', '<']
     
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
     
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
     
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        
    #CAP = temp_pass
    CAP = ""

def ried(ab):
    global d
    global cap_ca
    global l
    global newWindow
    print("Success")
    print("Hi "+ab)
    cap_ca.config(text = "Captcha")
    l = Label(newWindow, textvariable = pr, fg = "blue2",  bg = "cyan", font = ("Comic Sans MS", 20, "bold"))
    l.place(x = 25, y = 25, anchor = W)
    dab(ab)

    def di():
        global lab_em
        global ent_em
        global lab_pa
        global ent_pa
        global lab_ca
        global cap_ca
        global ent_ca
        global label
        global submit
    
        lab_em.place_forget()
        ent_em.place_forget()
        
        lab_pa.place_forget()
        ent_pa.place_forget()
        
        lab_ca.place_forget()
        cap_ca.place_forget()
        ent_ca.place_forget()

        submit.place_forget()

        newWindow.title("Dashboard")

    di()

    
def wred():
    global button
    global x
    x += 1
    print("Fail")
    messagebox.showerror("Wrong credentials", "Invalid Username or Password")
    captcha()
    cap_ca.config(text = CAP)
    if x >= 3:
        button.config(text = "Forgot Password")
        button.config(command = For)
        button.place(x=110, y = 200, anchor = CENTER)
    
def log_sub():
    fail = 0
    Email = email.get()
    Pass = pas.get()
    Cap = cap.get()
    email.set("")
    pas.set("")
    cap.set("")
    print(Email)
    print(Pass)
    print(Cap)
    
    if Cap != CAP:
        messagebox.showerror("Wrong Verfication", "Invalid Captcha")
        captcha()
        cap_ca.config(text = CAP)

    if Cap == CAP:
        query = """SELECT count(*) FROM credentials where EMAIL = %s and PASSWORD = %s"""
        mycursor.execute(query, (Email,Pass))
        result=mycursor.fetchone()
        
        query = """SELECT NAME FROM credentials where EMAIL = %s and PASSWORD = %s"""
        mycursor.execute(query, (Email,Pass))
        ab=mycursor.fetchone()
        ab = (str(ab)[2:-3])
        print(ab)
        number_of_rows=result[0]
        if number_of_rows == 1:
            ried(ab)
        else:
            wred()  

    print("")

def Log():
    global d
    global cap_ca
    global newWindow
    global lab_em
    global ent_em
    global lab_pa
    global ent_pa
    global lab_ca
    global cap_ca
    global ent_ca
    global label
    global submit
    global button

    d.set("")
    newWindow = Toplevel(root)
    newWindow.title("Login")
    newWindow.geometry("350x250")
    newWindow.config(bg = "cyan")
    newWindow.iconphoto(False, tk.PhotoImage(file="D:\Mayank\Tinkering\Coding\Python\Icon\globe.png"))
    captcha()
    button = Button(newWindow, text = "Move to Login", fg = "white", bg = "blue", font = ("Comic Sans MS", 13, "bold"), command = m)

    lab_em = Label(newWindow, text = "Email", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_em.place(x = 20, y = 60, anchor = W)
    ent_em = Entry(newWindow, textvariable = email, width = 25, font = ("Comic Sans MS", 10, "bold"))
    ent_em.place(x = 125, y = 60, anchor = W)

    lab_pa = Label(newWindow, text = "Password", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_pa.place(x = 20, y = 100, anchor = W)
    ent_pa = Entry(newWindow, textvariable = pas, width = 25, font = ("Comic Sans MS", 10, "bold"), show = "*")
    ent_pa.place(x = 125, y = 100, anchor = W)

    lab_ca = Label(newWindow, text = "Captcha", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_ca.place(x = 20, y = 140, anchor = W)
    cap_ca = Label(newWindow, text = CAP, bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    cap_ca.place(x = 125, y = 140, anchor = W)
    ent_ca = Entry(newWindow, textvariable = cap, width = 8, font = ("Comic Sans MS", 10, "bold"))
    ent_ca.place(x = 295, y = 140, anchor = CENTER)

    submit = Button(newWindow, text = "Submit", fg = "white", bg = "blue", font = ("Comic Sans MS", 13, "bold"), command = log_sub)
    submit.place(x = 270, y = 200, anchor = CENTER) 

#Register
global z
z = 0
global y
y = 0

Gen = ""

def de():
    global newWindow
    newWindow.destroy()
    
def m():
    de()
    Log()
        
def reg_sub():                    
    global DOB
    global z
    global mycursor
    if z != 2:
        messagebox.showerror("No DOB selected!", "You have not entered Date of Birth")
    else:
        Name = name.get()
        g = v.get()
        Email = email.get()
        Pass = pas.get()
        Repass = repas.get()
        if Pass != Repass :
            messagebox.showerror("Invalid Match!", "Your password does not match with confirm password")
        Coun = coun.get()
        State = state.get()
        City = city.get()
        if g == 1:
            Gen = "Male"
        elif g == 2:
            Gen = "Female"
        else:
            messagebox.showerror("No Gender selected!", "You have not selected Gender")
        if g == 1 or g == 2:
            if Pass == Repass :
                mycursor = mydb.cursor() 
                sql = "INSERT INTO credentials (Name, Gender, Email, Password, Dob, Country, State, City)\
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (Name, Gen, Email, Pass, DOB, Coun, State, City)
                   
                mycursor.execute(sql, val)
                mydb.commit()

                name.set("")
                email.set("")
                pas.set("")
                repas.set("")
                coun.set("")
                state.set("")
                city.set("")
                date.config(text = " Click to Select DOB ")
                messagebox.showinfo("Welcome to our community", "Registration Successful!")
                button.place(x=110, y = 410, anchor = CENTER)
                
                print(Name)
                print(Gen)
                print(Email)
                print(Pass)
                print(Repass)
                print(DOB)
                print(Coun)
                print(State)
                print(City)
                print("")
        
def label_clicked(event):
    global z
    cal.place(x= 225, y=240, anchor = CENTER)
    sub_dob.place(x = 246, y = 160, anchor = CENTER)
    ent_nat.place_forget()
    ent_sta.place_forget()
    z = 1

def dob_clicked(event):
    global DOB
    global z
    DOB = cal.get_date()
    date.config(text = DOB)
    ent_nat.place(x= 125, y=280, anchor = W)
    ent_sta.place(x = 125, y = 320, anchor = W)
    cal.place_forget()
    sub_dob.place_forget()
    z = 2
    
def Reg():
    global newWindow
    newWindow = Toplevel(root)
    newWindow.title("Register")
    newWindow.geometry("350x450")
    newWindow.config(bg = "cyan")
    newWindow.iconphoto(False, tk.PhotoImage(file="D:\Mayank\Tinkering\Coding\Python\Icon\globe.png"))
    global lab_na
    global ent_na
    global lab_gen
    global v
    global M
    global F
    global lab_pa
    global ent_pa
    global lab_email
    global ent_email
    global lab_rep_pa
    global ent_rep_pa
    global lab_dob
    global date
    global cal
    global sub_dob
    global lab_nat
    global ent_nat
    global lab_sta
    global ent_sta
    global lab_cit
    global ent_cit
    global submit
    global status
    global button
    button = Button(newWindow, text = "Move to Login", fg = "white", bg = "blue", font = ("Comic Sans MS", 13, "bold"), command = m)
    
    lab_na = Label(newWindow, text = "Name", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_na.place(x = 20, y = 40, anchor = W)
    ent_na = Entry(newWindow, textvariable = name, width = 25, font = ("Comic Sans MS", 10, "bold"))
    ent_na.place(x = 125, y = 40, anchor = W)

    lab_gen = Label(newWindow, text = "Gender", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_gen.place(x = 20, y = 80, anchor = W)
    v = tk.IntVar()
    M = tk.Radiobutton(newWindow, bg = "cyan", text="Male", font = ("Comic Sans MS", 12, "bold"), variable=v, value=1)
    M.place(x= 170, y=80, anchor = CENTER)
    F = tk.Radiobutton(newWindow, bg = "cyan", text="Female", font = ("Comic Sans MS", 12, "bold"), variable=v, value=2)
    F.place(x= 270, y=80, anchor = CENTER)

    lab_em = Label(newWindow, text = "Email", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_em.place(x = 20, y = 120, anchor = W)
    ent_em = Entry(newWindow, textvariable = email, width = 25, font = ("Comic Sans MS", 10, "bold"))
    ent_em.place(x = 125, y = 120, anchor = W)

    lab_pa = Label(newWindow, text = "Password", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_pa.place(x = 20, y = 160, anchor = W)
    ent_pa = Entry(newWindow, textvariable = pas, width = 25, font = ("Comic Sans MS", 10, "bold"))
    ent_pa.place(x = 125, y = 160, anchor = W)

    lab_rep_pa = Label(newWindow, text = "Confirm", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_rep_pa.place(x = 20, y = 200, anchor = W)
    ent_pa = Entry(newWindow, textvariable = repas, width = 25, font = ("Comic Sans MS", 10, "bold"))
    ent_pa.place(x = 125, y = 200, anchor = W)

    lab_dob = Label(newWindow, text = "DOB", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_dob.place(x = 20, y = 240, anchor = W) 

    date = Label(newWindow, text = " Click to Select DOB ", fg = "white", bg = "blue", font = ("Comic Sans MS", 12, "bold"))
    date.place(x = 225, y = 240, anchor = CENTER)
    date.bind("<Button-1>", label_clicked)
    cal = Calendar(newWindow, selectmode = 'day', year = 2020, month = 5, day = 22)
    sub_dob = Label(newWindow, text = "Submit", fg = "white", bg = "blue", font = ("Comic Sans MS", 8, "bold"))
    sub_dob.bind("<Button-1>", dob_clicked)

    lab_nat = Label(newWindow, text = "Country", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_nat.place(x = 20, y = 280, anchor = W)
    ent_nat = Entry(newWindow, textvariable = coun, width = 25, font = ("Comic Sans MS", 10, "bold"))
    ent_nat.place(x = 125, y = 280, anchor = W)

    lab_sta = Label(newWindow, text = "State", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_sta.place(x = 20, y = 320, anchor = W)
    ent_sta = Entry(newWindow, textvariable = state, width = 25, font = ("Comic Sans MS", 10, "bold"))
    ent_sta.place(x = 125, y = 320, anchor = W)

    lab_cit = Label(newWindow, text = "City", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_cit.place(x = 20, y = 360, anchor = W)
    ent_cit = Entry(newWindow, textvariable = city, width = 25, font = ("Comic Sans MS", 10, "bold"))
    ent_cit.place(x = 125, y = 360, anchor = W)

    submit = Button(newWindow, text = "Submit", fg = "white", bg = "blue", font = ("Comic Sans MS", 13, "bold"), command = reg_sub)
    submit.place(x = 270, y = 410, anchor = CENTER) 

#Dashboard
def z():
    global canvas
    global can
    cas.pack_forget()
    pr.set("")
    project.set("")

def A():
    global newWindow
    global l
    global lab_L
    global ent_L
    global Ty
    global submit
    
    global lab
    newWindow.geometry("350x200")
    z()
    pr.set("Select Computer Lab")
    l.config(fg = "blue2")

    def Sub():
        global lab_L
        global ent_L
        global Ty
        global submit
        global Co
        Co = code.get()
        print(Co)
        
        query = """SELECT count(*) FROM lab where ID = %s"""
        mycursor.execute(query, (Co,))
        c = mycursor.fetchone()
        c = (str(c)[1:-2])
        print(c)
        c = int(c)
        if c == 1:
            print("Yey\n")
            lab_L.place_forget()
            ent_L.place_forget()
            Ty.place_forget()
            submit.place_forget()

            global cas
            global l
            global newWindow
            global lab
            newWindow.geometry("350x250")
            l.config(fg = "black")
            pr.set("Welcome to "+lab+" lab")
            i = tk.PhotoImage(file=r"D:\Mayank\Tinkering\Coding\Python\Lab Management\Dashboard.png")
            newWindow.i = i
            cas.create_image((0,0), image=i, anchor='nw')
            cas.pack(side = BOTTOM, pady = 20, padx = 20)
            
        else:
            print("Bye\n")

    def sel(event):
        global lab
        lab = event.widget.get()
        print(lab)

    lab_L = Label(newWindow, text = "Enter Lab Code", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    lab_L.place(x = 85, y = 115, anchor = W)
    
    ent_L = Entry(newWindow, textvariable = code, width = 8, font = ("Comic Sans MS", 10, "bold"))
    ent_L.place(x = 235, y = 115, anchor = W)

    Ty = ttk.Combobox(newWindow, width = 20, textvariable = n)
    Ty['values'] = lis
    Ty.current()
    Ty.set("Please select lab")
    Ty.bind("<<ComboboxSelected>>", sel)
    Ty.place(x = 175, y = 73, anchor = CENTER)

    submit = Button(newWindow, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = Sub)
    submit.place(x = 175, y = 163, anchor = CENTER)
    
def p():
    global canvas
    global pro
    pro.config(fg = "blue2")
    project.set("My Portfolio")
    img = tk.PhotoImage(file=r"D:\Mayank\Tinkering\Coding\Python\Lab Management\Portfolio.png")
    root.img = img
    canvas.create_image((0,0), image=img, anchor='nw')
    can.pack_forget()
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
        
def c():
    global canvas
    global pro
    pro.config(fg = "blue2")
    project.set("Contact Me")
    img = tk.PhotoImage(file=r"D:\Mayank\Tinkering\Coding\Python\Lab Management\Contact.png")
    root.img = img
    canvas.create_image((0,0), image=img, anchor='nw')
    can.pack_forget()
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    

def dab(ab):
    global newWindow
    def da():
        global cas
        global l
        l.config(fg = "black")
        pr.set("Welcome "+ab)
        i = tk.PhotoImage(file=r"D:\Mayank\Tinkering\Coding\Python\Lab Management\Dashboard.png")
        newWindow.i = i
        cas.create_image((0,0), image=i, anchor='nw')
        cas.pack(side = BOTTOM, pady = 20, padx = 20)
    
    menubar = Menu(newWindow)
  
    about = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='About', menu = about)
    about.add_command(label ='Porfolio', command = p)
    about.add_command(label ='Contact', command = c)
    about.add_separator()
    about.add_command(label ='Exit', command = newWindow.destroy)
      
    user = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='User', menu = user)
    user.add_command(label = ("Welcome " + ab), command = da)
    user.add_command(label ='Sign out', command = Sig)
      
    proj = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Administor Lab', menu = proj)

    proj.add_cascade(label ='Select Lab', command = A)
    proj.add_cascade(label ='Create Lab', command = None)
    
    proj.add_cascade(label ='Add PC', command = None)
    proj.add_cascade(label ='Add PC Accessory', command = None)
    proj.add_cascade(label ='Modify PC', command = None)
    
    proj.add_cascade(label ='Add Teacher', command = None)
    proj.add_cascade(label ='Remove Teacher', command = None)
    proj.add_cascade(label ='Warnings', command = None)
    
    proj.add_separator()
    proj.add_cascade(label ='Lab Summary', command = None)
      
    newWindow.config(menu = menubar)

    global cas
    global l
    
    cas = tk.Canvas(newWindow,width=298,height=168, bg = "cyan", highlightthickness=3, highlightbackground="black")
    da()
    
def Sig():
    newWindow.destroy()

#Root Widgets
menubar = Menu(root)
  
about = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='About Coder', menu = about)
about.add_command(label ='Porfolio', command = p)
about.add_command(label ='Contact', command = c)
about.add_separator()
about.add_command(label ='Exit', command = root.destroy)
  
user = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='User', menu = user)
user.add_command(label ='Login', command = Log)
user.add_command(label ='Register', command = Reg)
user.add_command(label ='Forgot Password', command = For)

proj = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Features', menu = proj)

'''cals = Menu(proj, tearoff=0)
cals.add_command(label='Maths', command = None)
cals.add_command(label='BMI', command = None)
cals.add_command(label='Profit Loss', command = None)
cals.add_command(label='Tally Marks', command = None)
cals.add_command(label='Tendencies', command = None)
cals.add_command(label='Factorial', command = None)
cals.add_command(label='Interest', command = None)

covs = Menu(proj, tearoff=0)
covs.add_command(label='Number system', command = None)
covs.add_command(label='Value Changer', command = None)
covs.add_command(label='Number to Number Name', command = None)

oths = Menu(proj, tearoff=0)
oths.add_command(label='Eng to Fre Translator', command = None)
oths.add_command(label='Geometry', command = None)
oths.add_command(label='Number Guessing Game', command = None)

proj.add_cascade(label ='Calculators', menu=cals, command = None)
proj.add_cascade(label ='Convertors', menu=covs, command = None)
proj.add_separator()
proj.add_cascade(label ='Misc.', menu=oths, command = None)'''
  
root.config(menu = menubar)
pro = Label(root, textvariable = project, fg = "blue2",  bg = "cyan", font = ("Comic Sans MS", 20, "bold"))
pro.place(x = 27, y = 28, anchor = W)
canvas = tk.Canvas(root,width=298,height=166, bg = "cyan", highlightthickness=3, highlightbackground="black")

global can
can = tk.Canvas(root,width=350,height=270, bg = "cyan", highlightbackground="white")

two = tk.PhotoImage(file=r'D:\Mayank\Tinkering\Coding\Python\Lab Management\Lab.png')
root.two = two
can.create_image((0,0), image=two, anchor='nw')
can.pack(side = BOTTOM, pady = 0, padx = 0)

root.mainloop()
