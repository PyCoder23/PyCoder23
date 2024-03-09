# It might be possible that you encounter error(s) while running this because of mysql/xampp or library(s) not installed.
# But this will surely help you in your programs. All the BEST!
# Make Sure to Create database and input your credentials in quotes in line 19, 20, 21

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from PIL import Image, ImageTk
from num2words import num2words
import time
import random
import math
x = 0
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="USERNAME",
    password="PASSWORD",
    database="DATABASE_NAME",
    charset="utf8"
    )
mycursor = mydb.cursor() 

root = tk.Tk()
root.title("Mayank's Webpage")
root.geometry("350x270")
root.config(bg = "blue")
root.iconphoto(False, tk.PhotoImage(file="globe.png"))
root.resizable(False, False)

project = tk.StringVar()
pr = tk.StringVar()

name =tk.StringVar()
email =tk.StringVar()
pas =tk.StringVar()
repas =tk.StringVar()
coun =tk.StringVar()
state =tk.StringVar()
city =tk.StringVar()

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
    newWindow.iconphoto(False, tk.PhotoImage(file="globe.png"))
    newWindow.resizable(False, False)

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
        
    CAP = temp_pass
    #CAP = ""  # For easy and fast testing and debugging 

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
        mycursor.reset()
        mycursor.execute(query, (Email,Pass))
        result=mycursor.fetchone()
        
        query = """SELECT NAME FROM credentials where EMAIL = %s and PASSWORD = %s"""
        mycursor.reset()
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
    bgC = 'black'
    fgC = 'white'
    newWindow = Toplevel(root)
    newWindow.title("Login")
    newWindow.geometry("350x250")
    newWindow.config(bg = bgC)
    newWindow.iconphoto(False, tk.PhotoImage(file="globe.png"))
    newWindow.resizable(False, False)
    
    captcha()
    button = Button(newWindow, text = "Move to Login", fg = "white", bg = "blue", font = ("Comic Sans MS", 13, "bold"), command = m)

    lab_em = Label(newWindow, text = "Email", bg = bgC, fg = fgC, font = ("Comic Sans MS", 13, "bold"))
    lab_em.place(x = 20, y = 60, anchor = W)
    ent_em = Entry(newWindow, textvariable = email, width = 25, font = ("Comic Sans MS", 10, "bold"))
    ent_em.place(x = 125, y = 60, anchor = W)

    lab_pa = Label(newWindow, text = "Password", bg = bgC, fg = fgC, font = ("Comic Sans MS", 13, "bold"))
    lab_pa.place(x = 20, y = 100, anchor = W)
    ent_pa = Entry(newWindow, textvariable = pas, width = 25, font = ("Comic Sans MS", 10, "bold"), show = "*")
    ent_pa.place(x = 125, y = 100, anchor = W)

    lab_ca = Label(newWindow, text = "Captcha", bg = bgC, fg = fgC, font = ("Comic Sans MS", 13, "bold"))
    lab_ca.place(x = 20, y = 140, anchor = W)
    cap_ca = Label(newWindow, text = CAP, bg = bgC, font = ("Comic Sans MS", 13, "bold"))
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
    newWindow.iconphoto(False, tk.PhotoImage(file="globe.png"))
    newWindow.resizable(False, False)

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

#Image commands
def a():
    global canvas
    pro.config(fg = "white")
    project.set("My Portfolio")
    one = tk.PhotoImage(file=r"Portfolio.png")
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()
    
def b():
    global canvas
    pro.config(fg = "white")
    project.set("Contact Me")
    one = tk.PhotoImage(file=r'Contact.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def aa():
    global canvas
    pro.config(fg = "white")
    project.set("Calculator")
    one = tk.PhotoImage(file=r"Calculator.png")
    root.one = one
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    root.geometry("350x528")
    canvas.config(height = 444)
    global can
    can.pack_forget()

def ab():
    global canvas
    pro.config(fg = "white")
    project.set("BMI Calculator")
    one = tk.PhotoImage(file=r'BMI.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def ac():
    global canvas
    pro.config(fg = "white")
    project.set("Profit Loss")
    one = tk.PhotoImage(file=r"Profit Loss.png")
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def ad():
    global canvas
    pro.config(fg = "white")
    project.set("Tally Marks")
    one = tk.PhotoImage(file=r"Tally.png")
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()
    
def ae():
    global canvas
    pro.config(fg = "white")
    project.set("Number Tendencies")
    one = tk.PhotoImage(file=r'Number tendencies.png')
    root.one = one 
    canvas.config(height = 281)
    root.geometry("350x365")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()
    
def af():
    global canvas
    pro.config(fg = "white")
    project.set("Factorial Calculator")
    one = tk.PhotoImage(file=r"Factorial.png")
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def ag():
    global canvas
    pro.config(fg = "white")
    project.set("Interest Calculator")
    one = tk.PhotoImage(file=r'Interest.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()
    
def ba():
    global canvas
    pro.config(fg = "white")
    project.set("Number system")
    one = tk.PhotoImage(file=r'Number system.png')
    root.one = one 
    canvas.config(height = 270)
    root.geometry("350x354")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def bc():
    global canvas
    pro.config(fg = "white")
    project.set("Value Changer")
    one = tk.PhotoImage(file=r'Value changer.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def bd():
    global canvas
    pro.config(fg = "white")
    project.set("Number to Name")
    one = tk.PhotoImage(file=r'Number name.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()
    
def ca():
    global canvas
    pro.config(fg = "black")
    project.set("Question Game")
    one = tk.PhotoImage(file=r'Question.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def db():
    pro.config(fg = "white")    
    project.set("Eng to French")
    one = tk.PhotoImage(file=r"Eng to French.png")
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def dc():
    global canvas
    pro.config(fg = "white")
    project.set("Geometry Assist")
    one = tk.PhotoImage(file=r'Geometry.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def dd():
    global canvas
    pro.config(fg = "white")
    project.set("Guess the number")
    one = tk.PhotoImage(file=r'Number guessing game.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()
    
#Dashboard
def A():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Calculator")
    win.geometry("300x420")
    win.config(bg = "cyan")
    win.resizable(False, False)

    ops = ["a", "b", "c", "d", "e", "f", "eq", "CE", "C", "bk", "sq", "rt", "cu", "curt", "rec"]
    global num1
    num1 = 0
    global num2
    num2 = 0
    global Ans
    Ans = 0
    global op
    op = ""
    global A
    A = 0

    def callback(ans):
        char= ans.get()
        try :
            char = float(char)
        except ValueError:
            ans.set(ans.get()[0:-1])

    def enter(args):
        global op
        global num1
        global num2
        if args in ops:
            if args == "eq" and float(num1) != 0:
                equal(args)
                print("")
                
            elif args == "a" or args == "b" or args == "c" or args == "d" or args == "sq" or args == "rt" or args == "per" or args == "cu" or args == "curt" or args == "rec" :
                oper(args)
                
            elif args == "C":
                op = ""
                num1 = 0
                num2 = 0
                ans.set("")
                print("")
                
            elif args == "CE":
                ans.set("")

            elif args == "bk":
                ans.set(ans.get()[0:-1])

            elif args == "e":
                a = ans.get()
                a = float(a)
                if (a % 1) == 0:
                    a = int(a)
                    ans.set(str(a)+".")
                else:
                    ans.set(float(ans.get()))

            elif args == "f":
                val = float(ans.get())
                val = 0 - float(val)
                if val % 1 == 0:
                    val = int(val)
                else:
                    val = float(val)
                ans.set(val)
                
        else:
            char = ""
            char = ans.get()
            char += str(args)
            ans.set(char)

    def equal(args):
        global op
        global num1
        global num2
        num2 = ans.get()
        print(num2)
        ans.set("")
        print(str(num1)+op+str(num2))
        oper(args)
        global Ans
        Ans = round(Ans, 3)
        if Ans % 1 == 0:
            Ans = int(Ans)
        else:
            Ans = float(Ans)
        a = str(Ans)
        if len(a) > 12:
            charlen = len(a)
            charlen
            b = 1
            for i in range(1, charlen+1):
                b *= 10
            a = int(Ans)
            a = a / b
            a = round(a, 6)
            sc = str(a) + " * 10 ^ "+str(i)
        ans.set(Ans)
        op = ""
        num1 = 0
        num2 = 0
        Ans = 0

    def Eq():
        global Ans
        global op
        global num1
        global num2
        Ans = round(Ans, 3)
        if Ans % 1 == 0:
            Ans = int(Ans)
        else:
            Ans = float(Ans)
        ans.set(Ans)
        print("")
        op = ""
        num1 = 0
        num2 = 0
        Ans = 0
        
    def oper(args):
        global num1
        global op
        global Ans
        if args == "a" or op == "+":
            op = "+"
            if args == "eq":
                Ans = float(num1) + float(num2)
                print(Ans)
            
        elif args == "b" or op == "-":
            op = "-"
            if args == "eq":
                Ans = float(num1) - float(num2)
                print(Ans)
            
        elif args == "c" or op == "x":
            op = "x"
            if args == "eq":
                Ans = float(num1) * float(num2)
                print(Ans)

        elif args == "d" or op == "/":
            op = "/"
            if args == "eq":
                Ans = float(num1) / float(num2)
                print(Ans)

        num1 = ans.get()
        print(num1)
        ans.set("")
        
        if args == "sq" or op == "sq":
            op = "sq"
            Ans = float(num1) * float(num1)
            print(Ans)
            Eq()
        elif args == "rt" or op == "rt":
            import math
            op = "rt"
            Ans = math.sqrt(float(num1))
            print(Ans)
            Eq()

        elif args == "cu" or op == "cu":
            op = "cu"
            Ans = float(num1) * float(num1) * float(num1)
            print(Ans)
            Eq()

        elif args == "curt" or op == "curt":
            op = "curt"
            Ans = num1
            Ans = np.cbrt(Ans)
            print(Ans)
            Eq()

        elif args == "rec" or op == "rec":
            op = "rec"
            Ans = 1/float(num1)
            print(Ans)
            Eq()            

    def Next(event):
        global A
        print("hi")
        if A % 2 == 0:
            win.geometry("360x420")
            entry.place(x=180, y=50, anchor = CENTER)
            entry.config(width = 15)
            sq.place(x=300, y=120, anchor = CENTER)
            win.place(x=300, y=180, anchor = CENTER)
            Cu.place(x=300, y=240, anchor = CENTER)
            curt.place(x=300, y=300, anchor = CENTER)
            rec.place(x=300, y=360, anchor = CENTER)
            
        elif A % 2 == 1:
            win.geometry("300x420")
            entry.place(x=150, y=50, anchor = CENTER)
            entry.config(width = 12)
            sq.place_forget()
            win.place_forget()
            Cu.place_forget()
            curt.place_forget()
            rec.place_forget()
            
        A += 1 
        
    ans = StringVar()
    ans.trace("w", lambda name, index,mode, ans=ans: callback(ans))

    entry=Entry(win, textvariable = ans, width = 12, font = ("Xenara", 28, "bold"), justify = "right")
    entry.place(x=150, y=50, anchor = CENTER)

    clent = Button(win, text = " CE ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("CE"))
    clent.place(x=60, y=120, anchor = CENTER)

    clear = Button(win, text = " C ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("C"))
    clear.place(x=120, y=120, anchor = CENTER)

    bksp = Button(win, text = " ⌫ ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("bk"))
    bksp.place(x=180, y=120, anchor = CENTER)

    add = Button(win, text = " + ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("a"))
    add.place(x=240, y=120, anchor = CENTER)

    but_one = Button(win, text = " 1 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(1))
    but_one.place(x=60, y=180, anchor = CENTER)

    but_two = Button(win, text = " 2 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(2))
    but_two.place(x=120, y=180, anchor = CENTER)

    but_three = Button(win, text = " 3 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(3))
    but_three.place(x=180, y=180, anchor = CENTER)

    sub = Button(win, text = " - ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("b"))
    sub.place(x=240, y=180, anchor = CENTER)

    but_four = Button(win, text = " 4 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(4))
    but_four.place(x=60, y=240, anchor = CENTER)

    but_five = Button(win, text = " 5 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(5))
    but_five.place(x=120, y=240, anchor = CENTER)

    but_six = Button(win, text = " 6 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(6))
    but_six.place(x=180, y=240, anchor = CENTER)

    mul = Button(win, text = " x ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("c"))
    mul.place(x=240, y=240, anchor = CENTER)

    but_seven = Button(win, text = " 7 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(7))
    but_seven.place(x=60, y=300, anchor = CENTER)

    but_eight = Button(win, text = " 8 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(8))
    but_eight.place(x=120, y=300, anchor = CENTER)

    but_nine = Button(win, text = " 9 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(9))
    but_nine.place(x=180, y=300, anchor = CENTER)

    div = Button(win, text = " / ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("d"))
    div.place(x=240, y=300, anchor = CENTER)

    sign = Button(win, text = "+/-", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("f"))
    sign.place(x=60, y=360, anchor = CENTER)

    but_zero = Button(win, text = " 0 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(0))
    but_zero.place(x=120, y=360, anchor = CENTER)

    point = Button(win, text = ".", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("e"))
    point.place(x=180, y=360, anchor = CENTER)

    eq = Button(win, text = " = ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("eq"))
    eq.place(x=240, y=360, anchor = CENTER)

    sq = Button(win, text = " sq ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("sq"))
    win = Button(win, text = " √ ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("rt"))
    Cu = Button(win, text = " cu ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("cu"))
    curt = Button(win, text = " ∛ ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("curt"))
    rec = Button(win, text = " 1/x ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("rec"))

    more = Label(win, text = " → ", fg = "white", bg = "white", font = ("Comic Sans MS", 22, "bold"))
    more.place(x=54, y=50, anchor = CENTER)
    more.bind("<Button-1>", Next)

def B():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("BMI Calculator")
    win.geometry("400x230")
    win.config(bg = "cyan")
    win.resizable(False, False)

    wei = tk.StringVar()
    hei = tk.StringVar()
    ans = tk.StringVar()

    def Submit():
        ans.set("")
        A = wei.get()
        B = hei.get()
        try:
            A = float(A)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter numericals only")
        else:
            try:
                B = float(B)
            except ValueError:
                messagebox.showerror("Invalid Input", "Enter numericals only")
            else:
                print(A)
                print(B)
                BMI = A/(B*B)
                BMI = round(BMI, 2)
                print(BMI)
                print("")
                ans.set(BMI)
            
    Title = Label(win, text = "BMI Calculator", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 19, "bold"))
    Title.place(x = 200, y = 25, anchor = CENTER)

    placeholder_A = "Enter your weight (kg)"
    entry_1 = Entry(win, width = 20, textvariable = wei, font = ("Comic Sans MS", 11, "bold"))
    entry_1.place(x = 200, y = 70, anchor = CENTER)
    def erase_A(event=None):
        if entry_1.get() == placeholder_A:
            entry_1.delete(0,'end')
            
    def add_A(event=None):
        if entry_1.get() == '':
            entry_1.insert(0,placeholder_A)

    add_A()
    entry_1.bind('<FocusIn>',erase_A)
    entry_1.bind('<FocusOut>',add_A)

    placeholder_B = "Enter your height (m)"
    entry_2 = Entry(win, width = 20, textvariable = hei, font = ("Comic Sans MS", 11, "bold"))
    entry_2.place(x = 200, y = 110, anchor = CENTER)
    def erase_B(event=None):
        if entry_2.get() == placeholder_B:
            entry_2.delete(0,'end')
            
    def add_B(event=None):
        if entry_2.get() == '':
            entry_2.insert(0,placeholder_B)

    add_B()
    entry_2.bind('<FocusIn>',erase_B)
    entry_2.bind('<FocusOut>',add_B)

    submit = Button(win, text = "Calculate", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = Submit)
    submit.place(x = 200, y = 160, anchor = CENTER)

    out = Label(win, textvariable = ans, bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
    out.place(x = 200, y = 205, anchor = CENTER)

def C():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Profit Loss Calculator")
    win.geometry("400x170")
    win.config(bg = "cyan")
    win.resizable(False, False)

    wei = tk.StringVar()
    hei = tk.StringVar()
    ans = tk.StringVar()
    num = tk.StringVar()
    ans=tk.StringVar()
    n = tk.StringVar()
    a = tk.StringVar()
    b = tk.StringVar()
    op = ""

    def Submit(op):
        if op == "":
            messagebox.showerror("No Input", "Choose operation please")
        else:
            ans.set("")
            A = a.get()
            B = b.get()
            try:
                A = int(A)
                B = int(B)
            except ValueError:
                messagebox.showerror("Invalid Input", "Enter integars only")
            else:
                print(A)
                print(B)
                ans.set(A)
                ent1.place_forget()
                ent2.place_forget() 
                submit.place_forget()
                Ty.place_forget()
                lab.place_forget()
                if op == 'Cost Price' or op == 'Selling Price':
                    Price(op, A, B)
                elif op == 'Profit or Loss' or op == 'Profit or Loss %':
                    Pro(op, A, B)

    def fin(out, A, B):
        global M
        global N
        
        x.config(text = str(M) + " was " + str(A))
        x.place(x = 110, y = 70, anchor = W)

        y.config(text = str(N) + " was " + str(B))
        y.place(x = 110, y = 115, anchor = W)
        
        z.config(text = out)
        z.place(x = 110, y = 160, anchor = W)
        
    def Price(op, A, B):
        if op == 'Cost Price':
            cp = A - B
            cp = round(cp, 3)
            print("Cost Price = "+str(cp))
            out = "Cost Price = "+str(cp)
            
        elif op == 'Selling Price':
            sp = A + B
            sp = round(sp, 3)
            print("Selling Price = "+str(sp))
            out = "Selling Price = "+str(sp)
        fin(out, A, B)
        
    def Pro(op, A, B):
        if op == 'Profit or Loss':
            pro = B - A
            pro = round(pro, 3)
            print("Profit = "+str(pro))
            out = "Profit = "+str(pro)
            
        elif op == 'Profit or Loss %':
            per = B - A
            per = (per/A) * 100
            per = round(per, 3)
            print("Profit = " + str(per) + "%")
            out = "Profit = " + str(per) + "%"
        fin(out, A, B)
            
    def sel(event):
        op = event.widget.get()
        print(op)
        submit.config(command = lambda : Submit(op))
        lab.place_forget()

        win.geometry("400x200")
        global M
        global N
        global placeholder1
        global placeholder2
        if op == 'Cost Price':
            placeholder1 = 'Enter S.P.'
            placeholder2 = 'Enter Profit or Loss'
            win.geometry("400x220")
            lab.config(text = "Express Gain in +ve and Loss in -ve")
            lab.place(x = 200, y = 195, anchor = CENTER)
            M = "Selling Price"
            N = "Profit/Loss"
            
        elif op == 'Selling Price':
            placeholder1 = 'Enter C.P.'
            win.geometry("400x220")
            placeholder2 = 'Enter Profit or Loss'
            lab.config(text = "Express Gain in +ve and Loss in -ve")
            lab.place(x = 200, y = 195, anchor = CENTER)
            M = "Cost Price"
            N = "Profit/Loss"
            
        elif op == 'Profit or Loss':
            placeholder1 = 'Enter C.P.'
            placeholder2 = 'Enter S.P.'
            M = "Cost Price"
            N = "Selling Price"

        elif op == 'Profit or Loss %':
            placeholder1 = 'Enter C.P.'
            placeholder2 = 'Enter S.P.'
            M = "Cost Price"
            N = "Selling Price"

        ent1.delete(0,'end')
        ent1.insert(0,placeholder1)

        ent2.delete(0,'end')
        ent2.insert(0,placeholder2)
        
        ent1.place(x = 150, y = 115, anchor = CENTER)
        ent2.place(x = 150, y = 155, anchor = CENTER) 
        submit.place(x = 270, y = 135, anchor = CENTER)
        
    Title = Label(win, text = "Profit Loss Calculator", fg = "blue2", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    Title.place(x = 200, y = 25, anchor = CENTER)

    Ty = ttk.Combobox(win, width = 20, textvariable = n)
    Ty['values'] = ('Cost Price', 
                    'Selling Price',
                    'Profit or Loss', 
                    'Profit or Loss %',)

    Ty.place(x = 200, y = 70, anchor = CENTER)
    Ty.current()
    Ty.set("Select Operation")
    Ty.bind("<<ComboboxSelected>>", sel)

    ent1 = Entry(win, width = 20, textvariable = a, fg = "black")
    ent2 = Entry(win, width = 20, textvariable = b, fg = "black")

    lab = Label(win, text = "", fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))

    global placeholder1
    global placeholder2
    placeholder1 = 'Please enter side'
    def erase_a(event=None):
        if ent1.get() == placeholder1:
            ent1.delete(0,'end')
    def add_a(event=None):
        if ent1.get() == '':
            ent1.insert(0,placeholder1)
    add_a()
    ent1.bind('<FocusIn>',erase_a)
    ent1.bind('<FocusOut>',add_a)

    placeholder2 = 'Please enter 2nd side'
    def erase_b(event=None):
        if ent2.get() == placeholder2:
            ent2.delete(0,'end')
    def add_b(event=None):
        if ent2.get() == '':
            ent2.insert(0,placeholder2)
    add_b()
    ent2.bind('<FocusIn>',erase_b)
    ent2.bind('<FocusOut>',add_b)

    x = Label(win, text = "", fg = "black", bg = "cyan", font = ("Comic Sans MS", 14, "bold"))
    y = Label(win, text = "", fg = "black", bg = "cyan", font = ("Comic Sans MS", 14, "bold"))
    z = Label(win, text = "", fg = "black", bg = "cyan", font = ("Comic Sans MS", 14, "bold"))

    submit = Button(win, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = lambda : Submit(op))
    submit.place(x = 200, y = 120, anchor = CENTER)

    out = Label(win, textvariable = ans, bg = "cyan", font = ("Comic Sans MS", 12, "bold"))    
    
def D():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Tally Marks Calculator")
    global width
    global height
    global dim
    width,height=400,200
    dim = str(width)+'x'+str(height)
    win.geometry(dim)
    win.config(bg = "cyan")
    win.resizable(False, False)

    a = tk.StringVar()
    b = tk.StringVar()
    global stat
    stat = 0
    global x
    x = 1

    dic = {}
    tal = {}

    def Submit():
        global stat
        topic = a.get()
        a.set("")
        if topic == "":
            messagebox.showinfo("No Input!", "Enter the topic!")
        elif topic != "" :   
            submit.place_forget()
            stat = 1
            label_1.config(text = "Enter number of observations")
            entry_1.place_forget()
            entry_2.place(x= 150, y= 120,anchor = CENTER)
            submit.place(x= 250, y= 120,anchor = CENTER)
            submit.config(command = lambda : get_num(topic))

    def get_num(topic):
        global stat
        obs = b.get()
        b.set("")
        try:
            obs = int(obs)
        except ValueError:
            messagebox.showinfo("Invalid Input!", "Enter numerical value only for number of observations!")
        else:
            submit.place_forget()
            print(topic)
            print(obs)
            global x
            Prog(obs, topic, x)

    def Prog(obs, topic, x):
        b.set("")
        global height
        global dim
        global width
        height = 300
        dim = str(width)+'x'+str(height)
        win.geometry(dim)
        if x <= obs:
            num = num2words(x, to = 'ordinal_num')
            label_2.config(text = "Enter "+num+" observation")
            entry_1.config(width = 25)
            entry_1.place(x = 200, y = 110,anchor = CENTER)
            entry_2.config(width = 25)
            entry_2.place(x = 200, y = 200,anchor = CENTER)
            label_1.config(text = "Enter "+topic)
            label_2.place(x = 200, y = 155,anchor = CENTER)
            submit.config(command = lambda : ob_get(x, obs, topic))
            submit.place(x= 200,y= 250, anchor = CENTER)
        else:
            pro(obs, topic)

    def ob_get(x, obs, topic):
        if x <= obs:
            subject = a.get()
            observation = b.get()
            a.set("")
            b.set("")
            try:
                observation = int(observation)
            except ValueError:
                messagebox.showinfo("Invalid Input!", "Enter numerical value only in observation!")
            else:
                x += 1
                dic[subject]=observation
                Prog(obs, topic, x)

    def pro(obs, topic):
        print("")
        print(dic)
        label_1.place_forget()
        entry_1.place_forget()
        label_2.place_forget()
        entry_2.place_forget()
        submit.place_forget()
        tally = ""
        for i in dic.keys():
            print("")
            print(i)
            j = dic[i]
            print(j)
            j - int(j)
            tally = ""
            while j > 0:
                if j % 5 == 0:
                    x = j / 5
                    x = int(x)
                    for y in range(1, x+1):
                        tally = tally + '-||||'
                        j -= 5
                else:
                    x = j % 5
                    x = int(x)
                    for y in range(1, x+1):
                        tally = tally + "|"
                        j -= 1

            tally_m = tally[::-1]
            print(tally_m)
            tal[i] = tally_m
        disp(obs, topic)

    def disp(obs, topic):
        global height
        global dim
        global width
        label_1.config(text = "Tally Marks Table")
        label_1.place(x= 200, y= 70, anchor = CENTER)
        subject = Label(win, text = topic, fg = "red", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
        tally_label = Label(win, text = "Tally Marks", fg = "red", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
        subject.place(x= 120,y= 110,anchor = "e")
        tally_label.place(x= 275,y= 110,anchor = "e")
        Max = 0
        for z in dic.values():
            if z > Max:
                Max = z 
        if Max > 12 :
            t = Max - 17
            t *= 15
            t = round(t, 0)
            t = int(t)
            width = 400 + t
            dim = str(width)+'x'+str(height)
            win.geometry(dim)
            Title.place(x= round(width/2, 0), y= 25, anchor = CENTER)
            label_1.place(x= round(width/2, 0), y= 70, anchor = CENTER)
            tally_label.place(x= round(width/2.85, 0), y= 110, anchor = W)
            subject.place(x= round(width/7.2, 0), y= 110, anchor = W)
            
        if obs > 4 :
            t = obs - 4
            height = 300 + (t*30)
            dim = str(width)+'x'+str(height)
            win.geometry(dim)
            
        y_var = 160
        for i in tal.keys():
            sub = Label(win, text = i, fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
            tall = Label(win, text = tal[i], fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
            if Max > 12:
                sub.place(x= round(width/7.2, 0),y= y_var,anchor = W)
                tall.place(x= round(width/2.85, 0),y= y_var,anchor = W)
            else :
                sub.place(x= 120,y= y_var,anchor = "e")
                tall.place(x= 275,y= y_var,anchor = "e")
            y_var += 30

    Title = Label(win, text = "Tally Marks Calculator", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 19, "bold"))
    label_1 = Label(win, text = "Enter topic", fg = "blue2", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    label_2 = Label(win, text = "Enter topic", fg = "blue2", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    entry_1 = Entry(win, width= 15, textvariable = a)
    entry_2 = Entry(win, width= 15, textvariable = b)
    submit = Button(win, text = "Submit", fg = "white", bg = "black", font = ("Comic Sans MS", 12, "bold"), command = Submit)

    Title.place(x= 200, y= 25,anchor = CENTER)
    entry_1.place(x= 150, y= 120,anchor = CENTER)
    submit.place(x= 250, y= 120,anchor = CENTER)
    label_1.place(x= 200, y= 70, anchor = CENTER)
    
def E():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Data Handling")
    global width
    global height
    global dim
    width,height=400,200
    dim = str(width)+'x'+str(height)
    win.geometry(dim)
    win.config(bg = "cyan")
    win.resizable(False, False)
    a= tk.StringVar()
    List = []
    Dic = {}
    num = []
    freq_lis = []
    global x
    x = 1

    def Submit():
        global stat
        obs = a.get()
        a.set("")
        if obs == "":
            messagebox.showinfo("No Input!", "Enter the topic!")
        elif obs != "" :   
            try:
                obs = int(obs)
            except ValueError:
                messagebox.showinfo("Invalid Input!", "Enter numerical value only for number of observations!")
            else:
                print(str(obs)+"\n")
                global x
                Prog(obs, x)

    def Prog(obs, x):
        if x <= obs:
            if x == 1:
                pos = "st"
                
            elif x == 2:
                pos = "nd"
                
            elif x == 3:
                pos = "rd"

            elif x >= 4:
                pos = "th"

            label_1.config(text = "Enter "+str(x)+pos+" observation")
            submit.config(command = lambda : ob_get(x, obs))
        else:
            pro(obs)

    def ob_get(x, obs):
        if x <= obs:
            observation = a.get()
            a.set("")
            try:
                observation = int(observation)
            except ValueError:
                messagebox.showinfo("Invalid Input!", "Enter numerical value only in observation!")
            else:
                print(observation)
                x += 1
                if observation in num:
                    y = num.index(observation)
                    z = freq_lis[y]
                    freq_lis[y] = z + 1
                else:
                    freq_lis.append(1)
                    num.append(observation)
                List.append(observation)
                Prog(obs, x)

    def pro(obs):
        #Screen change
        entry_1.place_forget()
        submit.place_forget()
        label_1.config(text = "The central tendencies")
        List.sort()

        #Assigning vars
        mean = 0
        median = 0
        mode = 0
        Range = 0
        high = 0 
        low = 0
        Sum = 0

        # Resizing window
        global width
        global height
        global dim
        width,height=400,350
        dim = str(width)+'x'+str(height)
        win.geometry(dim)

        # Mean
        for i in List:
            Sum += i
            
        mean = Sum/obs

        # Median
        if obs % 2 == 0:
            A = obs/2
            B = (obs/2)+1
            A = int(A)
            A -= 1
            B = int(B)
            B -= 1
            median = (List[A]+List[B])/2
        elif obs % 2 == 1:
            A = (obs+1)/2
            A = int(A)
            A -= 1
            median = List[A]

        # Range, Highest, Lowest
        for h in List:
            if h > high :
                high = h
                
        low = high
        for j in List:
            if j < low :
                low = j

        Range = high - low

        # Mode, Most and least frequency
        Hi = 0
        Lo = obs
        for j in freq_lis:
            if j > Hi:
                Hi = j
            if j < Lo:
                Lo = j

        Modes = ""
        print("")
        while Hi in freq_lis:
            pos_mode = freq_lis.index(Hi)
            freq_lis.remove(Hi)
            Mode = num[pos_mode]
            num.remove(Mode)
            if Modes == "":
                count_mode = 1
                Modes = Modes + str(Mode)
            else:
                count_mode += 1
                Modes = Modes + ", " + str(Mode)

        # Output
        print("Mean = "+str(mean))
        print("Median = "+str(median))
        print("Mode = "+str(Modes))
        print("Highest observation = "+str(high))
        print("Lowest observation = "+str(low))
        print("Range = "+str(Range))
        print("Highest frequency = "+str(Hi))
        print("Lowest frequency = "+str(Lo))
        
        label_a = Label(win, text = "Mean = "+str(mean), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_a.place(x= 200, y= 110, anchor = CENTER)
        
        label_b = Label(win, text = "Median = "+str(median), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_b.place(x= 200, y= 140, anchor = CENTER)

        label_c = Label(win, text = "Mode(s) = "+str(Modes), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_c.place(x= 200, y= 170, anchor = CENTER)

        label_d = Label(win, text = "Range = "+str(Range), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_d.place(x= 200, y= 200, anchor = CENTER)

        label_e = Label(win, text = "Highest observation = "+str(high), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_e.place(x= 200, y= 230, anchor = CENTER)

        label_f = Label(win, text = "Lowest observation = "+str(low), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_f.place(x= 200, y= 260, anchor = CENTER)

        label_g = Label(win, text = "Highest frequency = "+str(Hi), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_g.place(x= 200, y= 290, anchor = CENTER)

        label_h = Label(win, text = "Lowest frequency = "+str(Lo), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_h.place(x= 200, y= 320, anchor = CENTER)

    Title = Label(win, text = "Number tendencies", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 19, "bold"))
    label_1 = Label(win, text = "Enter number of observations", fg = "blue2", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    entry_1 = Entry(win, width= 15, textvariable = a)
    submit = Button(win, text = "Submit", fg = "white", bg = "black", font = ("Comic Sans MS", 12, "bold"), command = Submit)

    Title.place(x= 200, y= 25,anchor = CENTER)
    entry_1.place(x= 150, y= 120,anchor = CENTER)
    submit.place(x= 250, y= 120,anchor = CENTER)
    label_1.place(x= 200, y= 70, anchor = CENTER)

def F():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Factorial")
    win.geometry("400x200")
    win.config(bg = "cyan")
    win.resizable(False, False)

    num = tk.StringVar()
    ans=tk.StringVar()

    def Submit():
        Pro = 1
        ans.set("")
        A = num.get()
        try:
            A = int(A)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter integars only")
        else:
            print(A)
            for i in range(1, A+1):
                Pro = Pro * i
            ans.set("Factorial of " + str(A) + " is " + str(Pro))
            
    Title = Label(win, text = "Factorial", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    Title.place(x = 200, y = 25, anchor = CENTER)

    label_1 = Label(win, text = "Enter Number", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    label_1.place(x = 200, y = 70, anchor = CENTER)

    entry = Entry(win, width = 20, textvariable = num, fg = "blue3")
    entry.place(x = 140, y = 115, anchor = CENTER)

    submit = Button(win, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = Submit)
    submit.place(x = 260, y = 115, anchor = CENTER)

    out = Label(win, textvariable = ans, bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
    out.place(x = 200, y = 160, anchor = CENTER)

def G():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Interest Calculator")
    win.geometry("400x200")
    win.config(bg = "cyan")
    win.resizable(False, False)

    n = tk.StringVar()
    Cur = tk.StringVar()
    Pa = tk.StringVar()
    Ri = tk.StringVar()
    Ti = tk.StringVar()
    Cr = tk.StringVar()
    ANS = tk.StringVar()
    ans = tk.StringVar()

    def sel(event):
        global ty
        ty = event.widget.get()
        
    def Submit(ty):
        cur = Cur.get()
        if cur == "Please enter Currency":
            messagebox.showerror("No currency entered", "Please enter transaction currency")
        else:
            print("\nCurrency is " + str(cur))
            print(ty)
            Title.config(text = ty + " Calculator")
            Ty.place_forget()
            label_1.config(textvariable = ans)
            ans.set("Enter principal amount")
            submit.config(command = lambda : get_pa(ty, cur))
            entry.place_forget()
            entry_2.place(x = 140, y = 115, anchor = CENTER)
            entry_2.config(textvariable = Pa)
            submit.place(x = 260, y = 115, anchor = CENTER)

    def get_pa(ty, cur):
        P = Pa.get()
        try:
            P = float(P)
        except ValueError:
            messagebox.showerror("Invalid Input!", "Enter numerical value only")
        else:        
            ans.set("Enter Rate of Interest")
            submit.config(command = lambda : get_ri(ty, cur, P))
            entry_2.place(x = 140, y = 115, anchor = CENTER)
            entry_2.config(textvariable = Ri)
            submit.place(x = 260, y = 115, anchor = CENTER)

    def get_ri(ty, cur, P):
        R = Ri.get()
        try:
            R = float(R)
        except ValueError:
            messagebox.showerror("Invalid Input!", "Enter numerical value only")
        else:
            ans.set("Enter Time(in years)")
            submit.config(command = lambda : get_ti(ty, cur, P, R))
            entry_2.place(x = 140, y = 115, anchor = CENTER)
            entry_2.config(textvariable = Ti)
            submit.place(x = 260, y = 115, anchor = CENTER)

    def get_ti(ty, cur, P, R):
        T = Ti.get()
        try:
            T = float(T)
        except ValueError:
            messagebox.showerror("Invalid Input!", "Enter numerical value only")
        else:
            if ty == "Compound Interest":
                ans.set("Enter Compound Freq. per year")
                submit.config(command = lambda : get_cr(ty, cur, P, R, T))
                entry_2.place(x = 140, y = 115, anchor = CENTER)
                entry_2.config(textvariable = Cr)
                submit.place(x = 260, y = 115, anchor = CENTER)
            else:
                si(ty, cur, P, R, T)

    def get_cr(ty, cur, P, R, T):
        N = Cr.get()
        try:
            N = float(N)
        except ValueError:
            messagebox.showerror("Invalid Input!", "Enter numerical value only")
        else:
            ci(ty, cur, P, R, T, N)

    def si(ty, cur, P, R, T):
        submit.place_forget()
        entry.place_forget()
        entry_2.place_forget()
        label_1.config(textvariable = ans)
        label_1.config(font = ("Comic Sans MS", 12, "bold"))
        label_1.place(x = 200, y = 80, anchor = CENTER)
        label_2.place(x = 200, y = 110, anchor = CENTER)
        SI = (P * R * T)/100
        SI = round(SI, 2)
        ans.set("Simple Interest = "+cur+str(SI))
        ANS.set("Amount = "+cur+str(round(SI+P, 2)))
        ret.place(x = 200, y = 160, anchor = CENTER)

    def ci(ty, cur, P, R, T, N):
        submit.place_forget()
        entry.place_forget()
        entry_2.place_forget()
        label_1.config(textvariable = ans)
        label_1.config(font = ("Comic Sans MS", 12, "bold"))
        label_1.place(x = 200, y = 80, anchor = CENTER)
        label_2.place(x = 200, y = 110, anchor = CENTER)
        CI = P * ((1+(R)/(100*N))**(N*T))
        CI -= P
        CI = round(CI, 2)
        ans.set("Compound Interest = "+cur+str(CI))
        ANS.set("Amount = "+cur+str(round(CI+P, 2)))
        ret.place(x = 200, y = 160, anchor = CENTER)
        

    def again():
        n.set("")
        Cur.set("")
        Pa.set("")
        Ri.set("")
        Ti.set("")
        Cr.set("")
        ANS.set("")
        ans.set("")
        
        ret.place_forget()
        label_1.config(font = ("Comic Sans MS", 15, "bold"))
        label_2.place_forget()
        placeholder = 'Please enter Currency'

        entry.place(x = 140, y = 155, anchor = CENTER)

        def erase(event=None):
            if entry.get() == placeholder:
                entry.delete(0,'end')
        def add(event=None):
            if entry.get() == '':
                entry.insert(0,placeholder)

        add()
        entry.bind('<FocusIn>',erase)
        entry.bind('<FocusOut>',add)

        ans.set("Select Interest")
        label_1.place(x = 200, y = 70, anchor = CENTER)

        Ty.place(x = 200, y = 110, anchor = CENTER)

        submit.config(command = lambda : Submit(ty))
        submit.place(x = 260, y = 155, anchor = CENTER)

    Title = Label(win, text = "Interest Calculator", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    Title.place(x = 200, y = 30, anchor = CENTER)

    placeholder = 'Please enter Currency'

    entry = Entry(win, width = 20, textvariable = Cur)
    entry_2 = Entry(win, width = 20, text = "")
    entry.place(x = 140, y = 155, anchor = CENTER)

    def erase(event=None):
        if entry.get() == placeholder:
            entry.delete(0,'end')
    def add(event=None):
        if entry.get() == '':
            entry.insert(0,placeholder)

    add()
    entry.bind('<FocusIn>',erase)
    entry.bind('<FocusOut>',add)

    label_1 = Label(win, text = "Select Interest", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    label_1.place(x = 200, y = 70, anchor = CENTER)

    label_2 = Label(win, textvariable = ANS, fg = "blue", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))

    Ty = ttk.Combobox(win, width = 20, textvariable = n)
    Ty['values'] = ('Simple Interest', 
                    'Compound Interest')

    Ty.place(x = 200, y = 110, anchor = CENTER)
    Ty.current()
    Ty.bind("<<ComboboxSelected>>", sel)

    submit = Button(win, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = lambda : Submit(ty))
    submit.place(x = 260, y = 155, anchor = CENTER)

    ret = Button(win, text = "Use again", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = again)
    
def H():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Number system convertor")
    win.geometry("350x280")
    win.config(bg = "cyan")
    win.resizable(False, False)

    Bina = 0
    Deca = 0
    Octa = 0
    Hexa = ""

    global Dec
    global Bin
    global Oct
    global Hex

    Bin = ""
    Dec = ""
    Oct = ""
    Hex = ""

    put = ""


    a=tk.StringVar()
    global A
    put = ""
    A = ""

    def h():
        global x
        if x == 10:
            x = ""
            x = "A"

        if x == 11:
            x = ""
            x = "B"
            
        if x == 12:
            x = ""
            x = "C"
            
        if x == 13:
            x = ""
            x = "D"
            
        if x == 14:
            x = ""
            x = "E"
            
        if x == 15:
            x = ""
            x = "F"

    def get_data():
        global n
        n = 0
        Bin = ""
        Dec = ""
        Oct = ""
        Hex = ""

        global Deca
        global Bina
        global Octa
        global Hexa
        
        Bina = 0
        Deca = 0
        Octa = 0
        Hexa = 0
        
        A = a.get()
        A = str(A)
        print("")
        print(A)
        Check(A)

    def origin(event):
        global fro
        fro = event.widget.get()
        

    def desired(event):
        global to
        to = event.widget.get()

    def Check(A) :
        #Decimal to others
        print(fro)
        print(to)
        global y
        y = ""
        if fro == to :
            put = ""
            out.set(put)
            messagebox.showinfo("Invalid Conversion selected", "You have entered origin and destination number system the same!")
        else :
            if fro == "Decimal" or fro == "Binary" or fro == "Octal" :
                try:
                    A = int(A)
                except:
                    put = ""
                    out.set(put)
                    messagebox.showinfo("Invalid Input", "Enter Integars only for type conversion!")
                else:
                    A = str(A)
                    lim = 9
                    
                    #Decimal to others
                    if fro == "Decimal" and to == "Binary":
                        DB(A)
                        global Bin
                        put = "Equivalent " + to + " Value = " + "(" + Bin + ")" + "2"
                        out.set(put)
                        win.geometry("350x290")

                    elif fro == "Decimal" and to == "Octal" :                    
                        DO(A)
                        global Oct
                        put = "Equivalent " + to + " Value = " + "(" + Oct + ")" + "8"
                        out.set(put)
                        win.geometry("350x290")
                        
                    elif fro == "Decimal" and to == "Hexadecimal" :
                        DH(A)
                        global Hex
                        put = "Equivalent " + to + " Value = " + "(" + Hex + ")" + "16"
                        out.set(put)
                        win.geometry("350x290")
                
                    #Binary to others
                    elif fro == "Binary" and to == "Decimal" :
                        BD(A)
                        global Dec
                        global n
                        if n == 0:
                            put = "Equivalent " + to + " Value = " + "(" + Dec + ")" + "10"
                            out.set(put)
                            win.geometry("350x290")
                        else :
                            out.set("")
                        
                    elif fro == "Binary" and to == "Octal" :
                        BO(A)

                    elif fro == "Binary" and to == "Hexadecimal" :
                        BH(A)

                    #Octal to others
                    
                    elif fro == "Octal" and to == "Binary" :
                        OB(A)

                    elif fro == "Octal" and to == "Decimal" :
                        OD(A)
                        if n == 0:
                            put = "Equivalent " + to + " Value = " + "(" + Dec + ")" + "10"
                            out.set(put)
                            win.geometry("350x290")
                        else :
                            out.set("")
                        
                    elif fro == "Octal" and to == "Hexadecimal" :
                        OH(A)

            #Hexadecimal to others
            if fro == "Hexadecimal":
                if fro == "Hexadecimal" and to == "Binary" :
                    HB(A)

                elif fro == "Hexadecimal" and to == "Decimal" :
                    HD(A)
                    if n == 0:
                        put = "Equivalent " + to + " Value = " + "(" + Dec + ")" + "10"
                        out.set(put)
                        win.geometry("350x290")
                    else :
                        out.set("")
                    
                elif fro == "Hexadecimal" and to == "Octal" :
                    HO(A)



    # Decimal to others
    def DB(A):
        global Deca
        global Bin
        Deca = A
        Deca = int(Deca) 
        x = 0
        while Deca > 0 :
            x = Deca % 2
            global y
            y = y + str(x)
            Deca = Deca // 2
        Bin = ""
        Bin = y[::-1]
        
    def DO(A):
        global Deca
        global Oct
        Deca = A
        Deca = int(Deca)
        x = 0
        while Deca > 0 :
            x = Deca % 8
            global y
            y = y + str(x)
            Deca = Deca // 8
        Oct = ""
        Oct = y[::-1]

    def DH(A):
        global Deca
        global Hex
        Deca = A
        Deca = int(Deca)
        global x
        x = 0
        while Deca > 0 :
            x = Deca % 16
            if x >= 10:
                h()
            global y
            y = y + str(x)
            Deca = Deca // 16
        Hex = ""
        Hex = y[::-1]


    # Others to Decimal
    def BD(A):
        Bina = A
        Bina = int(Bina)
        global Dec
        global n
        o = 0
        x = 0
        y = -1
        z = 0
        n = 0
        while Bina > 0 :
            y += 1
            x = Bina % 10
            if n == 0:
                if x <= 1 and x >= 0:
                    z = 2 ** y
                    z *= x
                    o += z 
                else :
                    n = 1
                    put = ""
                    out.set(put)
                    messagebox.showinfo("Invalid Input", "Enter 0 and 1 only for type conversion!")
            Bina = Bina // 10
                
        Dec = str(o)

    def OD(A):
        Octa = A
        Octa = int(Octa)
        global Dec
        global n
        o = 0
        x = 0
        y = -1
        z = 0
        n = 0
        while Octa > 0 :
            y += 1
            x = Octa % 10
            if x <= 7 and x >= 0:
                if n == 0:
                    z = 8 ** y
                    z *= x
                    o += z 
            else :
                n = 1
                put = ""
                out.set(put)
                win.geometry("350x290")
                messagebox.showinfo("Invalid Input", "Enter Integars from 0 to 7 only for type conversion!")

            Octa = Octa // 10
                
        Dec = str(o)

    def HD(A):
        Hexa = A
        global Dec
        h = 0
        global hd
        hd = 0
        x = 0
        y = -1
        z = 0
        global n
        n = 0
        charlen = len(Hexa)
        charlen -= 1
        while charlen >= 0 :
            if n == 0:  
                y += 1
                hd = Hexa[charlen]
                
                if hd >= '0' and hd <= '9':
                    hd = int(hd)
                    
                elif hd >= 'A' and hd <= 'F':
                    hd = ord(hd)
                    hd = hd - 55
                    
                elif hd >= 'a' and hd <= 'f':
                    hd = ord(hd)
                    hd = hd - 87

                else :
                    n = 1
                    put = ""
                    out.set(put)
                    messagebox.showinfo("Invalid Input", "Enter Integars and Alphabets from A to F only for type conversion!")                

            charlen -= 1
            if n == 0:   
                z = 16 ** y
                z *= hd
                h += z
            
        Dec = str(h)

    # Octal, Hexadecimal to Binary
    def OB(A):
        global Dec
        global Deca
        global n
        OD(A)
        A = Dec
        DB(A)
        global Bin
        if n == 0:
            put = "Equivalent " + to + " Value = " + "(" + Bin + ")" + "2"
            out.set(put)
        else :
            out.set("")
            
    def HB(A):
        global Dec
        global Deca
        global n
        HD(A)
        A = Dec
        DB(A)
        global Bin
        if n == 0:
            put = "Equivalent " + to + " Value = " + "(" + Bin + ")" + "2"
            out.set(put)
        else :
            out.set("")

    # Binary, Hexadecimal to Octal
    def BO(A):
        global Dec
        global Deca
        global n
        BD(A)
        A = Dec
        DO(A)
        global Oct
        if n == 0:
            put = "Equivalent " + to + " Value = " + "(" + Oct + ")" + "8"
            out.set(put)
        else :
            out.set("")

    def HO(A):
        global Dec
        global Deca
        global n
        HD(A)
        A = Dec
        DO(A)
        global Oct
        if n == 0:
            put = "Equivalent " + to + " Value = " + "(" + Oct + ")" + "8"
            out.set(put)
        else :
            out.set("")

     # Octal, Binary to Hexadecimal
    def OH(A):
        global Dec
        global Deca
        global n
        OD(A)
        A = Dec
        DH(A)
        global Hex
        if n == 0:
            put = "Equivalent " + to + " Value = " + "(" + Hex + ")" + "16"
            out.set(put)
        else :
            out.set("")

    def BH(A):
        global Dec
        global Deca
        global n
        BD(A)
        A = Dec
        DH(A)
        global Hex
        if n == 0:
            put = "Equivalent " + to + " Value = " + "(" + Hex + ")" + "16"
            out.set(put)
            print(out.get())
        else :
            out.set("")


    # Entry, Label and Button creation
    entry = Entry(win, width= 15, textvariable = a)
    entry.place(x=175,y=175, anchor= CENTER)

    out = tk.StringVar()
    out.set("")

    label_1 = Label(win, text = "Number system converter", font=("Comic Sans MS", 16, "bold"))
    label_1.config(fg= "blue", bg = "cyan")

    label_4 = Label(win, text = "Enter origin number", font=("Comic Sans MS", 11, "bold"))
    label_4.config(fg= "black", bg = "cyan")

    label_5 = Label(win, textvariable = out, font=("Comic Sans MS", 10, "bold"))
    label_5.config(fg= "black", bg = "cyan")

    label_1.place(x=175,y=25, anchor= CENTER)
    label_4.place(x=175, y=145, anchor= CENTER)
    label_5.place(x=175, y=255, anchor= CENTER)

    button = Button(win, text= "Click to Show", bg = "blue3", fg = "white", font = ("Comic Sans MS", 10, "bold"), command= get_data)
    button.place(x=175, y=220, anchor = CENTER)

    # Combobox creation
    n = tk.StringVar()
    m = tk.StringVar()

    fromchoosen = ttk.Combobox(win, width = 20, textvariable = n)
    tochoosen = ttk.Combobox(win, width = 20, textvariable = m)
      
    # Adding combobox 'from' drop down list
    fromchoosen['values'] = ('Decimal', 
                             'Binary',
                             'Octal',
                             'Hexadecimal')

    fromchoosen.place(x = 175, y = 70, anchor = CENTER)
    fromchoosen.current()
    fromchoosen.set("Origin No. system")
    fromchoosen.bind("<<ComboboxSelected>>", origin)

    # Adding combobox 'to' drop down list
    tochoosen['values'] = ('Decimal', 
                           'Binary',
                           'Octal',
                           'Hexadecimal')

    tochoosen.place(x = 175, y = 105, anchor = CENTER)
    tochoosen.current()
    tochoosen.set("Desired No. system")
    tochoosen.bind("<<ComboboxSelected>>", desired)

    win.mainloop()

def J():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Value Changer")
    win.geometry("400x180")
    win.config(bg = "cyan")
    win.resizable(False, False)

    num1 = tk.StringVar()
    num2 = tk.StringVar()
    ans=tk.StringVar()

    def Submit():
        ans.set("")
        A = num1.get()
        B = num2.get()
        try:
            A = int(A)
            B = int(B)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter integars only")
        else:
            print("A = " + str(A))
            print("B = " + str(B)+"\n")
            A, B = B, A
            print("A = " + str(A))
            print("B = " + str(B)+"\n")
            
            win.geometry("400x210")
            ans.set("Now A = " + str(A) + " and B = " + str(B))
            
    Title = Label(win, text = "Value Changer", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    Title.place(x = 200, y = 25, anchor = CENTER)

    label_1 = Label(win, text = "Enter Numbers", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    label_1.place(x = 200, y = 67, anchor = CENTER)

    label_a = Label(win, text = "A", fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
    label_a.place(x = 100, y = 105, anchor = CENTER)

    label_b = Label(win, text = "B", fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
    label_b.place(x = 100, y = 135, anchor = CENTER)

    entry1 = Entry(win, width = 17, textvariable = num1, fg = "blue3")
    entry1.place(x = 170, y = 105, anchor = CENTER)

    entry2 = Entry(win, width = 17, textvariable = num2, fg = "blue3")
    entry2.place(x = 170, y = 135, anchor = CENTER)

    submit = Button(win, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = Submit)
    submit.place(x = 275, y = 120, anchor = CENTER)

    out = Label(win, textvariable = ans, bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
    out.place(x = 200, y = 180, anchor = CENTER)

def K():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Number to Name Convertor")
    win.geometry("400x200")
    win.config(bg = "cyan")
    win.resizable(False, False)

    num = tk.StringVar()
    ans = tk.StringVar()

    def Submit():
        ans.set("")
        A = num.get()
        try:
            A = int(A)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter integars only")
        else:
            print(A)
            print(num2words(A)) # Number Name
            print(num2words(A, to = 'ordinal')) # Alpha position
            print(num2words(A, to = 'ordinal_num')) # Numeric Position
            print(num2words(A, to = 'currency')) # Currency
            print(num2words(A, lang ='fr')) # Number name in French
            print("")
            name = num2words(A)
            ans.set("Number name of "+str(A)+" is "+name)

    Title = Label(win, text = "Number to Number Name", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    Title.place(x = 200, y = 25, anchor = CENTER)

    label_1 = Label(win, text = "Enter Number", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    label_1.place(x = 200, y = 70, anchor = CENTER)

    entry = Entry(win, width = 20, textvariable = num, fg = "blue3")
    entry.place(x = 140, y = 115, anchor = CENTER)

    ans.set("")
    submit = Button(win, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = Submit)
    submit.place(x = 260, y = 115, anchor = CENTER)

    out = Label(win, textvariable = ans, bg = "cyan", font = ("Comic Sans MS", 11, "bold"), wraplength = 300, justify = "center")
    out.place(x = 200, y = 160, anchor = CENTER)

def N():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Anglo-Francais Translator")
    win.geometry("400x200")
    win.config(bg = "cyan")
    win.resizable(False, False)

    Dict = {"Hello":"Bonjour", "Good Morning":"Bonjour", "Good Afternoon":"Bon Apres-Midi", "Good Evening":"Bonsoir",
        "Good Night":"Bonne nuit", "Hi":"Salut", "Bye":"Au Revoir", "Please":"S'ill vous plait", "Thank you":"Merci",
        "Sorry":"Desole", "How are you":"Comment allez vous", "School":"Ecole", "See you soon":"A Bientot",
        "See you tommorow":"A Demain", "Mother":"Mere", "Father":"Pere", "Brother":"Frere", "Sister":"Soeur"}
    
    List = []
    for j in Dict.keys():
        List.append(j)

    List.sort()
        
    t = tk.StringVar()
    ans = tk.StringVar()

    var = tk.Variable(value=List)

    a = 0
    def empty():
        ent.delete(0, 'end')
        ans.set("")
        
    def checkkey(event):
        a = 0
        value = event.widget.get()
          
        if value == '':
            data = List
        else:
            z = 1
            data = []
            for item in List:
                z = 1
                b = item.lower()
                d = value.lower()
                ch = len(value)
                t = len(b)
                if t < ch:
                    ch = t
                for i in range(0, ch):
                    if d[i] in b[i]:
                        m = 0
                    else :
                        z = 0

                if z == 1:
                    a += 1
                    print(a)
                    if item not in data:
                        data.append(item)
                else:
                    a = 0
       
        update(data)
        lb.place(x= 220, y= 87, anchor = "n")
        if a <= 6 :
            lb.config(height = a)
            
        else:
            lb.config(height = 6)
        
    def update(data):
        lb.delete(0, 'end')
        for item in data:
            lb.insert('end', item)

    def items_selected(event):
        ind = lb.curselection()
        lb.place_forget()
        Item = ",".join([lb.get(i) for i in ind])
        ent.delete(0,"end")
        ent.insert(0, Item)
        c = 0
        for n in Dict:
            if n == Item:
                print(Dict[Item])
                ans.set(Dict[Item])
                c = 1
        if c == 0:
            print("Sorry")
            ans.set("Sorry")

    title = Label(win, text = "Eng to French Traslator", fg = "blue2", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    title.place(x= 200, y= 25, anchor = CENTER)

    eng = Label(win, text = "Eng", fg = "black", bg = "cyan", font = ("Comic Sans MS", 14, "bold"))
    eng.place(x= 100, y= 75, anchor = CENTER)

    fre = Label(win, text = "Fre", fg = "black", bg = "cyan", font = ("Comic Sans MS", 14, "bold"), justify = "left")
    fre.place(x= 100, y= 140, anchor = CENTER)

    dis = Label(win, textvariable = ans, bg = "white", width = 20, font = ("Comic Sans MS", 10, "bold"))
    dis.place(x= 220, y= 140, anchor = CENTER)

    ent = Entry(win, width = 20, font = ("Comic Sans MS", 10, "bold"))
    ent.place(x= 220, y= 75, anchor = CENTER)
    ent.bind('<KeyRelease>', checkkey)

    lb = tk.Listbox(win, listvariable=var, height=6, selectmode=tk.EXTENDED)
    lb.bind('<<ListboxSelect>>', items_selected)

    cle = Button(win, text = " C ", fg = "white", bg = "blue2", font = ("Comic Sans MS", 8, "bold"), command = empty, borderwidth=0)
    cle.place(x= 290, y= 75, anchor = CENTER)
    win.mainloop()

def O():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Geometry")
    win.geometry("400x200")
    win.config(bg = "cyan")
    win.resizable(False, False)

    Ans = tk.StringVar()
    n = tk.StringVar()
    m = tk.StringVar()

    a = tk.StringVar()
    b = tk.StringVar()
    c = tk.StringVar()

    ans = 0
    peri = 0
    area = 0
    def r():
        print("")
        ans = 0
        peri = 0
        area = 0
        A = 0
        B = 0
        C = 0
        n.set("")
        m.set("")
        a.set("")
        b.set("")
        c.set("")
        Ans.set("")
        opt.config(text = "Unit is cm")
        dis.config(text = "")
        submit.config(command = lambda : Submit(ty, sh))
        win.geometry("400x200")
        ent1.place_forget()
        ent2.place_forget()
        ent3.place_forget()
        Ty.place(x = 200, y = 70, anchor = CENTER)
        Ty.set("Select Operation")
        Sh.place(x = 200, y = 110, anchor = CENTER)
        Sh.set("Select Shape")
        ch.place_forget()
        submit.place(x = 200, y = 155, anchor = CENTER)
        opt.place_forget()
        
    def go(ty, sh):
        global Y
        A = 0
        B = 0
        C = 0
        global ans
        A = a.get()
        if sh == "Rectangle" or sh == "Cylinder" or sh == "Right-angled Triangle":
            B = b.get()
        elif sh == "Normal Triangle" :
            B = b.get() 
            C = c.get()
        try:
            A = int(A)
            B = int(B)
            C = int(C)
        except ValueError:
            messagebox.showerror("Invalid Input!", "Enter integars only")
        else:
            if sh == "Square":
                print("Side = " + str(A))
                peri = A * 4
                area = A * A
                if ty == "Perimeter":
                    ans = peri
                elif ty == "Area":
                    ans = area

            elif sh == "Rectangle":
                print("Length = " + str(A))
                print("Height = " + str(B))
                peri = 2*(A+B)
                area = A * B
                if ty == "Perimeter":
                    ans = peri
                elif ty == "Area":
                    ans = area

            elif sh == "Right-angled Triangle":
                C = (A*A) + (B*B)
                C = math.sqrt(C)
                peri = A + B + C
                area = A * B
                peri = round(peri, 3)
                area = round(area, 3)
                if ty == "Perimeter":
                    ans = peri
                    print("Height = " + str(B))
                elif ty == "Area":
                    ans = area
                    print("Perp. = " + str(B))
                print("Base = " + str(A))

            elif sh == "Normal Triangle":
                peri = A + B + C
                s = peri/2
                area = s*(s-A)*(s-B)*(s-C)
                area = math.sqrt(area)
                area = round(area, 3)
                if ty == "Perimeter":
                    ans = peri
                elif ty == "Area":
                    ans = area
                print("Side A = " + str(A))
                print("Side B = " + str(B))
                print("Side C = " + str(C))

            elif sh == "Circle":
                peri = 2 * A * 22/7
                area = A * A * 22/7
                peri = round(peri, 3)
                area = round(area, 3)
                if ty == "Perimeter":
                    ans = peri
                elif ty == "Area":
                    ans = area
                print("Radius = " + str(A))

            elif sh == "Cylinder":
                peri = 2 * A * 22/7 * B
                area = A * A * 22/7 * B
                peri = round(peri, 3)
                area = round(area, 3)
                if ty == "Perimeter":
                    ans = peri
                elif ty == "Area":
                    ans = area
                print("Radius = " + str(A))
                print("Height = " + str(B))

            opt.config(text = (ty + " of " + sh)) 
            Ans.set(str(ans)+" cm")
            print(ty + " of this " + sh + " = " + str(ans))
            ch.place(x = 340, y = 80, anchor = CENTER)
            dis.place(x = 300, y = Y, anchor = CENTER)
            opt.place(x = 90, y = Y, anchor = CENTER)

    def Submit(ty, sh):
        global Y
        opt.place(x = 90, y = 155, anchor = CENTER)
        print(ty)
        print(sh)
        global peri
        global area
        global placeholder1
        global placeholder2
        global placeholder3
        Ty.place_forget()
        Sh.place_forget()
        ent1.place(x = 200, y = 70, anchor = CENTER)

        if sh == "Square":
            win.geometry("400x160")
            submit.place(x = 200, y = 115, anchor = CENTER)
            opt.place(x = 93, y = 115, anchor = CENTER)
            dis.place(x = 300, y = 115, anchor = CENTER)
            Y = 115
            
        elif sh == "Rectangle":
            ent1.delete(0,'end')
            placeholder1 = 'Please enter length'
            ent1.insert(0,placeholder1)
            ent2.delete(0,'end')
            placeholder2 = 'Please enter breadth'
            ent2.insert(0,placeholder2)
            ent2.place(x = 200, y = 110, anchor = CENTER)
            Y = 155
                
        elif sh == "Right-angled Triangle":
            if ty == "Perimeter":
                placeholder1 = 'Please enter perp.'            
            elif ty == "Area":
                placeholder1 = 'Please enter height'

            placeholder2 = 'Please enter base'    
            ent1.delete(0,'end')
            ent1.insert(0,placeholder1)
            ent2.delete(0,'end')
            ent2.insert(0,placeholder2)
            ent2.place(x = 200, y = 110, anchor = CENTER)
            Y = 155

        elif sh == "Normal Triangle":
            win.geometry("400x250")
            submit.place(x = 200, y = 205, anchor = CENTER)
            opt.place(x = 93, y = 205, anchor = CENTER)
            dis.place(x = 300, y = 205, anchor = CENTER)

            placeholder1 = 'Please enter side A.'
            placeholder2 = 'Please enter side B.'
            placeholder3 = 'Please enter side C.'                    
            ent1.delete(0,'end')
            ent1.insert(0,placeholder1)
            ent2.delete(0,'end')
            ent2.insert(0,placeholder2)
            ent2.place(x = 200, y = 110, anchor = CENTER)
            ent3.delete(0,'end')
            ent3.insert(0,placeholder3)
            ent3.place(x = 200, y = 150, anchor = CENTER)
            Y = 205
            
        elif sh == "Circle":
            win.geometry("400x160")
            submit.place(x = 200, y = 115, anchor = CENTER)
            opt.place(x = 93, y = 115, anchor = CENTER)
            dis.place(x = 300, y = 115, anchor = CENTER)
            
            placeholder1 = 'Please enter radius.'                    
            ent1.delete(0,'end')
            ent1.insert(0,placeholder1)
            Y = 115

        elif sh == "Cylinder":
            placeholder1 = 'Please enter base radius'
            placeholder2 = 'Please enter height'
            ent1.delete(0,'end')
            ent1.insert(0,placeholder1)
            ent2.delete(0,'end')
            ent2.insert(0,placeholder2)
            ent2.place(x = 200, y = 110, anchor = CENTER)
            Y = 155
            
        submit.config(command = lambda : go(ty, sh))

    def sen(event):
        global ty
        ty = event.widget.get()

    def sem(event):
        global sh
        sh = event.widget.get()

    Title = Label(win, text = "Geometry Assistant", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    Title.place(x = 200, y = 30, anchor = CENTER)

    Ty = ttk.Combobox(win, width = 20, textvariable = n)
    Ty['values'] = ('Perimeter', 
                    'Area')

    Ty.place(x = 200, y = 70, anchor = CENTER)
    Ty.current()
    Ty.set("Select Operation")
    Ty.bind("<<ComboboxSelected>>", sen)

    Sh = ttk.Combobox(win, width = 20, textvariable = m)
    Sh['values'] = ('Square', 
                    'Rectangle',
                    'Right-angled Triangle',
                    'Normal Triangle',
                    'Circle',
                    'Cylinder')

    Sh.place(x = 200, y = 110, anchor = CENTER)
    Sh.current()
    Sh.set("Select Shape")
    Sh.bind("<<ComboboxSelected>>", sem)

    ent1 = Entry(win, textvariable = a, width = 20, font = ("Comic Sans MS", 10, "bold"))
    ent2 = Entry(win, textvariable = b, width = 20, font = ("Comic Sans MS", 10, "bold"))
    ent3 = Entry(win, textvariable = c, width = 20, font = ("Comic Sans MS", 10, "bold"))

    global placeholder1
    global placeholder2
    global placeholder3

    placeholder1 = 'Please enter side'
    def erase_a(event=None):
        if ent1.get() == placeholder1:
            ent1.delete(0,'end')
    def add_a(event=None):
        if ent1.get() == '':
            ent1.insert(0,placeholder1)
    add_a()
    ent1.bind('<FocusIn>',erase_a)
    ent1.bind('<FocusOut>',add_a)

    placeholder2 = 'Please enter 2nd side'
    def erase_b(event=None):
        if ent2.get() == placeholder2:
            ent2.delete(0,'end')
    def add_b(event=None):
        if ent2.get() == '':
            ent2.insert(0,placeholder2)
    add_b()
    ent2.bind('<FocusIn>',erase_b)
    ent2.bind('<FocusOut>',add_b)

    placeholder3 = 'Please enter 3rd side'
    def erase_c(event=None):
        if ent3.get() == placeholder3:
            ent3.delete(0,'end')
    def add_c(event=None):
        if ent3.get() == '':
            ent3.insert(0,placeholder3)
    add_c()
    ent3.bind('<FocusIn>',erase_c)
    ent3.bind('<FocusOut>',add_c)

    opt = Label(win, text = "Unit is cm", wraplength = 120, fg = "black", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))

    dis = Label(win, textvariable = Ans, fg = "black", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    dis.place(x = 300, y = 155, anchor = CENTER)

    submit = Button(win, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = lambda : Submit(ty, sh))
    submit.place(x = 200, y = 155, anchor = CENTER)

    ch = Button(win, text = "Reuse", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = r)

def P():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Number Guessing game")
    win.geometry("400x250")
    win.config(bg = "cyan")
    win.resizable(False, False)
    win.iconphoto(False, tk.PhotoImage(file="globe.png"))

    num = tk.StringVar()
    ans=tk.StringVar()
    r=tk.StringVar()

    global t
    t = 5

    def Guess():
        global x
        global Sum
        x = random.randint(1, 99)
        global evod
        if x % 2 == 0:
            evod = "even"
        else:
            evod = "odd"

        global prote
        fac = 0
        for i in range(1, x+1):
            if x % i == 0:
                fac += 1
        if fac == 2:
            prote = " prime"
        else:
            prote = " composite"

        y = str(x)
        global dig
        a = 0
        b = 0
        if x > 10:
            dig = " 2-digit"
            a = y[0]
            b = y[1]
        else:
            dig = " 1-digit"
            a = y[0]
        Sum = int(a) + int(b) 
            
    Guess()

    def fin():
        global t
        turn = 5 - t
        turn = num2words(turn)
        ans.set("Congratulations!")
        r.set("You won!")
        clue_1.config(text = "You guessed me in " + turn + " turns")
        clue_2.config(text = "The Coder's mystery was hacked by you")
        entry.place_forget()
        out.place_forget()
        submit.config(text = "Play Again")
        submit.config(command = reset)
        submit.place(x = 200, y = 200, anchor = CENTER)
        
    def Submit():
        global x
        ans.set("")
        A = num.get()
        num.set("")
        try:
            A = int(A)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter integars only")
        else:
            print("You entered "+str(A))
            global t
            t -= 1
            r.set("You have " + str(t) + " attempts")
            
            if A < x:
                ans.set("Too Low")
                
            elif A > x:
                ans.set("Too High")
                
            elif A == x:
                fin()

            pro(t)

    def pro(t):
        if t == 0:
            print("")
            end()

    def end():
        global x
        ans.set("")
        r.set("No attempts left!")
        clue_1.config(text = "You could not guess me! Ha Ha Ha")
        clue_2.config(text = "The Coder's mystery number was "+str(x))
        entry.place_forget()
        out.place_forget()
        submit.config(text = "Try Again")
        submit.config(command = reset)
        submit.place(x = 200, y = 200, anchor = CENTER)

    def reset():
        Guess()

        global evod
        global dig
        global Sum
        global t
        
        ans.set("")
        
        t = 5
        r.set("You have " + str(t) + " attempts")
        clue_1.config(text = "I am an " + evod + prote + dig + " number")
        clue_2.config(text = "Sum of my digits is " + str(Sum))
        entry.place(x = 140, y = 185, anchor = CENTER)
        out.place(x = 200, y = 220, anchor = CENTER)
        submit.config(text = "Submit")
        submit.config(command = Submit)
        submit.place(x = 260, y = 185, anchor = CENTER)
               
    Title = Label(win, text = "Guess the Coder's number", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    Title.place(x = 200, y = 25, anchor = CENTER)

    r.set("You have " + str(t) + " attempts")
    rule_1 = Label(win, textvariable = r, fg = "blue", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    rule_1.place(x = 200, y = 70, anchor = CENTER)

    global evod
    global dig
    clue_1 = Label(win, text = "I am an " + evod + prote + dig + " number", fg = "black", bg = "cyan", font = ("Comic Sans MS", 14, "bold"))
    clue_1.place(x = 200, y = 105, anchor = CENTER)

    global Sum
    clue_2 = Label(win, text = "Sum of my digits is " + str(Sum), fg = "black", bg = "cyan", font = ("Comic Sans MS", 14, "bold"))
    clue_2.place(x = 200, y = 140, anchor = CENTER)

    entry = Entry(win, width = 20, textvariable = num, fg = "blue3")
    entry.place(x = 140, y = 185, anchor = CENTER)

    submit = Button(win, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = Submit)
    submit.place(x = 260, y = 185, anchor = CENTER)

    out = Label(win, textvariable = ans, bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
    out.place(x = 200, y = 220, anchor = CENTER)
    
#Dashboard
def p():
    global cas
    global l
    l.config(fg = "white")
    pr.set("My Portfolio")
    img = tk.PhotoImage(file=r"Portfolio.png")
    newWindow.img = img
    cas.create_image((0,0), image=img, anchor='nw')
    cas.pack(side = BOTTOM, pady = 20, padx = 20)
    
def c():
    global cas
    global l
    l.config(fg = "white")
    pr.set("Contact Me")
    img = tk.PhotoImage(file=r"Contact1.png")
    newWindow.img = img
    cas.create_image((0,0), image=img, anchor='nw')
    cas.pack(side = BOTTOM, pady = 20, padx = 20)
    

def dab(ab):
    global newWindow
    def da():
        global cas
        global l
        l.config(fg = "white", bg = "black")
        pr.set("Welcome "+ab)
        img = tk.PhotoImage(file=r"Dashboard.png")
        newWindow.img = img
        cas.create_image((0,0), image=img, anchor='nw')
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
    menubar.add_cascade(label ='Projects', menu = proj)

    cals = Menu(proj, tearoff=0)
    cals.add_command(label='Maths', command = A)
    cals.add_command(label='BMI', command = B)
    cals.add_command(label='Profit Loss', command = C)
    cals.add_command(label='Tally Marks', command = D)
    cals.add_command(label='Tendencies', command = E)
    cals.add_command(label='Factorial', command = F)
    cals.add_command(label='Interest', command = G)

    covs = Menu(proj, tearoff=0)
    covs.add_command(label='Number system', command = H)
    covs.add_command(label='Value Changer', command = J)
    covs.add_command(label='Number to Number Name', command = K)


    oths = Menu(proj, tearoff=0)
    oths.add_command(label='Eng to Fre Translator', command = N)
    oths.add_command(label='Geometry', command = O)
    oths.add_command(label='Guess the Number', command = P)

    proj.add_cascade(label ='Calculators', menu=cals, command = None)
    proj.add_cascade(label ='Convertors', menu=covs, command = None)
    proj.add_separator()
    proj.add_cascade(label ='Misc.', menu=oths, command = None)
      
    newWindow.config(menu = menubar)

    global cas
    global l
    
    cas = tk.Canvas(newWindow,width=298,height=168, bg = "black", highlightthickness=3, highlightbackground="black")
    da()
    
def Sig():
    newWindow.destroy()

#Root Widgets
menubar = Menu(root)
  
about = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='About', menu = about)
about.add_command(label ='Porfolio', command = a)
about.add_command(label ='Contact', command = b)
about.add_separator()
about.add_command(label ='Exit', command = root.destroy)
  
user = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='User', menu = user)
user.add_command(label ='Login', command = Log)
user.add_command(label ='Register', command = Reg)
user.add_command(label ='Forgot Password', command = For)

proj = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Features', menu = proj)

cals = Menu(proj, tearoff=0)
cals.add_command(label='Maths', command = aa)
cals.add_command(label='BMI', command = ab)
cals.add_command(label='Profit Loss', command = ac)
cals.add_command(label='Tally Marks', command = ad)
cals.add_command(label='Tendencies', command = ae)
cals.add_command(label='Factorial', command = af)
cals.add_command(label='Interest', command = ag)

covs = Menu(proj, tearoff=0)
covs.add_command(label='Number system', command = ba)
covs.add_command(label='Value Changer', command = bc)
covs.add_command(label='Number to Number Name', command = bd)

oths = Menu(proj, tearoff=0)
oths.add_command(label='Eng to Fre Translator', command = db)
oths.add_command(label='Geometry', command = dc)
oths.add_command(label='Number Guessing Game', command = dd)

proj.add_cascade(label ='Calculators', menu=cals, command = None)
proj.add_cascade(label ='Convertors', menu=covs, command = None)
proj.add_separator()
proj.add_cascade(label ='Misc.', menu=oths, command = None)
  
root.config(menu = menubar)
pro = Label(root, textvariable = project, fg = "white",  bg = "blue", font = ("Comic Sans MS", 20, "bold"))
pro.place(x = 27, y = 28, anchor = W)
canvas = tk.Canvas(root,width=294,height=166, bg = "cyan", highlightthickness=3, highlightbackground="black")

global can
can = tk.Canvas(root,width=350,height=270, bg = "cyan", highlightbackground="white")

two = tk.PhotoImage(file=r'Page.png')
root.two = two
can.create_image((0,0), image=two, anchor='nw')
can.pack(side = BOTTOM, pady = 0, padx = 0)

root.mainloop()
mycursor = mydb.cursor() 

root = tk.Tk()
root.title("Mayank's Webpage")
root.geometry("350x270")
root.config(bg = "blue")
root.iconphoto(False, tk.PhotoImage(file="globe.png"))
root.resizable(False, False)

project = tk.StringVar()
pr = tk.StringVar()

name =tk.StringVar()
email =tk.StringVar()
pas =tk.StringVar()
repas =tk.StringVar()
coun =tk.StringVar()
state =tk.StringVar()
city =tk.StringVar()

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
    newWindow.iconphoto(False, tk.PhotoImage(file="globe.png"))
    newWindow.resizable(False, False)

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
        
    CAP = temp_pass
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
        mycursor.reset()
        mycursor.execute(query, (Email,Pass))
        result=mycursor.fetchone()
        
        query = """SELECT NAME FROM credentials where EMAIL = %s and PASSWORD = %s"""
        mycursor.reset()
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
    bgC = 'black'
    fgC = 'white'
    newWindow = Toplevel(root)
    newWindow.title("Login")
    newWindow.geometry("350x250")
    newWindow.config(bg = bgC)
    newWindow.iconphoto(False, tk.PhotoImage(file="globe.png"))
    newWindow.resizable(False, False)
    
    captcha()
    button = Button(newWindow, text = "Move to Login", fg = "white", bg = "blue", font = ("Comic Sans MS", 13, "bold"), command = m)

    lab_em = Label(newWindow, text = "Email", bg = bgC, fg = fgC, font = ("Comic Sans MS", 13, "bold"))
    lab_em.place(x = 20, y = 60, anchor = W)
    ent_em = Entry(newWindow, textvariable = email, width = 25, font = ("Comic Sans MS", 10, "bold"))
    ent_em.place(x = 125, y = 60, anchor = W)

    lab_pa = Label(newWindow, text = "Password", bg = bgC, fg = fgC, font = ("Comic Sans MS", 13, "bold"))
    lab_pa.place(x = 20, y = 100, anchor = W)
    ent_pa = Entry(newWindow, textvariable = pas, width = 25, font = ("Comic Sans MS", 10, "bold"), show = "*")
    ent_pa.place(x = 125, y = 100, anchor = W)

    lab_ca = Label(newWindow, text = "Captcha", bg = bgC, fg = fgC, font = ("Comic Sans MS", 13, "bold"))
    lab_ca.place(x = 20, y = 140, anchor = W)
    cap_ca = Label(newWindow, text = CAP, bg = bgC, font = ("Comic Sans MS", 13, "bold"))
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
    newWindow.iconphoto(False, tk.PhotoImage(file="globe.png"))
    newWindow.resizable(False, False)

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

#Image commands
def a():
    global canvas
    pro.config(fg = "white")
    project.set("My Portfolio")
    one = tk.PhotoImage(file=r"Portfolio.png")
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()
    
def b():
    global canvas
    pro.config(fg = "white")
    project.set("Contact Me")
    one = tk.PhotoImage(file=r'Contact.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def aa():
    global canvas
    pro.config(fg = "white")
    project.set("Calculator")
    one = tk.PhotoImage(file=r"Calculator.png")
    root.one = one
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    root.geometry("350x528")
    canvas.config(height = 444)
    global can
    can.pack_forget()

def ab():
    global canvas
    pro.config(fg = "white")
    project.set("BMI Calculator")
    one = tk.PhotoImage(file=r'BMI.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def ac():
    global canvas
    pro.config(fg = "white")
    project.set("Profit Loss")
    one = tk.PhotoImage(file=r"Profit Loss.png")
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def ad():
    global canvas
    pro.config(fg = "white")
    project.set("Tally Marks")
    one = tk.PhotoImage(file=r"Tally.png")
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()
    
def ae():
    global canvas
    pro.config(fg = "white")
    project.set("Number Tendencies")
    one = tk.PhotoImage(file=r'Number tendencies.png')
    root.one = one 
    canvas.config(height = 281)
    root.geometry("350x365")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()
    
def af():
    global canvas
    pro.config(fg = "white")
    project.set("Factorial Calculator")
    one = tk.PhotoImage(file=r"Factorial.png")
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def ag():
    global canvas
    pro.config(fg = "white")
    project.set("Interest Calculator")
    one = tk.PhotoImage(file=r'Interest.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()
    
def ba():
    global canvas
    pro.config(fg = "white")
    project.set("Number system")
    one = tk.PhotoImage(file=r'Number system.png')
    root.one = one 
    canvas.config(height = 270)
    root.geometry("350x354")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def bc():
    global canvas
    pro.config(fg = "white")
    project.set("Value Changer")
    one = tk.PhotoImage(file=r'Value changer.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def bd():
    global canvas
    pro.config(fg = "white")
    project.set("Number to Name")
    one = tk.PhotoImage(file=r'Number name.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()
    
def ca():
    global canvas
    pro.config(fg = "black")
    project.set("Question Game")
    one = tk.PhotoImage(file=r'Question.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def db():
    pro.config(fg = "white")    
    project.set("Eng to French")
    one = tk.PhotoImage(file=r"Eng to French.png")
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def dc():
    global canvas
    pro.config(fg = "white")
    project.set("Geometry Assist")
    one = tk.PhotoImage(file=r'Geometry.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()

def dd():
    global canvas
    pro.config(fg = "white")
    project.set("Guess the number")
    one = tk.PhotoImage(file=r'Number guessing game.png')
    root.one = one 
    canvas.config(height = 166)
    root.geometry("350x250")
    canvas.create_image((0,0), image=one, anchor='nw')
    canvas.pack(side = BOTTOM, pady = 20, padx = 20)
    global can
    can.pack_forget()
    
#Dashboard
def A():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Calculator")
    win.geometry("300x420")
    win.config(bg = "cyan")
    win.resizable(False, False)

    ops = ["a", "b", "c", "d", "e", "f", "eq", "CE", "C", "bk", "sq", "rt", "cu", "curt", "rec"]
    global num1
    num1 = 0
    global num2
    num2 = 0
    global Ans
    Ans = 0
    global op
    op = ""
    global A
    A = 0

    def callback(ans):
        char= ans.get()
        try :
            char = float(char)
        except ValueError:
            ans.set(ans.get()[0:-1])

    def enter(args):
        global op
        global num1
        global num2
        if args in ops:
            if args == "eq" and float(num1) != 0:
                equal(args)
                print("")
                
            elif args == "a" or args == "b" or args == "c" or args == "d" or args == "sq" or args == "rt" or args == "per" or args == "cu" or args == "curt" or args == "rec" :
                oper(args)
                
            elif args == "C":
                op = ""
                num1 = 0
                num2 = 0
                ans.set("")
                print("")
                
            elif args == "CE":
                ans.set("")

            elif args == "bk":
                ans.set(ans.get()[0:-1])

            elif args == "e":
                a = ans.get()
                a = float(a)
                if (a % 1) == 0:
                    a = int(a)
                    ans.set(str(a)+".")
                else:
                    ans.set(float(ans.get()))

            elif args == "f":
                val = float(ans.get())
                val = 0 - float(val)
                if val % 1 == 0:
                    val = int(val)
                else:
                    val = float(val)
                ans.set(val)
                
        else:
            char = ""
            char = ans.get()
            char += str(args)
            ans.set(char)

    def equal(args):
        global op
        global num1
        global num2
        num2 = ans.get()
        print(num2)
        ans.set("")
        print(str(num1)+op+str(num2))
        oper(args)
        global Ans
        Ans = round(Ans, 3)
        if Ans % 1 == 0:
            Ans = int(Ans)
        else:
            Ans = float(Ans)
        a = str(Ans)
        if len(a) > 12:
            charlen = len(a)
            charlen
            b = 1
            for i in range(1, charlen+1):
                b *= 10
            a = int(Ans)
            a = a / b
            a = round(a, 6)
            sc = str(a) + " * 10 ^ "+str(i)
        ans.set(Ans)
        op = ""
        num1 = 0
        num2 = 0
        Ans = 0

    def Eq():
        global Ans
        global op
        global num1
        global num2
        Ans = round(Ans, 3)
        if Ans % 1 == 0:
            Ans = int(Ans)
        else:
            Ans = float(Ans)
        ans.set(Ans)
        print("")
        op = ""
        num1 = 0
        num2 = 0
        Ans = 0
        
    def oper(args):
        global num1
        global op
        global Ans
        if args == "a" or op == "+":
            op = "+"
            if args == "eq":
                Ans = float(num1) + float(num2)
                print(Ans)
            
        elif args == "b" or op == "-":
            op = "-"
            if args == "eq":
                Ans = float(num1) - float(num2)
                print(Ans)
            
        elif args == "c" or op == "x":
            op = "x"
            if args == "eq":
                Ans = float(num1) * float(num2)
                print(Ans)

        elif args == "d" or op == "/":
            op = "/"
            if args == "eq":
                Ans = float(num1) / float(num2)
                print(Ans)

        num1 = ans.get()
        print(num1)
        ans.set("")
        
        if args == "sq" or op == "sq":
            op = "sq"
            Ans = float(num1) * float(num1)
            print(Ans)
            Eq()
        elif args == "rt" or op == "rt":
            import math
            op = "rt"
            Ans = math.sqrt(float(num1))
            print(Ans)
            Eq()

        elif args == "cu" or op == "cu":
            op = "cu"
            Ans = float(num1) * float(num1) * float(num1)
            print(Ans)
            Eq()

        elif args == "curt" or op == "curt":
            op = "curt"
            Ans = num1
            Ans = np.cbrt(Ans)
            print(Ans)
            Eq()

        elif args == "rec" or op == "rec":
            op = "rec"
            Ans = 1/float(num1)
            print(Ans)
            Eq()            

    def Next(event):
        global A
        print("hi")
        if A % 2 == 0:
            win.geometry("360x420")
            entry.place(x=180, y=50, anchor = CENTER)
            entry.config(width = 15)
            sq.place(x=300, y=120, anchor = CENTER)
            win.place(x=300, y=180, anchor = CENTER)
            Cu.place(x=300, y=240, anchor = CENTER)
            curt.place(x=300, y=300, anchor = CENTER)
            rec.place(x=300, y=360, anchor = CENTER)
            
        elif A % 2 == 1:
            win.geometry("300x420")
            entry.place(x=150, y=50, anchor = CENTER)
            entry.config(width = 12)
            sq.place_forget()
            win.place_forget()
            Cu.place_forget()
            curt.place_forget()
            rec.place_forget()
            
        A += 1 
        
    ans = StringVar()
    ans.trace("w", lambda name, index,mode, ans=ans: callback(ans))

    entry=Entry(win, textvariable = ans, width = 12, font = ("Xenara", 28, "bold"), justify = "right")
    entry.place(x=150, y=50, anchor = CENTER)

    clent = Button(win, text = " CE ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("CE"))
    clent.place(x=60, y=120, anchor = CENTER)

    clear = Button(win, text = " C ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("C"))
    clear.place(x=120, y=120, anchor = CENTER)

    bksp = Button(win, text = " ⌫ ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("bk"))
    bksp.place(x=180, y=120, anchor = CENTER)

    add = Button(win, text = " + ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("a"))
    add.place(x=240, y=120, anchor = CENTER)

    but_one = Button(win, text = " 1 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(1))
    but_one.place(x=60, y=180, anchor = CENTER)

    but_two = Button(win, text = " 2 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(2))
    but_two.place(x=120, y=180, anchor = CENTER)

    but_three = Button(win, text = " 3 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(3))
    but_three.place(x=180, y=180, anchor = CENTER)

    sub = Button(win, text = " - ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("b"))
    sub.place(x=240, y=180, anchor = CENTER)

    but_four = Button(win, text = " 4 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(4))
    but_four.place(x=60, y=240, anchor = CENTER)

    but_five = Button(win, text = " 5 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(5))
    but_five.place(x=120, y=240, anchor = CENTER)

    but_six = Button(win, text = " 6 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(6))
    but_six.place(x=180, y=240, anchor = CENTER)

    mul = Button(win, text = " x ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("c"))
    mul.place(x=240, y=240, anchor = CENTER)

    but_seven = Button(win, text = " 7 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(7))
    but_seven.place(x=60, y=300, anchor = CENTER)

    but_eight = Button(win, text = " 8 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(8))
    but_eight.place(x=120, y=300, anchor = CENTER)

    but_nine = Button(win, text = " 9 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(9))
    but_nine.place(x=180, y=300, anchor = CENTER)

    div = Button(win, text = " / ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("d"))
    div.place(x=240, y=300, anchor = CENTER)

    sign = Button(win, text = "+/-", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("f"))
    sign.place(x=60, y=360, anchor = CENTER)

    but_zero = Button(win, text = " 0 ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter(0))
    but_zero.place(x=120, y=360, anchor = CENTER)

    point = Button(win, text = ".", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("e"))
    point.place(x=180, y=360, anchor = CENTER)

    eq = Button(win, text = " = ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("eq"))
    eq.place(x=240, y=360, anchor = CENTER)

    sq = Button(win, text = " sq ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("sq"))
    win = Button(win, text = " √ ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("rt"))
    Cu = Button(win, text = " cu ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("cu"))
    curt = Button(win, text = " ∛ ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("curt"))
    rec = Button(win, text = " 1/x ", fg="white", bg = "blue", width = 3, height = 1, font = ("Comic Sans MS", 15,"bold"), command = lambda: enter("rec"))

    more = Label(win, text = " → ", fg = "white", bg = "white", font = ("Comic Sans MS", 22, "bold"))
    more.place(x=54, y=50, anchor = CENTER)
    more.bind("<Button-1>", Next)

def B():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("BMI Calculator")
    win.geometry("400x230")
    win.config(bg = "cyan")
    win.resizable(False, False)

    wei = tk.StringVar()
    hei = tk.StringVar()
    ans = tk.StringVar()

    def Submit():
        ans.set("")
        A = wei.get()
        B = hei.get()
        try:
            A = float(A)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter numericals only")
        else:
            try:
                B = float(B)
            except ValueError:
                messagebox.showerror("Invalid Input", "Enter numericals only")
            else:
                print(A)
                print(B)
                BMI = A/(B*B)
                BMI = round(BMI, 2)
                print(BMI)
                print("")
                ans.set(BMI)
            
    Title = Label(win, text = "BMI Calculator", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 19, "bold"))
    Title.place(x = 200, y = 25, anchor = CENTER)

    placeholder_A = "Enter your weight (kg)"
    entry_1 = Entry(win, width = 20, textvariable = wei, font = ("Comic Sans MS", 11, "bold"))
    entry_1.place(x = 200, y = 70, anchor = CENTER)
    def erase_A(event=None):
        if entry_1.get() == placeholder_A:
            entry_1.delete(0,'end')
            
    def add_A(event=None):
        if entry_1.get() == '':
            entry_1.insert(0,placeholder_A)

    add_A()
    entry_1.bind('<FocusIn>',erase_A)
    entry_1.bind('<FocusOut>',add_A)

    placeholder_B = "Enter your height (m)"
    entry_2 = Entry(win, width = 20, textvariable = hei, font = ("Comic Sans MS", 11, "bold"))
    entry_2.place(x = 200, y = 110, anchor = CENTER)
    def erase_B(event=None):
        if entry_2.get() == placeholder_B:
            entry_2.delete(0,'end')
            
    def add_B(event=None):
        if entry_2.get() == '':
            entry_2.insert(0,placeholder_B)

    add_B()
    entry_2.bind('<FocusIn>',erase_B)
    entry_2.bind('<FocusOut>',add_B)

    submit = Button(win, text = "Calculate", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = Submit)
    submit.place(x = 200, y = 160, anchor = CENTER)

    out = Label(win, textvariable = ans, bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
    out.place(x = 200, y = 205, anchor = CENTER)

def C():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Profit Loss Calculator")
    win.geometry("400x170")
    win.config(bg = "cyan")
    win.resizable(False, False)

    wei = tk.StringVar()
    hei = tk.StringVar()
    ans = tk.StringVar()
    num = tk.StringVar()
    ans=tk.StringVar()
    n = tk.StringVar()
    a = tk.StringVar()
    b = tk.StringVar()
    op = ""

    def Submit(op):
        if op == "":
            messagebox.showerror("No Input", "Choose operation please")
        else:
            ans.set("")
            A = a.get()
            B = b.get()
            try:
                A = int(A)
                B = int(B)
            except ValueError:
                messagebox.showerror("Invalid Input", "Enter integars only")
            else:
                print(A)
                print(B)
                ans.set(A)
                ent1.place_forget()
                ent2.place_forget() 
                submit.place_forget()
                Ty.place_forget()
                lab.place_forget()
                if op == 'Cost Price' or op == 'Selling Price':
                    Price(op, A, B)
                elif op == 'Profit or Loss' or op == 'Profit or Loss %':
                    Pro(op, A, B)

    def fin(out, A, B):
        global M
        global N
        
        x.config(text = str(M) + " was " + str(A))
        x.place(x = 110, y = 70, anchor = W)

        y.config(text = str(N) + " was " + str(B))
        y.place(x = 110, y = 115, anchor = W)
        
        z.config(text = out)
        z.place(x = 110, y = 160, anchor = W)
        
    def Price(op, A, B):
        if op == 'Cost Price':
            cp = A - B
            cp = round(cp, 3)
            print("Cost Price = "+str(cp))
            out = "Cost Price = "+str(cp)
            
        elif op == 'Selling Price':
            sp = A + B
            sp = round(sp, 3)
            print("Selling Price = "+str(sp))
            out = "Selling Price = "+str(sp)
        fin(out, A, B)
        
    def Pro(op, A, B):
        if op == 'Profit or Loss':
            pro = B - A
            pro = round(pro, 3)
            print("Profit = "+str(pro))
            out = "Profit = "+str(pro)
            
        elif op == 'Profit or Loss %':
            per = B - A
            per = (per/A) * 100
            per = round(per, 3)
            print("Profit = " + str(per) + "%")
            out = "Profit = " + str(per) + "%"
        fin(out, A, B)
            
    def sel(event):
        op = event.widget.get()
        print(op)
        submit.config(command = lambda : Submit(op))
        lab.place_forget()

        win.geometry("400x200")
        global M
        global N
        global placeholder1
        global placeholder2
        if op == 'Cost Price':
            placeholder1 = 'Enter S.P.'
            placeholder2 = 'Enter Profit or Loss'
            win.geometry("400x220")
            lab.config(text = "Express Gain in +ve and Loss in -ve")
            lab.place(x = 200, y = 195, anchor = CENTER)
            M = "Selling Price"
            N = "Profit/Loss"
            
        elif op == 'Selling Price':
            placeholder1 = 'Enter C.P.'
            win.geometry("400x220")
            placeholder2 = 'Enter Profit or Loss'
            lab.config(text = "Express Gain in +ve and Loss in -ve")
            lab.place(x = 200, y = 195, anchor = CENTER)
            M = "Cost Price"
            N = "Profit/Loss"
            
        elif op == 'Profit or Loss':
            placeholder1 = 'Enter C.P.'
            placeholder2 = 'Enter S.P.'
            M = "Cost Price"
            N = "Selling Price"

        elif op == 'Profit or Loss %':
            placeholder1 = 'Enter C.P.'
            placeholder2 = 'Enter S.P.'
            M = "Cost Price"
            N = "Selling Price"

        ent1.delete(0,'end')
        ent1.insert(0,placeholder1)

        ent2.delete(0,'end')
        ent2.insert(0,placeholder2)
        
        ent1.place(x = 150, y = 115, anchor = CENTER)
        ent2.place(x = 150, y = 155, anchor = CENTER) 
        submit.place(x = 270, y = 135, anchor = CENTER)
        
    Title = Label(win, text = "Profit Loss Calculator", fg = "blue2", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    Title.place(x = 200, y = 25, anchor = CENTER)

    Ty = ttk.Combobox(win, width = 20, textvariable = n)
    Ty['values'] = ('Cost Price', 
                    'Selling Price',
                    'Profit or Loss', 
                    'Profit or Loss %',)

    Ty.place(x = 200, y = 70, anchor = CENTER)
    Ty.current()
    Ty.set("Select Operation")
    Ty.bind("<<ComboboxSelected>>", sel)

    ent1 = Entry(win, width = 20, textvariable = a, fg = "black")
    ent2 = Entry(win, width = 20, textvariable = b, fg = "black")

    lab = Label(win, text = "", fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))

    global placeholder1
    global placeholder2
    placeholder1 = 'Please enter side'
    def erase_a(event=None):
        if ent1.get() == placeholder1:
            ent1.delete(0,'end')
    def add_a(event=None):
        if ent1.get() == '':
            ent1.insert(0,placeholder1)
    add_a()
    ent1.bind('<FocusIn>',erase_a)
    ent1.bind('<FocusOut>',add_a)

    placeholder2 = 'Please enter 2nd side'
    def erase_b(event=None):
        if ent2.get() == placeholder2:
            ent2.delete(0,'end')
    def add_b(event=None):
        if ent2.get() == '':
            ent2.insert(0,placeholder2)
    add_b()
    ent2.bind('<FocusIn>',erase_b)
    ent2.bind('<FocusOut>',add_b)

    x = Label(win, text = "", fg = "black", bg = "cyan", font = ("Comic Sans MS", 14, "bold"))
    y = Label(win, text = "", fg = "black", bg = "cyan", font = ("Comic Sans MS", 14, "bold"))
    z = Label(win, text = "", fg = "black", bg = "cyan", font = ("Comic Sans MS", 14, "bold"))

    submit = Button(win, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = lambda : Submit(op))
    submit.place(x = 200, y = 120, anchor = CENTER)

    out = Label(win, textvariable = ans, bg = "cyan", font = ("Comic Sans MS", 12, "bold"))    
    
def D():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Tally Marks Calculator")
    global width
    global height
    global dim
    width,height=400,200
    dim = str(width)+'x'+str(height)
    win.geometry(dim)
    win.config(bg = "cyan")
    win.resizable(False, False)

    a = tk.StringVar()
    b = tk.StringVar()
    global stat
    stat = 0
    global x
    x = 1

    dic = {}
    tal = {}

    def Submit():
        global stat
        topic = a.get()
        a.set("")
        if topic == "":
            messagebox.showinfo("No Input!", "Enter the topic!")
        elif topic != "" :   
            submit.place_forget()
            stat = 1
            label_1.config(text = "Enter number of observations")
            entry_1.place_forget()
            entry_2.place(x= 150, y= 120,anchor = CENTER)
            submit.place(x= 250, y= 120,anchor = CENTER)
            submit.config(command = lambda : get_num(topic))

    def get_num(topic):
        global stat
        obs = b.get()
        b.set("")
        try:
            obs = int(obs)
        except ValueError:
            messagebox.showinfo("Invalid Input!", "Enter numerical value only for number of observations!")
        else:
            submit.place_forget()
            print(topic)
            print(obs)
            global x
            Prog(obs, topic, x)

    def Prog(obs, topic, x):
        b.set("")
        global height
        global dim
        global width
        height = 300
        dim = str(width)+'x'+str(height)
        win.geometry(dim)
        if x <= obs:
            num = num2words(x, to = 'ordinal_num')
            label_2.config(text = "Enter "+num+" observation")
            entry_1.config(width = 25)
            entry_1.place(x = 200, y = 110,anchor = CENTER)
            entry_2.config(width = 25)
            entry_2.place(x = 200, y = 200,anchor = CENTER)
            label_1.config(text = "Enter "+topic)
            label_2.place(x = 200, y = 155,anchor = CENTER)
            submit.config(command = lambda : ob_get(x, obs, topic))
            submit.place(x= 200,y= 250, anchor = CENTER)
        else:
            pro(obs, topic)

    def ob_get(x, obs, topic):
        if x <= obs:
            subject = a.get()
            observation = b.get()
            a.set("")
            b.set("")
            try:
                observation = int(observation)
            except ValueError:
                messagebox.showinfo("Invalid Input!", "Enter numerical value only in observation!")
            else:
                x += 1
                dic[subject]=observation
                Prog(obs, topic, x)

    def pro(obs, topic):
        print("")
        print(dic)
        label_1.place_forget()
        entry_1.place_forget()
        label_2.place_forget()
        entry_2.place_forget()
        submit.place_forget()
        tally = ""
        for i in dic.keys():
            print("")
            print(i)
            j = dic[i]
            print(j)
            j - int(j)
            tally = ""
            while j > 0:
                if j % 5 == 0:
                    x = j / 5
                    x = int(x)
                    for y in range(1, x+1):
                        tally = tally + '-||||'
                        j -= 5
                else:
                    x = j % 5
                    x = int(x)
                    for y in range(1, x+1):
                        tally = tally + "|"
                        j -= 1

            tally_m = tally[::-1]
            print(tally_m)
            tal[i] = tally_m
        disp(obs, topic)

    def disp(obs, topic):
        global height
        global dim
        global width
        label_1.config(text = "Tally Marks Table")
        label_1.place(x= 200, y= 70, anchor = CENTER)
        subject = Label(win, text = topic, fg = "red", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
        tally_label = Label(win, text = "Tally Marks", fg = "red", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
        subject.place(x= 120,y= 110,anchor = "e")
        tally_label.place(x= 275,y= 110,anchor = "e")
        Max = 0
        for z in dic.values():
            if z > Max:
                Max = z 
        if Max > 12 :
            t = Max - 17
            t *= 15
            t = round(t, 0)
            t = int(t)
            width = 400 + t
            dim = str(width)+'x'+str(height)
            win.geometry(dim)
            Title.place(x= round(width/2, 0), y= 25, anchor = CENTER)
            label_1.place(x= round(width/2, 0), y= 70, anchor = CENTER)
            tally_label.place(x= round(width/2.85, 0), y= 110, anchor = W)
            subject.place(x= round(width/7.2, 0), y= 110, anchor = W)
            
        if obs > 4 :
            t = obs - 4
            height = 300 + (t*30)
            dim = str(width)+'x'+str(height)
            win.geometry(dim)
            
        y_var = 160
        for i in tal.keys():
            sub = Label(win, text = i, fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
            tall = Label(win, text = tal[i], fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
            if Max > 12:
                sub.place(x= round(width/7.2, 0),y= y_var,anchor = W)
                tall.place(x= round(width/2.85, 0),y= y_var,anchor = W)
            else :
                sub.place(x= 120,y= y_var,anchor = "e")
                tall.place(x= 275,y= y_var,anchor = "e")
            y_var += 30

    Title = Label(win, text = "Tally Marks Calculator", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 19, "bold"))
    label_1 = Label(win, text = "Enter topic", fg = "blue2", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    label_2 = Label(win, text = "Enter topic", fg = "blue2", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    entry_1 = Entry(win, width= 15, textvariable = a)
    entry_2 = Entry(win, width= 15, textvariable = b)
    submit = Button(win, text = "Submit", fg = "white", bg = "black", font = ("Comic Sans MS", 12, "bold"), command = Submit)

    Title.place(x= 200, y= 25,anchor = CENTER)
    entry_1.place(x= 150, y= 120,anchor = CENTER)
    submit.place(x= 250, y= 120,anchor = CENTER)
    label_1.place(x= 200, y= 70, anchor = CENTER)
    
def E():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Data Handling")
    global width
    global height
    global dim
    width,height=400,200
    dim = str(width)+'x'+str(height)
    win.geometry(dim)
    win.config(bg = "cyan")
    win.resizable(False, False)
    a= tk.StringVar()
    List = []
    Dic = {}
    num = []
    freq_lis = []
    global x
    x = 1

    def Submit():
        global stat
        obs = a.get()
        a.set("")
        if obs == "":
            messagebox.showinfo("No Input!", "Enter the topic!")
        elif obs != "" :   
            try:
                obs = int(obs)
            except ValueError:
                messagebox.showinfo("Invalid Input!", "Enter numerical value only for number of observations!")
            else:
                print(str(obs)+"\n")
                global x
                Prog(obs, x)

    def Prog(obs, x):
        if x <= obs:
            if x == 1:
                pos = "st"
                
            elif x == 2:
                pos = "nd"
                
            elif x == 3:
                pos = "rd"

            elif x >= 4:
                pos = "th"

            label_1.config(text = "Enter "+str(x)+pos+" observation")
            submit.config(command = lambda : ob_get(x, obs))
        else:
            pro(obs)

    def ob_get(x, obs):
        if x <= obs:
            observation = a.get()
            a.set("")
            try:
                observation = int(observation)
            except ValueError:
                messagebox.showinfo("Invalid Input!", "Enter numerical value only in observation!")
            else:
                print(observation)
                x += 1
                if observation in num:
                    y = num.index(observation)
                    z = freq_lis[y]
                    freq_lis[y] = z + 1
                else:
                    freq_lis.append(1)
                    num.append(observation)
                List.append(observation)
                Prog(obs, x)

    def pro(obs):
        #Screen change
        entry_1.place_forget()
        submit.place_forget()
        label_1.config(text = "The central tendencies")
        List.sort()

        #Assigning vars
        mean = 0
        median = 0
        mode = 0
        Range = 0
        high = 0 
        low = 0
        Sum = 0

        # Resizing window
        global width
        global height
        global dim
        width,height=400,350
        dim = str(width)+'x'+str(height)
        win.geometry(dim)

        # Mean
        for i in List:
            Sum += i
            
        mean = Sum/obs

        # Median
        if obs % 2 == 0:
            A = obs/2
            B = (obs/2)+1
            A = int(A)
            A -= 1
            B = int(B)
            B -= 1
            median = (List[A]+List[B])/2
        elif obs % 2 == 1:
            A = (obs+1)/2
            A = int(A)
            A -= 1
            median = List[A]

        # Range, Highest, Lowest
        for h in List:
            if h > high :
                high = h
                
        low = high
        for j in List:
            if j < low :
                low = j

        Range = high - low

        # Mode, Most and least frequency
        Hi = 0
        Lo = obs
        for j in freq_lis:
            if j > Hi:
                Hi = j
            if j < Lo:
                Lo = j

        Modes = ""
        print("")
        while Hi in freq_lis:
            pos_mode = freq_lis.index(Hi)
            freq_lis.remove(Hi)
            Mode = num[pos_mode]
            num.remove(Mode)
            if Modes == "":
                count_mode = 1
                Modes = Modes + str(Mode)
            else:
                count_mode += 1
                Modes = Modes + ", " + str(Mode)

        # Output
        print("Mean = "+str(mean))
        print("Median = "+str(median))
        print("Mode = "+str(Modes))
        print("Highest observation = "+str(high))
        print("Lowest observation = "+str(low))
        print("Range = "+str(Range))
        print("Highest frequency = "+str(Hi))
        print("Lowest frequency = "+str(Lo))
        
        label_a = Label(win, text = "Mean = "+str(mean), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_a.place(x= 200, y= 110, anchor = CENTER)
        
        label_b = Label(win, text = "Median = "+str(median), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_b.place(x= 200, y= 140, anchor = CENTER)

        label_c = Label(win, text = "Mode(s) = "+str(Modes), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_c.place(x= 200, y= 170, anchor = CENTER)

        label_d = Label(win, text = "Range = "+str(Range), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_d.place(x= 200, y= 200, anchor = CENTER)

        label_e = Label(win, text = "Highest observation = "+str(high), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_e.place(x= 200, y= 230, anchor = CENTER)

        label_f = Label(win, text = "Lowest observation = "+str(low), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_f.place(x= 200, y= 260, anchor = CENTER)

        label_g = Label(win, text = "Highest frequency = "+str(Hi), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_g.place(x= 200, y= 290, anchor = CENTER)

        label_h = Label(win, text = "Lowest frequency = "+str(Lo), fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
        label_h.place(x= 200, y= 320, anchor = CENTER)

    Title = Label(win, text = "Number tendencies", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 19, "bold"))
    label_1 = Label(win, text = "Enter number of observations", fg = "blue2", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    entry_1 = Entry(win, width= 15, textvariable = a)
    submit = Button(win, text = "Submit", fg = "white", bg = "black", font = ("Comic Sans MS", 12, "bold"), command = Submit)

    Title.place(x= 200, y= 25,anchor = CENTER)
    entry_1.place(x= 150, y= 120,anchor = CENTER)
    submit.place(x= 250, y= 120,anchor = CENTER)
    label_1.place(x= 200, y= 70, anchor = CENTER)

def F():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Factorial")
    win.geometry("400x200")
    win.config(bg = "cyan")
    win.resizable(False, False)

    num = tk.StringVar()
    ans=tk.StringVar()

    def Submit():
        Pro = 1
        ans.set("")
        A = num.get()
        try:
            A = int(A)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter integars only")
        else:
            print(A)
            for i in range(1, A+1):
                Pro = Pro * i
            ans.set("Factorial of " + str(A) + " is " + str(Pro))
            
    Title = Label(win, text = "Factorial", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    Title.place(x = 200, y = 25, anchor = CENTER)

    label_1 = Label(win, text = "Enter Number", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    label_1.place(x = 200, y = 70, anchor = CENTER)

    entry = Entry(win, width = 20, textvariable = num, fg = "blue3")
    entry.place(x = 140, y = 115, anchor = CENTER)

    submit = Button(win, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = Submit)
    submit.place(x = 260, y = 115, anchor = CENTER)

    out = Label(win, textvariable = ans, bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
    out.place(x = 200, y = 160, anchor = CENTER)

def G():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Interest Calculator")
    win.geometry("400x200")
    win.config(bg = "cyan")
    win.resizable(False, False)

    n = tk.StringVar()
    Cur = tk.StringVar()
    Pa = tk.StringVar()
    Ri = tk.StringVar()
    Ti = tk.StringVar()
    Cr = tk.StringVar()
    ANS = tk.StringVar()
    ans = tk.StringVar()

    def sel(event):
        global ty
        ty = event.widget.get()
        
    def Submit(ty):
        cur = Cur.get()
        if cur == "Please enter Currency":
            messagebox.showerror("No currency entered", "Please enter transaction currency")
        else:
            print("\nCurrency is " + str(cur))
            print(ty)
            Title.config(text = ty + " Calculator")
            Ty.place_forget()
            label_1.config(textvariable = ans)
            ans.set("Enter principal amount")
            submit.config(command = lambda : get_pa(ty, cur))
            entry.place_forget()
            entry_2.place(x = 140, y = 115, anchor = CENTER)
            entry_2.config(textvariable = Pa)
            submit.place(x = 260, y = 115, anchor = CENTER)

    def get_pa(ty, cur):
        P = Pa.get()
        try:
            P = float(P)
        except ValueError:
            messagebox.showerror("Invalid Input!", "Enter numerical value only")
        else:        
            ans.set("Enter Rate of Interest")
            submit.config(command = lambda : get_ri(ty, cur, P))
            entry_2.place(x = 140, y = 115, anchor = CENTER)
            entry_2.config(textvariable = Ri)
            submit.place(x = 260, y = 115, anchor = CENTER)

    def get_ri(ty, cur, P):
        R = Ri.get()
        try:
            R = float(R)
        except ValueError:
            messagebox.showerror("Invalid Input!", "Enter numerical value only")
        else:
            ans.set("Enter Time(in years)")
            submit.config(command = lambda : get_ti(ty, cur, P, R))
            entry_2.place(x = 140, y = 115, anchor = CENTER)
            entry_2.config(textvariable = Ti)
            submit.place(x = 260, y = 115, anchor = CENTER)

    def get_ti(ty, cur, P, R):
        T = Ti.get()
        try:
            T = float(T)
        except ValueError:
            messagebox.showerror("Invalid Input!", "Enter numerical value only")
        else:
            if ty == "Compound Interest":
                ans.set("Enter Compound Freq. per year")
                submit.config(command = lambda : get_cr(ty, cur, P, R, T))
                entry_2.place(x = 140, y = 115, anchor = CENTER)
                entry_2.config(textvariable = Cr)
                submit.place(x = 260, y = 115, anchor = CENTER)
            else:
                si(ty, cur, P, R, T)

    def get_cr(ty, cur, P, R, T):
        N = Cr.get()
        try:
            N = float(N)
        except ValueError:
            messagebox.showerror("Invalid Input!", "Enter numerical value only")
        else:
            ci(ty, cur, P, R, T, N)

    def si(ty, cur, P, R, T):
        submit.place_forget()
        entry.place_forget()
        entry_2.place_forget()
        label_1.config(textvariable = ans)
        label_1.config(font = ("Comic Sans MS", 12, "bold"))
        label_1.place(x = 200, y = 80, anchor = CENTER)
        label_2.place(x = 200, y = 110, anchor = CENTER)
        SI = (P * R * T)/100
        SI = round(SI, 2)
        ans.set("Simple Interest = "+cur+str(SI))
        ANS.set("Amount = "+cur+str(round(SI+P, 2)))
        ret.place(x = 200, y = 160, anchor = CENTER)

    def ci(ty, cur, P, R, T, N):
        submit.place_forget()
        entry.place_forget()
        entry_2.place_forget()
        label_1.config(textvariable = ans)
        label_1.config(font = ("Comic Sans MS", 12, "bold"))
        label_1.place(x = 200, y = 80, anchor = CENTER)
        label_2.place(x = 200, y = 110, anchor = CENTER)
        CI = P * ((1+(R)/(100*N))**(N*T))
        CI -= P
        CI = round(CI, 2)
        ans.set("Compound Interest = "+cur+str(CI))
        ANS.set("Amount = "+cur+str(round(CI+P, 2)))
        ret.place(x = 200, y = 160, anchor = CENTER)
        

    def again():
        n.set("")
        Cur.set("")
        Pa.set("")
        Ri.set("")
        Ti.set("")
        Cr.set("")
        ANS.set("")
        ans.set("")
        
        ret.place_forget()
        label_1.config(font = ("Comic Sans MS", 15, "bold"))
        label_2.place_forget()
        placeholder = 'Please enter Currency'

        entry.place(x = 140, y = 155, anchor = CENTER)

        def erase(event=None):
            if entry.get() == placeholder:
                entry.delete(0,'end')
        def add(event=None):
            if entry.get() == '':
                entry.insert(0,placeholder)

        add()
        entry.bind('<FocusIn>',erase)
        entry.bind('<FocusOut>',add)

        ans.set("Select Interest")
        label_1.place(x = 200, y = 70, anchor = CENTER)

        Ty.place(x = 200, y = 110, anchor = CENTER)

        submit.config(command = lambda : Submit(ty))
        submit.place(x = 260, y = 155, anchor = CENTER)

    Title = Label(win, text = "Interest Calculator", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    Title.place(x = 200, y = 30, anchor = CENTER)

    placeholder = 'Please enter Currency'

    entry = Entry(win, width = 20, textvariable = Cur)
    entry_2 = Entry(win, width = 20, text = "")
    entry.place(x = 140, y = 155, anchor = CENTER)

    def erase(event=None):
        if entry.get() == placeholder:
            entry.delete(0,'end')
    def add(event=None):
        if entry.get() == '':
            entry.insert(0,placeholder)

    add()
    entry.bind('<FocusIn>',erase)
    entry.bind('<FocusOut>',add)

    label_1 = Label(win, text = "Select Interest", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    label_1.place(x = 200, y = 70, anchor = CENTER)

    label_2 = Label(win, textvariable = ANS, fg = "blue", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))

    Ty = ttk.Combobox(win, width = 20, textvariable = n)
    Ty['values'] = ('Simple Interest', 
                    'Compound Interest')

    Ty.place(x = 200, y = 110, anchor = CENTER)
    Ty.current()
    Ty.bind("<<ComboboxSelected>>", sel)

    submit = Button(win, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = lambda : Submit(ty))
    submit.place(x = 260, y = 155, anchor = CENTER)

    ret = Button(win, text = "Use again", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = again)
    
def H():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Number system convertor")
    win.geometry("350x290")
    win.config(bg = "cyan")
    win.resizable(False, False)

    Bina = 0
    Deca = 0
    Octa = 0
    Hexa = ""

    global Dec
    global Bin
    global Oct
    global Hex

    Bin = ""
    Dec = ""
    Oct = ""
    Hex = ""

    put = ""


    a=tk.StringVar()
    global A
    put = ""
    A = ""

    def h():
        global x
        if x == 10:
            x = ""
            x = "A"

        if x == 11:
            x = ""
            x = "B"
            
        if x == 12:
            x = ""
            x = "C"
            
        if x == 13:
            x = ""
            x = "D"
            
        if x == 14:
            x = ""
            x = "E"
            
        if x == 15:
            x = ""
            x = "F"

    def get_data():
        global n
        n = 0
        Bin = ""
        Dec = ""
        Oct = ""
        Hex = ""

        global Deca
        global Bina
        global Octa
        global Hexa
        
        Bina = 0
        Deca = 0
        Octa = 0
        Hexa = 0
        
        A = a.get()
        A = str(A)
        print("")
        print(A)
        Check(A)

    def origin(event):
        global fro
        fro = event.widget.get()
        

    def desired(event):
        global to
        to = event.widget.get()

    def Check(A) :
        #Decimal to others
        print(fro)
        print(to)
        global y
        y = ""
        if fro == to :
            put = ""
            out.set(put)
            messagebox.showinfo("Invalid Conversion selected", "You have entered origin and destination number system the same!")
        else :
            if fro == "Decimal" or fro == "Binary" or fro == "Octal" :
                try:
                    A = int(A)
                except:
                    put = ""
                    out.set(put)
                    messagebox.showinfo("Invalid Input", "Enter Integars only for type conversion!")
                else:
                    A = str(A)
                    lim = 9
                    
                    #Decimal to others
                    if fro == "Decimal" and to == "Binary":
                        DB(A)
                        global Bin
                        put = "Equivalent " + to + " Value = " + "(" + Bin + ")" + "2"
                        out.set(put)

                    elif fro == "Decimal" and to == "Octal" :                    
                        DO(A)
                        global Oct
                        put = "Equivalent " + to + " Value = " + "(" + Oct + ")" + "8"
                        out.set(put)
                        
                    elif fro == "Decimal" and to == "Hexadecimal" :
                        DH(A)
                        global Hex
                        put = "Equivalent " + to + " Value = " + "(" + Hex + ")" + "16"
                        out.set(put)
                
                    #Binary to others
                    elif fro == "Binary" and to == "Decimal" :
                        BD(A)
                        global Dec
                        global n
                        if n == 0:
                            put = "Equivalent " + to + " Value = " + "(" + Dec + ")" + "10"
                            out.set(put)
                        else :
                            out.set("")
                        
                    elif fro == "Binary" and to == "Octal" :
                        BO(A)

                    elif fro == "Binary" and to == "Hexadecimal" :
                        BH(A)

                    #Octal to others
                    
                    elif fro == "Octal" and to == "Binary" :
                        OB(A)

                    elif fro == "Octal" and to == "Decimal" :
                        OD(A)
                        if n == 0:
                            put = "Equivalent " + to + " Value = " + "(" + Dec + ")" + "10"
                            out.set(put)
                        else :
                            out.set("")
                        
                    elif fro == "Octal" and to == "Hexadecimal" :
                        OH(A)

            #Hexadecimal to others
            if fro == "Hexadecimal":
                if fro == "Hexadecimal" and to == "Binary" :
                    HB(A)

                elif fro == "Hexadecimal" and to == "Decimal" :
                    HD(A)
                    if n == 0:
                        put = "Equivalent " + to + " Value = " + "(" + Dec + ")" + "10"
                        out.set(put)
                    else :
                        out.set("")
                    
                elif fro == "Hexadecimal" and to == "Octal" :
                    HO(A)



    # Decimal to others
    def DB(A):
        global Deca
        global Bin
        Deca = A
        Deca = int(Deca) 
        x = 0
        while Deca > 0 :
            x = Deca % 2
            global y
            y = y + str(x)
            Deca = Deca // 2
        Bin = ""
        Bin = y[::-1]
        
    def DO(A):
        global Deca
        global Oct
        Deca = A
        Deca = int(Deca)
        x = 0
        while Deca > 0 :
            x = Deca % 8
            global y
            y = y + str(x)
            Deca = Deca // 8
        Oct = ""
        Oct = y[::-1]

    def DH(A):
        global Deca
        global Hex
        Deca = A
        Deca = int(Deca)
        global x
        x = 0
        while Deca > 0 :
            x = Deca % 16
            if x >= 10:
                h()
            global y
            y = y + str(x)
            Deca = Deca // 16
        Hex = ""
        Hex = y[::-1]


    # Others to Decimal
    def BD(A):
        Bina = A
        Bina = int(Bina)
        global Dec
        global n
        o = 0
        x = 0
        y = -1
        z = 0
        n = 0
        while Bina > 0 :
            y += 1
            x = Bina % 10
            if n == 0:
                if x <= 1 and x >= 0:
                    z = 2 ** y
                    z *= x
                    o += z 
                else :
                    n = 1
                    put = ""
                    out.set(put)
                    messagebox.showinfo("Invalid Input", "Enter 0 and 1 only for type conversion!")
            Bina = Bina // 10
                
        Dec = str(o)

    def OD(A):
        Octa = A
        Octa = int(Octa)
        global Dec
        global n
        o = 0
        x = 0
        y = -1
        z = 0
        n = 0
        while Octa > 0 :
            y += 1
            x = Octa % 10
            if x <= 7 and x >= 0:
                if n == 0:
                    z = 8 ** y
                    z *= x
                    o += z 
            else :
                n = 1
                put = ""
                out.set(put)
                messagebox.showinfo("Invalid Input", "Enter Integars from 0 to 7 only for type conversion!")

            Octa = Octa // 10
                
        Dec = str(o)

    def HD(A):
        Hexa = A
        global Dec
        h = 0
        global hd
        hd = 0
        x = 0
        y = -1
        z = 0
        global n
        n = 0
        charlen = len(Hexa)
        charlen -= 1
        while charlen >= 0 :
            if n == 0:  
                y += 1
                hd = Hexa[charlen]
                
                if hd >= '0' and hd <= '9':
                    hd = int(hd)
                    
                elif hd >= 'A' and hd <= 'F':
                    hd = ord(hd)
                    hd = hd - 55
                    
                elif hd >= 'a' and hd <= 'f':
                    hd = ord(hd)
                    hd = hd - 87

                else :
                    n = 1
                    put = ""
                    out.set(put)
                    messagebox.showinfo("Invalid Input", "Enter Integars and Alphabets from A to F only for type conversion!")                

            charlen -= 1
            if n == 0:   
                z = 16 ** y
                z *= hd
                h += z
            
        Dec = str(h)

    # Octal, Hexadecimal to Binary
    def OB(A):
        global Dec
        global Deca
        global n
        OD(A)
        A = Dec
        DB(A)
        global Bin
        if n == 0:
            put = "Equivalent " + to + " Value = " + "(" + Bin + ")" + "2"
            out.set(put)
        else :
            out.set("")
            
    def HB(A):
        global Dec
        global Deca
        global n
        HD(A)
        A = Dec
        DB(A)
        global Bin
        if n == 0:
            put = "Equivalent " + to + " Value = " + "(" + Bin + ")" + "2"
            out.set(put)
        else :
            out.set("")

    # Binary, Hexadecimal to Octal
    def BO(A):
        global Dec
        global Deca
        global n
        BD(A)
        A = Dec
        DO(A)
        global Oct
        if n == 0:
            put = "Equivalent " + to + " Value = " + "(" + Oct + ")" + "8"
            out.set(put)
        else :
            out.set("")

    def HO(A):
        global Dec
        global Deca
        global n
        HD(A)
        A = Dec
        DO(A)
        global Oct
        if n == 0:
            put = "Equivalent " + to + " Value = " + "(" + Oct + ")" + "8"
            out.set(put)
        else :
            out.set("")

     # Octal, Binary to Hexadecimal
    def OH(A):
        global Dec
        global Deca
        global n
        OD(A)
        A = Dec
        DH(A)
        global Hex
        if n == 0:
            put = "Equivalent " + to + " Value = " + "(" + Hex + ")" + "16"
            out.set(put)
        else :
            out.set("")

    def BH(A):
        global Dec
        global Deca
        global n
        BD(A)
        A = Dec
        DH(A)
        global Hex
        if n == 0:
            put = "Equivalent " + to + " Value = " + "(" + Hex + ")" + "16"
            out.set(put)
            print(out.get())
        else :
            out.set("")


    # Entry, Label and Button creation
    entry = Entry(win, width= 15, textvariable = a)
    entry.place(x=250,y=170, anchor= CENTER)

    out = tk.StringVar()
    out.set("")

    label_1 = Label(win, text = "Number system converter", font=("Comic Sans MS", 16, "bold"))
    label_1.config(fg= "blue", bg = "cyan")

    label_4 = Label(win, text = "Enter origin number", font=("Comic Sans MS", 11, "bold"))
    label_4.config(fg= "black", bg = "cyan")

    label_5 = Label(win, textvariable = out, font=("Comic Sans MS", 10, "bold"))
    label_5.config(fg= "black", bg = "cyan")

    label_1.place(x=173,y=25, anchor= CENTER)
    label_4.place(x=100, y=170, anchor= CENTER)
    label_5.place(x=173, y=255, anchor= CENTER)

    button = Button(win, text= "Click to Show", bg = "blue3", fg = "white", font = ("Comic Sans MS", 10, "bold"), command= get_data).place(x=115, y=200)

    # Combobox creation
    n = tk.StringVar()
    m = tk.StringVar()

    fromchoosen = ttk.Combobox(win, width = 20, textvariable = n)
    tochoosen = ttk.Combobox(win, width = 20, textvariable = m)
      
    # Adding combobox 'from' drop down list
    fromchoosen['values'] = ('Decimal', 
                             'Binary',
                             'Octal',
                             'Hexadecimal')

    fromchoosen.place(x = 80, y = 70)
    fromchoosen.current()
    fromchoosen.set("Origin No. system")
    fromchoosen.bind("<<ComboboxSelected>>", origin)

    # Adding combobox 'to' drop down list
    tochoosen['values'] = ('Decimal', 
                           'Binary',
                           'Octal',
                           'Hexadecimal')

    tochoosen.place(x = 80, y = 120)
    tochoosen.current()
    tochoosen.set("Desired No. system")
    tochoosen.bind("<<ComboboxSelected>>", desired)

    win.mainloop()

def J():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Value Changer")
    win.geometry("400x180")
    win.config(bg = "cyan")
    win.resizable(False, False)

    num1 = tk.StringVar()
    num2 = tk.StringVar()
    ans=tk.StringVar()

    def Submit():
        ans.set("")
        A = num1.get()
        B = num2.get()
        try:
            A = int(A)
            B = int(B)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter integars only")
        else:
            print("A = " + str(A))
            print("B = " + str(B)+"\n")
            A, B = B, A
            print("A = " + str(A))
            print("B = " + str(B)+"\n")
            
            win.geometry("400x210")
            ans.set("Now A = " + str(A) + " and B = " + str(B))
            
    Title = Label(win, text = "Value Changer", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    Title.place(x = 200, y = 25, anchor = CENTER)

    label_1 = Label(win, text = "Enter Numbers", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    label_1.place(x = 200, y = 67, anchor = CENTER)

    label_a = Label(win, text = "A", fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
    label_a.place(x = 100, y = 105, anchor = CENTER)

    label_b = Label(win, text = "B", fg = "black", bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
    label_b.place(x = 100, y = 135, anchor = CENTER)

    entry1 = Entry(win, width = 17, textvariable = num1, fg = "blue3")
    entry1.place(x = 170, y = 105, anchor = CENTER)

    entry2 = Entry(win, width = 17, textvariable = num2, fg = "blue3")
    entry2.place(x = 170, y = 135, anchor = CENTER)

    submit = Button(win, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = Submit)
    submit.place(x = 275, y = 120, anchor = CENTER)

    out = Label(win, textvariable = ans, bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
    out.place(x = 200, y = 180, anchor = CENTER)

def K():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Number to Name Convertor")
    win.geometry("400x200")
    win.config(bg = "cyan")
    win.resizable(False, False)

    num = tk.StringVar()
    ans = tk.StringVar()

    def Submit():
        ans.set("")
        A = num.get()
        try:
            A = int(A)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter integars only")
        else:
            print(A)
            print(num2words(A)) # Number Name
            print(num2words(A, to = 'ordinal')) # Alpha position
            print(num2words(A, to = 'ordinal_num')) # Numeric Position
            print(num2words(A, to = 'currency')) # Currency
            print(num2words(A, lang ='fr')) # Number name in French
            print("")
            name = num2words(A)
            ans.set("Number name of "+str(A)+" is "+name)

    Title = Label(win, text = "Number to Number Name", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    Title.place(x = 200, y = 25, anchor = CENTER)

    label_1 = Label(win, text = "Enter Number", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    label_1.place(x = 200, y = 70, anchor = CENTER)

    entry = Entry(win, width = 20, textvariable = num, fg = "blue3")
    entry.place(x = 140, y = 115, anchor = CENTER)

    ans.set("")
    submit = Button(win, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = Submit)
    submit.place(x = 260, y = 115, anchor = CENTER)

    out = Label(win, textvariable = ans, bg = "cyan", font = ("Comic Sans MS", 11, "bold"), wraplength = 300, justify = "center")
    out.place(x = 200, y = 160, anchor = CENTER)

def N():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Anglo-Francais Translator")
    win.geometry("400x200")
    win.config(bg = "cyan")
    win.resizable(False, False)

    Dict = {"Hello":"Bonjour", "Good Morning":"Bonjour", "Good Afternoon":"Bon Apres-Midi", "Good Evening":"Bonsoir",
        "Good Night":"Bonne nuit", "Hi":"Salut", "Bye":"Au Revoir", "Please":"S'ill vous plait", "Thank you":"Merci",
        "Sorry":"Desole", "How are you":"Comment allez vous", "School":"Ecole", "See you soon":"A Bientot",
        "See you tommorow":"A Demain", "Mother":"Mere", "Father":"Pere", "Brother":"Frere", "Sister":"Soeur"}
    
    List = []
    for j in Dict.keys():
        List.append(j)

    List.sort()
        
    t = tk.StringVar()
    ans = tk.StringVar()

    var = tk.Variable(value=List)

    a = 0
    def empty():
        ent.delete(0, 'end')
        ans.set("")
        
    def checkkey(event):
        a = 0
        value = event.widget.get()
          
        if value == '':
            data = List
        else:
            z = 1
            data = []
            for item in List:
                z = 1
                b = item.lower()
                d = value.lower()
                ch = len(value)
                t = len(b)
                if t < ch:
                    ch = t
                for i in range(0, ch):
                    if d[i] in b[i]:
                        m = 0
                    else :
                        z = 0

                if z == 1:
                    a += 1
                    print(a)
                    if item not in data:
                        data.append(item)
                else:
                    a = 0
       
        update(data)
        lb.place(x= 220, y= 87, anchor = "n")
        if a <= 6 :
            lb.config(height = a)
            
        else:
            lb.config(height = 6)
        
    def update(data):
        lb.delete(0, 'end')
        for item in data:
            lb.insert('end', item)

    def items_selected(event):
        ind = lb.curselection()
        lb.place_forget()
        Item = ",".join([lb.get(i) for i in ind])
        ent.delete(0,"end")
        ent.insert(0, Item)
        c = 0
        for n in Dict:
            if n == Item:
                print(Dict[Item])
                ans.set(Dict[Item])
                c = 1
        if c == 0:
            print("Sorry")
            ans.set("Sorry")

    title = Label(win, text = "Eng to French Traslator", fg = "blue2", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    title.place(x= 200, y= 25, anchor = CENTER)

    eng = Label(win, text = "Eng", fg = "black", bg = "cyan", font = ("Comic Sans MS", 14, "bold"))
    eng.place(x= 100, y= 75, anchor = CENTER)

    fre = Label(win, text = "Fre", fg = "black", bg = "cyan", font = ("Comic Sans MS", 14, "bold"), justify = "left")
    fre.place(x= 100, y= 140, anchor = CENTER)

    dis = Label(win, textvariable = ans, bg = "white", width = 20, font = ("Comic Sans MS", 10, "bold"))
    dis.place(x= 220, y= 140, anchor = CENTER)

    ent = Entry(win, width = 20, font = ("Comic Sans MS", 10, "bold"))
    ent.place(x= 220, y= 75, anchor = CENTER)
    ent.bind('<KeyRelease>', checkkey)

    lb = tk.Listbox(win, listvariable=var, height=6, selectmode=tk.EXTENDED)
    lb.bind('<<ListboxSelect>>', items_selected)

    cle = Button(win, text = " C ", fg = "white", bg = "blue2", font = ("Comic Sans MS", 8, "bold"), command = empty, borderwidth=0)
    cle.place(x= 290, y= 75, anchor = CENTER)
    win.mainloop()

def O():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Geometry")
    win.geometry("400x200")
    win.config(bg = "cyan")
    win.resizable(False, False)

    Ans = tk.StringVar()
    n = tk.StringVar()
    m = tk.StringVar()

    a = tk.StringVar()
    b = tk.StringVar()
    c = tk.StringVar()

    ans = 0
    peri = 0
    area = 0
    def r():
        print("")
        ans = 0
        peri = 0
        area = 0
        A = 0
        B = 0
        C = 0
        n.set("")
        m.set("")
        a.set("")
        b.set("")
        c.set("")
        Ans.set("")
        opt.config(text = "Unit is cm")
        dis.config(text = "")
        submit.config(command = lambda : Submit(ty, sh))
        win.geometry("400x200")
        ent1.place_forget()
        ent2.place_forget()
        ent3.place_forget()
        Ty.place(x = 200, y = 70, anchor = CENTER)
        Ty.set("Select Operation")
        Sh.place(x = 200, y = 110, anchor = CENTER)
        Sh.set("Select Shape")
        ch.place_forget()
        submit.place(x = 200, y = 155, anchor = CENTER)
        opt.place_forget()
        
    def go(ty, sh):
        global Y
        A = 0
        B = 0
        C = 0
        global ans
        A = a.get()
        if sh == "Rectangle" or sh == "Cylinder" or sh == "Right-angled Triangle":
            B = b.get()
        elif sh == "Normal Triangle" :
            B = b.get() 
            C = c.get()
        try:
            A = int(A)
            B = int(B)
            C = int(C)
        except ValueError:
            messagebox.showerror("Invalid Input!", "Enter integars only")
        else:
            if sh == "Square":
                print("Side = " + str(A))
                peri = A * 4
                area = A * A
                if ty == "Perimeter":
                    ans = peri
                elif ty == "Area":
                    ans = area

            elif sh == "Rectangle":
                print("Length = " + str(A))
                print("Height = " + str(B))
                peri = 2*(A+B)
                area = A * B
                if ty == "Perimeter":
                    ans = peri
                elif ty == "Area":
                    ans = area

            elif sh == "Right-angled Triangle":
                C = (A*A) + (B*B)
                C = math.sqrt(C)
                peri = A + B + C
                area = A * B
                peri = round(peri, 3)
                area = round(area, 3)
                if ty == "Perimeter":
                    ans = peri
                    print("Height = " + str(B))
                elif ty == "Area":
                    ans = area
                    print("Perp. = " + str(B))
                print("Base = " + str(A))

            elif sh == "Normal Triangle":
                peri = A + B + C
                s = peri/2
                area = s*(s-A)*(s-B)*(s-C)
                area = math.sqrt(area)
                area = round(area, 3)
                if ty == "Perimeter":
                    ans = peri
                elif ty == "Area":
                    ans = area
                print("Side A = " + str(A))
                print("Side B = " + str(B))
                print("Side C = " + str(C))

            elif sh == "Circle":
                peri = 2 * A * 22/7
                area = A * A * 22/7
                peri = round(peri, 3)
                area = round(area, 3)
                if ty == "Perimeter":
                    ans = peri
                elif ty == "Area":
                    ans = area
                print("Radius = " + str(A))

            elif sh == "Cylinder":
                peri = 2 * A * 22/7 * B
                area = A * A * 22/7 * B
                peri = round(peri, 3)
                area = round(area, 3)
                if ty == "Perimeter":
                    ans = peri
                elif ty == "Area":
                    ans = area
                print("Radius = " + str(A))
                print("Height = " + str(B))

            opt.config(text = (ty + " of " + sh)) 
            Ans.set(str(ans)+" cm")
            print(ty + " of this " + sh + " = " + str(ans))
            ch.place(x = 340, y = 80, anchor = CENTER)
            dis.place(x = 300, y = Y, anchor = CENTER)
            opt.place(x = 90, y = Y, anchor = CENTER)

    def Submit(ty, sh):
        global Y
        opt.place(x = 90, y = 155, anchor = CENTER)
        print(ty)
        print(sh)
        global peri
        global area
        global placeholder1
        global placeholder2
        global placeholder3
        Ty.place_forget()
        Sh.place_forget()
        ent1.place(x = 200, y = 70, anchor = CENTER)

        if sh == "Square":
            win.geometry("400x160")
            submit.place(x = 200, y = 115, anchor = CENTER)
            opt.place(x = 93, y = 115, anchor = CENTER)
            dis.place(x = 300, y = 115, anchor = CENTER)
            Y = 115
            
        elif sh == "Rectangle":
            ent1.delete(0,'end')
            placeholder1 = 'Please enter length'
            ent1.insert(0,placeholder1)
            ent2.delete(0,'end')
            placeholder2 = 'Please enter breadth'
            ent2.insert(0,placeholder2)
            ent2.place(x = 200, y = 110, anchor = CENTER)
            Y = 155
                
        elif sh == "Right-angled Triangle":
            if ty == "Perimeter":
                placeholder1 = 'Please enter perp.'            
            elif ty == "Area":
                placeholder1 = 'Please enter height'

            placeholder2 = 'Please enter base'    
            ent1.delete(0,'end')
            ent1.insert(0,placeholder1)
            ent2.delete(0,'end')
            ent2.insert(0,placeholder2)
            ent2.place(x = 200, y = 110, anchor = CENTER)
            Y = 155

        elif sh == "Normal Triangle":
            win.geometry("400x250")
            submit.place(x = 200, y = 205, anchor = CENTER)
            opt.place(x = 93, y = 205, anchor = CENTER)
            dis.place(x = 300, y = 205, anchor = CENTER)

            placeholder1 = 'Please enter side A.'
            placeholder2 = 'Please enter side B.'
            placeholder3 = 'Please enter side C.'                    
            ent1.delete(0,'end')
            ent1.insert(0,placeholder1)
            ent2.delete(0,'end')
            ent2.insert(0,placeholder2)
            ent2.place(x = 200, y = 110, anchor = CENTER)
            ent3.delete(0,'end')
            ent3.insert(0,placeholder3)
            ent3.place(x = 200, y = 150, anchor = CENTER)
            Y = 205
            
        elif sh == "Circle":
            win.geometry("400x160")
            submit.place(x = 200, y = 115, anchor = CENTER)
            opt.place(x = 93, y = 115, anchor = CENTER)
            dis.place(x = 300, y = 115, anchor = CENTER)
            
            placeholder1 = 'Please enter radius.'                    
            ent1.delete(0,'end')
            ent1.insert(0,placeholder1)
            Y = 115

        elif sh == "Cylinder":
            placeholder1 = 'Please enter base radius'
            placeholder2 = 'Please enter height'
            ent1.delete(0,'end')
            ent1.insert(0,placeholder1)
            ent2.delete(0,'end')
            ent2.insert(0,placeholder2)
            ent2.place(x = 200, y = 110, anchor = CENTER)
            Y = 155
            
        submit.config(command = lambda : go(ty, sh))

    def sen(event):
        global ty
        ty = event.widget.get()

    def sem(event):
        global sh
        sh = event.widget.get()

    Title = Label(win, text = "Geometry Assistant", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    Title.place(x = 200, y = 30, anchor = CENTER)

    Ty = ttk.Combobox(win, width = 20, textvariable = n)
    Ty['values'] = ('Perimeter', 
                    'Area')

    Ty.place(x = 200, y = 70, anchor = CENTER)
    Ty.current()
    Ty.set("Select Operation")
    Ty.bind("<<ComboboxSelected>>", sen)

    Sh = ttk.Combobox(win, width = 20, textvariable = m)
    Sh['values'] = ('Square', 
                    'Rectangle',
                    'Right-angled Triangle',
                    'Normal Triangle',
                    'Circle',
                    'Cylinder')

    Sh.place(x = 200, y = 110, anchor = CENTER)
    Sh.current()
    Sh.set("Select Shape")
    Sh.bind("<<ComboboxSelected>>", sem)

    ent1 = Entry(win, textvariable = a, width = 20, font = ("Comic Sans MS", 10, "bold"))
    ent2 = Entry(win, textvariable = b, width = 20, font = ("Comic Sans MS", 10, "bold"))
    ent3 = Entry(win, textvariable = c, width = 20, font = ("Comic Sans MS", 10, "bold"))

    global placeholder1
    global placeholder2
    global placeholder3

    placeholder1 = 'Please enter side'
    def erase_a(event=None):
        if ent1.get() == placeholder1:
            ent1.delete(0,'end')
    def add_a(event=None):
        if ent1.get() == '':
            ent1.insert(0,placeholder1)
    add_a()
    ent1.bind('<FocusIn>',erase_a)
    ent1.bind('<FocusOut>',add_a)

    placeholder2 = 'Please enter 2nd side'
    def erase_b(event=None):
        if ent2.get() == placeholder2:
            ent2.delete(0,'end')
    def add_b(event=None):
        if ent2.get() == '':
            ent2.insert(0,placeholder2)
    add_b()
    ent2.bind('<FocusIn>',erase_b)
    ent2.bind('<FocusOut>',add_b)

    placeholder3 = 'Please enter 3rd side'
    def erase_c(event=None):
        if ent3.get() == placeholder3:
            ent3.delete(0,'end')
    def add_c(event=None):
        if ent3.get() == '':
            ent3.insert(0,placeholder3)
    add_c()
    ent3.bind('<FocusIn>',erase_c)
    ent3.bind('<FocusOut>',add_c)

    opt = Label(win, text = "Unit is cm", wraplength = 120, fg = "black", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))

    dis = Label(win, textvariable = Ans, fg = "black", bg = "cyan", font = ("Comic Sans MS", 13, "bold"))
    dis.place(x = 300, y = 155, anchor = CENTER)

    submit = Button(win, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = lambda : Submit(ty, sh))
    submit.place(x = 200, y = 155, anchor = CENTER)

    ch = Button(win, text = "Reuse", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = r)

def P():
    global newWindow
    global win
    win = Toplevel(newWindow)
    win.title("Number Guessing game")
    win.geometry("400x250")
    win.config(bg = "cyan")
    win.resizable(False, False)
    win.iconphoto(False, tk.PhotoImage(file="globe.png"))

    num = tk.StringVar()
    ans=tk.StringVar()
    r=tk.StringVar()

    global t
    t = 5

    def Guess():
        global x
        global Sum
        x = random.randint(1, 99)
        global evod
        if x % 2 == 0:
            evod = "even"
        else:
            evod = "odd"

        global prote
        fac = 0
        for i in range(1, x+1):
            if x % i == 0:
                fac += 1
        if fac == 2:
            prote = " prime"
        else:
            prote = " composite"

        y = str(x)
        global dig
        a = 0
        b = 0
        if x > 10:
            dig = " 2-digit"
            a = y[0]
            b = y[1]
        else:
            dig = " 1-digit"
            a = y[0]
        Sum = int(a) + int(b) 
            
    Guess()

    def fin():
        global t
        turn = 5 - t
        turn = num2words(turn)
        ans.set("Congratulations!")
        r.set("You won!")
        clue_1.config(text = "You guessed me in " + turn + " turns")
        clue_2.config(text = "The Coder's mystery was hacked by you")
        entry.place_forget()
        out.place_forget()
        submit.config(text = "Play Again")
        submit.config(command = reset)
        submit.place(x = 200, y = 200, anchor = CENTER)
        
    def Submit():
        global x
        ans.set("")
        A = num.get()
        num.set("")
        try:
            A = int(A)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter integars only")
        else:
            print("You entered "+str(A))
            global t
            t -= 1
            r.set("You have " + str(t) + " attempts")
            
            if A < x:
                ans.set("Too Low")
                
            elif A > x:
                ans.set("Too High")
                
            elif A == x:
                fin()

            pro(t)

    def pro(t):
        if t == 0:
            print("")
            end()

    def end():
        global x
        ans.set("")
        r.set("No attempts left!")
        clue_1.config(text = "You could not guess me! Ha Ha Ha")
        clue_2.config(text = "The Coder's mystery number was "+str(x))
        entry.place_forget()
        out.place_forget()
        submit.config(text = "Try Again")
        submit.config(command = reset)
        submit.place(x = 200, y = 200, anchor = CENTER)

    def reset():
        Guess()

        global evod
        global dig
        global Sum
        global t
        
        ans.set("")
        
        t = 5
        r.set("You have " + str(t) + " attempts")
        clue_1.config(text = "I am an " + evod + prote + dig + " number")
        clue_2.config(text = "Sum of my digits is " + str(Sum))
        entry.place(x = 140, y = 185, anchor = CENTER)
        out.place(x = 200, y = 220, anchor = CENTER)
        submit.config(text = "Submit")
        submit.config(command = Submit)
        submit.place(x = 260, y = 185, anchor = CENTER)
               
    Title = Label(win, text = "Guess the Coder's number", fg = "blue", bg = "cyan", font = ("Comic Sans MS", 18, "bold"))
    Title.place(x = 200, y = 25, anchor = CENTER)

    r.set("You have " + str(t) + " attempts")
    rule_1 = Label(win, textvariable = r, fg = "blue", bg = "cyan", font = ("Comic Sans MS", 15, "bold"))
    rule_1.place(x = 200, y = 70, anchor = CENTER)

    global evod
    global dig
    clue_1 = Label(win, text = "I am an " + evod + prote + dig + " number", fg = "black", bg = "cyan", font = ("Comic Sans MS", 14, "bold"))
    clue_1.place(x = 200, y = 105, anchor = CENTER)

    global Sum
    clue_2 = Label(win, text = "Sum of my digits is " + str(Sum), fg = "black", bg = "cyan", font = ("Comic Sans MS", 14, "bold"))
    clue_2.place(x = 200, y = 140, anchor = CENTER)

    entry = Entry(win, width = 20, textvariable = num, fg = "blue3")
    entry.place(x = 140, y = 185, anchor = CENTER)

    submit = Button(win, text = "Submit", fg = "white", bg = "blue3", font = ("Comic Sans MS", 12, "bold"), command = Submit)
    submit.place(x = 260, y = 185, anchor = CENTER)

    out = Label(win, textvariable = ans, bg = "cyan", font = ("Comic Sans MS", 12, "bold"))
    out.place(x = 200, y = 220, anchor = CENTER)
    
#Dashboard
def p():
    global cas
    global l
    l.config(fg = "white")
    pr.set("My Portfolio")
    img = tk.PhotoImage(file=r"Portfolio.png")
    newWindow.img = img
    cas.create_image((0,0), image=img, anchor='nw')
    cas.pack(side = BOTTOM, pady = 20, padx = 20)
    
def c():
    global cas
    global l
    l.config(fg = "white")
    pr.set("Contact Me")
    img = tk.PhotoImage(file=r"Contact1.png")
    newWindow.img = img
    cas.create_image((0,0), image=img, anchor='nw')
    cas.pack(side = BOTTOM, pady = 20, padx = 20)
    

def dab(ab):
    global newWindow
    def da():
        global cas
        global l
        l.config(fg = "white", bg = "black")
        pr.set("Welcome "+ab)
        img = tk.PhotoImage(file=r"Dashboard.png")
        newWindow.img = img
        cas.create_image((0,0), image=img, anchor='nw')
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
    menubar.add_cascade(label ='Projects', menu = proj)

    cals = Menu(proj, tearoff=0)
    cals.add_command(label='Maths', command = A)
    cals.add_command(label='BMI', command = B)
    cals.add_command(label='Profit Loss', command = C)
    cals.add_command(label='Tally Marks', command = D)
    cals.add_command(label='Tendencies', command = E)
    cals.add_command(label='Factorial', command = F)
    cals.add_command(label='Interest', command = G)

    covs = Menu(proj, tearoff=0)
    covs.add_command(label='Number system', command = H)
    covs.add_command(label='Value Changer', command = J)
    covs.add_command(label='Number to Number Name', command = K)


    oths = Menu(proj, tearoff=0)
    oths.add_command(label='Eng to Fre Translator', command = N)
    oths.add_command(label='Geometry', command = O)
    oths.add_command(label='Guess the Number', command = P)

    proj.add_cascade(label ='Calculators', menu=cals, command = None)
    proj.add_cascade(label ='Convertors', menu=covs, command = None)
    proj.add_separator()
    proj.add_cascade(label ='Misc.', menu=oths, command = None)
      
    newWindow.config(menu = menubar)

    global cas
    global l
    
    cas = tk.Canvas(newWindow,width=298,height=168, bg = "black", highlightthickness=3, highlightbackground="black")
    da()
    
def Sig():
    newWindow.destroy()

#Root Widgets
menubar = Menu(root)
  
about = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='About', menu = about)
about.add_command(label ='Porfolio', command = a)
about.add_command(label ='Contact', command = b)
about.add_separator()
about.add_command(label ='Exit', command = root.destroy)
  
user = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='User', menu = user)
user.add_command(label ='Login', command = Log)
user.add_command(label ='Register', command = Reg)
user.add_command(label ='Forgot Password', command = For)

proj = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Features', menu = proj)

cals = Menu(proj, tearoff=0)
cals.add_command(label='Maths', command = aa)
cals.add_command(label='BMI', command = ab)
cals.add_command(label='Profit Loss', command = ac)
cals.add_command(label='Tally Marks', command = ad)
cals.add_command(label='Tendencies', command = ae)
cals.add_command(label='Factorial', command = af)
cals.add_command(label='Interest', command = ag)

covs = Menu(proj, tearoff=0)
covs.add_command(label='Number system', command = ba)
covs.add_command(label='Value Changer', command = bc)
covs.add_command(label='Number to Number Name', command = bd)

oths = Menu(proj, tearoff=0)
oths.add_command(label='Eng to Fre Translator', command = db)
oths.add_command(label='Geometry', command = dc)
oths.add_command(label='Number Guessing Game', command = dd)

proj.add_cascade(label ='Calculators', menu=cals, command = None)
proj.add_cascade(label ='Convertors', menu=covs, command = None)
proj.add_separator()
proj.add_cascade(label ='Misc.', menu=oths, command = None)
  
root.config(menu = menubar)
pro = Label(root, textvariable = project, fg = "white",  bg = "blue", font = ("Comic Sans MS", 20, "bold"))
pro.place(x = 27, y = 28, anchor = W)
canvas = tk.Canvas(root,width=294,height=166, bg = "cyan", highlightthickness=3, highlightbackground="black")

global can
can = tk.Canvas(root,width=350,height=270, bg = "cyan", highlightbackground="white")

two = tk.PhotoImage(file=r'Page.png')
root.two = two
can.create_image((0,0), image=two, anchor='nw')
can.pack(side = BOTTOM, pady = 0, padx = 0)

root.mainloop()
