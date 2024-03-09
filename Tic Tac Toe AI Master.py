from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import sys

root = tk.Tk()
root.title('Tic Tac Toe')
root.geometry("350x400")
root.resizable('False', 'False')
root.config(bg = 'cyan')

global ch
global bh

global win 
win = ''

ch = "X"
bh = "O"

myve = []
moveX = []
moveO = []
for i in range(1, 10):
    myve.append(i)

global stat
stat = 1

global ate
ate = 1

global score
score = 0

#TicTacToe Master:
#https://www.quora.com/Given-all-possible-games-of-Tic-Tac-Toe-which-first-move-is-the-most-likely-to-result-in-victory-for-the-first-player

def check():
    global ch
    global bh
    global stat
    global score
    global win
    win = ''
    if stat == 1:
        for i in moveO:
            for j in moveO:
                for k in moveO:
                    if i == 1 and j == 2 and k == 3:
                        win = 'O'
                    elif i == 4 and j == 5 and k == 6:
                        win = 'O'
                    elif i == 7 and j == 8 and k == 9:
                        win = 'O'

                    elif i == 1 and j == 4 and k == 7:
                        win = 'O'
                    elif i == 2 and j == 5 and k == 8:
                        win = 'O'
                    elif i == 3 and j == 6 and k == 9:
                        win = 'O'

                    elif i == 1 and j == 5 and k == 9:
                        win = 'O'
                    elif i == 3 and j == 5 and k == 7:
                        win = 'O'

        for i in moveX:
            for j in moveX:
                for k in moveX:
                    if i == 1 and j == 2 and k == 3:
                        win = 'X'
                    elif i == 4 and j == 5 and k == 6:
                        win = 'X'
                    elif i == 7 and j == 8 and k == 9:
                        win = 'X'

                    elif i == 1 and j == 4 and k == 7:
                        win = 'X'
                    elif i == 2 and j == 5 and k == 8:
                        win = 'X'
                    elif i == 3 and j == 6 and k == 9:
                        win = 'X'

                    elif i == 1 and j == 5 and k == 9:
                        win = 'X'
                    elif i == 3 and j == 5 and k == 7:
                        win = 'X'

        if win == bh:
            print(bh+' Wins!\nYou Lost! Ha Ha Ha!\nTry again!\n')
            messagebox.showinfo('Game Over!', 'Oh No! Computer Won and you lost!')
            score += 0
            exit()

        elif win == ch:
            print(ch+' Wins!\nCongratulations! \nYou Won!\n')
            messagebox.showinfo('Game Over!', 'Congratulations! You Won!')
            score += 1
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'D:\Outcomes\sample.png')
            messagebox.showerror('You are very strange!', 'I am afraid that I am siting with an alien!! Please call PyCoder@23')
            exit()
def start():
    global ch
    global bh
    print('Welcome to Tic Tac Toe\nThis is a Dangerous AI created by PyCoder23!\nWe hope you enjoy the game & get rid of stress for a moment')
    msg = messagebox.askquestion("Welcome", "You want to play as 'X'?", icon='warning')
    if msg == 'yes':
        ch = 'X'
        bh = 'O'
        print("You are playing as -> 'X' and Computer is -> 'O'\n")
        messagebox.showinfo("Welcome", "You are playing as -> 'X' and Computer is -> 'O'")
    else:
        ch = 'O'
        bh = 'X'
        print("You are playing as -> 'O' and Computer is -> 'X'\n")
        messagebox.showinfo("Welcome", "You are playing as -> 'O' and Computer is -> 'X'")

def sum1():
    global hi
    hi = 'A'
    press()

def sum2():
    global hi
    hi = 'B'
    press()

def sum3():
    global hi
    hi = 'C'
    press()

def sum4():
    global hi
    hi = 'D'
    press()

def sum5():
    global hi
    hi = 'E'
    press()

def sum6():
    global hi
    hi = 'F'
    press()

def sum7():
    global hi
    hi = 'G'
    press()

def sum8():
    global hi
    hi = 'H'
    press()

def sum9():
    global hi
    hi = 'I'
    press()

def res():
    msg = messagebox.askquestion("Welcome Back!", "Do you want to play again?")
    if msg == 'yes':
        global ate
        ate += 1

        global win
        win = ''

        global moveX
        global moveO
        moveX = []
        moveO = []

        global myve
        myve = []
        for i in range(1, 10):
            myve.append(i)

        lab1.config(text= 'A', bg = "blue", relief = GROOVE)
        lab2.config(text= 'B', bg = "blue", relief = GROOVE)
        lab3.config(text= 'C', bg = "blue", relief = GROOVE)

        lab4.config(text= 'D', bg = "blue", relief = GROOVE)
        lab5.config(text= 'E', bg = "blue", relief = GROOVE)
        lab6.config(text= 'F', bg = "blue", relief = GROOVE)

        lab7.config(text= 'G', bg = "blue", relief = GROOVE)
        lab8.config(text= 'H', bg = "blue", relief = GROOVE)
        lab9.config(text= 'I', bg = "blue", relief = GROOVE)

        start()
    else:
        fin()

def fin():
    global nam 
    global score
    global ate
    root.withdraw()
    age = score/ate * 100 
    age = round(age, 2)
    age = str(age) + str('%')
    messagebox.showinfo('Aftermath', 'You played '+str(ate)+ ' games and won '+str(score)+' out of them!'+ ' Your score is -> '+str(age)+'!')
    messagebox.showerror('Please play again soon!', "Bye, Thanks for playing")
    root.destroy()
    sys.exit()

def exit():
    global win
    if win == '':
        print('Game Over!\n')
        messagebox.showinfo('Game Over!', "Match resulted in Draw! Ha ha ha!")
        global score
        score += 0.5
    global stat 
    stat = 0
    res()

#AI Algorithms
def move():
    global com 
    global myve
    global moveO
    global moveX
    global ch
    com = 0
    if ch == 'X':
        #Defensive Algorithms which run when computer is 'O'
        for i in moveX:
            for j in moveX:
                #AI Algorith Defensive Row A
                if i == 1 and j == 2 and 3 in myve:
                    com = 3
                elif i == 2 and j == 3 and 1 in myve:
                    com = 1
                elif i == 3 and j == 1 and 2 in myve:
                    com = 2

                #AI Algorith Defensive Row B
                elif i == 4 and j == 5 and 6 in myve:
                    com = 6
                elif i == 5 and j == 6 and 4 in myve:
                    com = 4
                elif i == 6 and j == 4 and 5 in myve:
                    com = 5 

                #AI Algorith Defensive Row C
                elif i == 7 and j == 8 and 9 in myve:
                    com = 9
                elif i == 8 and j == 9 and 7 in myve:
                    com = 7
                elif i == 9 and j == 7 and 8 in myve:
                    com = 8 

                #AI Algorith Defensive Column A
                if i == 1 and j == 4 and 7 in myve:
                    com = 7
                elif i == 4 and j == 7 and 1 in myve:
                    com = 1
                elif i == 7 and j == 1 and 4 in myve:
                    com = 4

                #AI Algorith Defensive Column B
                elif i == 2 and j == 5 and 8 in myve:
                    com = 8
                elif i == 5 and j == 8 and 2 in myve:
                    com = 2
                elif i == 8 and j == 2 and 5 in myve:
                    com = 5 

                #AI Algorith Defensive Column C
                elif i == 3 and j == 6 and 9 in myve:
                    com = 9
                elif i == 6 and j == 9 and 3 in myve:
                    com = 3
                elif i == 9 and j == 3 and 6 in myve:
                    com = 6

                #AI Algorith Defensive Diagonal A
                if i == 1 and j == 5 and 9 in myve:
                    com = 9
                elif i == 5 and j == 9 and 1 in myve:
                    com = 1
                elif i == 9 and j == 1 and 5 in myve:
                    com = 5

                #AI Algorith Defensive Diagonal B
                elif i == 3 and j == 5 and 7 in myve:
                    com = 7
                elif i == 5 and j == 7 and 3 in myve:
                    com = 3
                elif i == 7 and j == 3 and 5 in myve:
                    com = 5                

                elif not myve:
                    messagebox.showerror('Programming Bug!', 'Please Call PyCoder@23')

        #Attacking Algorithms which run when computer is 'O'
        for i in moveO:
            for j in moveO:
                #AI Algorith Attacking Row A
                if i == 1 and j == 2 and 3 in myve:
                    com = 3
                elif i == 2 and j == 3 and 1 in myve:
                    com = 1
                elif i == 3 and j == 1 and 2 in myve:
                    com = 2

                #AI Algorith Attacking Row B
                elif i == 4 and j == 5 and 6 in myve:
                    com = 6
                elif i == 5 and j == 6 and 4 in myve:
                    com = 4
                elif i == 6 and j == 4 and 5 in myve:
                    com = 5 

                #AI Algorith Attacking Row C
                elif i == 7 and j == 8 and 9 in myve:
                    com = 9
                elif i == 8 and j == 9 and 7 in myve:
                    com = 7
                elif i == 9 and j == 7 and 8 in myve:
                    com = 8 

                #AI Algorith Attacking Column A
                if i == 1 and j == 4 and 7 in myve:
                    com = 7
                elif i == 4 and j == 7 and 1 in myve:
                    com = 1
                elif i == 7 and j == 1 and 4 in myve:
                    com = 4

                #AI Algorith Attacking Column B
                elif i == 2 and j == 5 and 8 in myve:
                    com = 8
                elif i == 5 and j == 8 and 2 in myve:
                    com = 2
                elif i == 8 and j == 2 and 5 in myve:
                    com = 5 

                #AI Algorith Attacking Column C
                elif i == 3 and j == 6 and 9 in myve:
                    com = 9
                elif i == 6 and j == 9 and 3 in myve:
                    com = 3
                elif i == 9 and j == 3 and 6 in myve:
                    com = 6

                #AI Algorith Attacking Diagonal A
                if i == 1 and j == 5 and 9 in myve:
                    com = 9
                elif i == 5 and j == 9 and 1 in myve:
                    com = 1
                elif i == 9 and j == 1 and 5 in myve:
                    com = 5

                #AI Algorith Attacking Diagonal B
                elif i == 3 and j == 5 and 7 in myve:
                    com = 7
                elif i == 5 and j == 7 and 3 in myve:
                    com = 3
                elif i == 7 and j == 3 and 5 in myve:
                    com = 5                

                elif not myve:
                    messagebox.showerror('Programming Bug!', 'Please Call PyCoder@23')
                    
        #Ghar bachao Algorithms which run when computer is 'O'!
        if com == 0:
            com = random.choice(myve)
            i = 0
            while True:
                com = random.choice(myve)
                if com % 2 == 0 and len(myve) != 8:
                    #B, H
                    if (com == 2 or com == 8) and (com + 1) not in moveO and (com - 1) not in moveO:
                        break
                    
                    #D, F
                    elif(com == 4 or com == 6) and (com + 3) not in moveO and (com - 3) not in moveO:
                        break

                    else:
                        i += 1
                        if i == 15: 
                            break

                elif com % 2 == 1:
                    #A, C
                    if (com == 1 or com == 3) and (com + 3) not in moveO and (com + 6) not in moveO:
                        break
                    
                    #C, I
                    elif (com == 3 or com == 9) and (com - 1) not in moveO and (com - 2) not in moveO:
                        break
                    
                    #G, I
                    elif (com == 9 or com == 7) and (com - 3) not in moveO and (com - 6) not in moveO:
                        break
                    
                    #A, G
                    elif (com == 7 or com == 1) and (com + 1) not in moveO and (com + 2) not in moveO:
                        break
                    
                    #AEI
                    elif com == 1 and 5 not in moveO and 9 not in moveO:
                        break
                    
                    #CEG
                    elif com == 3 and 5 not in moveO and 7 not in moveO:
                        break
                    
                    #GEC
                    elif com == 7 and 5 not in moveO and 3 not in moveO:
                        break
                    
                    #IEA
                    elif com == 9 and 5 not in moveO and 1 not in moveO:
                        break

                    else:
                        i += 1
                        if i == 15: 
                            break
            
            if 5 in myve :
                com = 5

            if 1 in moveX and 6 in moveX and len(myve) == 6:
                com = 2

            if 1 in moveX and 8 in moveX and len(myve) == 6:
                com = 4

            if (2 in moveX and 6 in moveX and 1 not in moveO and 9 not in moveO and 3 in myve) or (2 in moveX and 9 in moveX and 1 not in moveO and 6 not in moveO and 3 in myve) or (1 in moveX and 6 in moveX and 2 not in moveO and 9 not in moveO and 3 in myve):
                com = 3
                print('A')

            if (6 in moveX and 8 in moveX and 7 not in moveO and 3 not in moveO and 9 in myve) or (6 in moveX and 7 in moveX and 8 not in moveO and 3 not in moveO and 9 in myve) or (3 in moveX and 8 in moveX and 7 not in moveO and 6 not in moveO and 9 in myve):
                com = 9
                print('B')

            if (8 in moveX and 1 in moveX and 9 not in moveO and 4 not in moveO and 7 in myve) or (8 in moveX and 4 in moveX and 9 not in moveO and 1 not in moveO and 7 in myve) or (9 in moveX and 4 in moveX and 8 not in moveO and 1 not in moveO and 7 in myve):
                com = 7
                print('C')

            if (4 in moveX and 2 in moveX and 3 not in moveO and 7 not in moveO and 1 in myve) or (4 in moveX and 3 in moveX and 2 not in moveO and 7 not in moveO and 1 in myve) or (7 in moveX and 2 in moveX and 3 not in moveO and 4 not in moveO and 1 in myve):
                com = 1 
                print('D')

            if 1 in moveX and 9 in moveX and len(myve) == 6:
                com = 8

            print('AI Suggested Move -> '+(chr(com+64)))
        else:
            print('AI Recommended Move -> '+str(chr(com+64)))
            
    else:        
        #Defensive Algorithms which run when computer is 'X'
        for i in moveO:
            for j in moveO:
                #AI Algorith Defensive Row A
                if i == 1 and j == 2 and 3 in myve:
                    com = 3
                elif i == 2 and j == 3 and 1 in myve:
                    com = 1
                elif i == 3 and j == 1 and 2 in myve:
                    com = 2

                #AI Algorith Defensive Row B
                elif i == 4 and j == 5 and 6 in myve:
                    com = 6
                elif i == 5 and j == 6 and 4 in myve:
                    com = 4
                elif i == 6 and j == 4 and 5 in myve:
                    com = 5 

                #AI Algorith Defensive Row C
                elif i == 7 and j == 8 and 9 in myve:
                    com = 9
                elif i == 8 and j == 9 and 7 in myve:
                    com = 7
                elif i == 9 and j == 7 and 8 in myve:
                    com = 8 

                #AI Algorith Defensive Column A
                if i == 1 and j == 4 and 7 in myve:
                    com = 7
                elif i == 4 and j == 7 and 1 in myve:
                    com = 1
                elif i == 7 and j == 1 and 4 in myve:
                    com = 4

                #AI Algorith Defensive Column B
                elif i == 2 and j == 5 and 8 in myve:
                    com = 8
                elif i == 5 and j == 8 and 2 in myve:
                    com = 2
                elif i == 8 and j == 2 and 5 in myve:
                    com = 5 

                #AI Algorith Defensive Column C
                elif i == 3 and j == 6 and 9 in myve:
                    com = 9
                elif i == 6 and j == 9 and 3 in myve:
                    com = 3
                elif i == 9 and j == 3 and 6 in myve:
                    com = 6

                #AI Algorith Defensive Diagonal A
                if i == 1 and j == 5 and 9 in myve:
                    com = 9
                elif i == 5 and j == 9 and 1 in myve:
                    com = 1
                elif i == 9 and j == 1 and 5 in myve:
                    com = 5

                #AI Algorith Defensive Diagonal B
                elif i == 3 and j == 5 and 7 in myve:
                    com = 7
                elif i == 5 and j == 7 and 3 in myve:
                    com = 3
                elif i == 7 and j == 3 and 5 in myve:
                    com = 5                

                elif not myve:
                    messagebox.showerror('Programming Bug!', 'Please Call PyCoder@23')

        #Attacking Algorithms which run when computer is 'X'
        for i in moveX:
            for j in moveX:
                #AI Algorith Attacking Row A
                if i == 1 and j == 2 and 3 in myve:
                    com = 3
                elif i == 2 and j == 3 and 1 in myve:
                    com = 1
                elif i == 3 and j == 1 and 2 in myve:
                    com = 2

                #AI Algorith Attacking Row B
                elif i == 4 and j == 5 and 6 in myve:
                    com = 6
                elif i == 5 and j == 6 and 4 in myve:
                    com = 4
                elif i == 6 and j == 4 and 5 in myve:
                    com = 5 

                #AI Algorith Attacking Row C
                elif i == 7 and j == 8 and 9 in myve:
                    com = 9
                elif i == 8 and j == 9 and 7 in myve:
                    com = 7
                elif i == 9 and j == 7 and 8 in myve:
                    com = 8 

                #AI Algorith Attacking Column A
                if i == 1 and j == 4 and 7 in myve:
                    com = 7
                elif i == 4 and j == 7 and 1 in myve:
                    com = 1
                elif i == 7 and j == 1 and 4 in myve:
                    com = 4

                #AI Algorith Attacking Column B
                elif i == 2 and j == 5 and 8 in myve:
                    com = 8
                elif i == 5 and j == 8 and 2 in myve:
                    com = 2
                elif i == 8 and j == 2 and 5 in myve:
                    com = 5 

                #AI Algorith Attacking Column C
                elif i == 3 and j == 6 and 9 in myve:
                    com = 9
                elif i == 6 and j == 9 and 3 in myve:
                    com = 3
                elif i == 9 and j == 3 and 6 in myve:
                    com = 6

                #AI Algorith Attacking Diagonal A
                if i == 1 and j == 5 and 9 in myve:
                    com = 9
                elif i == 5 and j == 9 and 1 in myve:
                    com = 1
                elif i == 9 and j == 1 and 5 in myve:
                    com = 5

                #AI Algorith Attacking Diagonal B
                elif i == 3 and j == 5 and 7 in myve:
                    com = 7
                elif i == 5 and j == 7 and 3 in myve:
                    com = 3
                elif i == 7 and j == 3 and 5 in myve:
                    com = 5                

                elif not myve:
                    messagebox.showerror('Programming Bug!', 'Please Call PyCoder@23')
        
        #Ghar bachao Algorithms which run when computer is 'X'!
        if com == 0:
            com = random.choice(myve)
            i = 0
            while True:
                com = random.choice(myve)
                if com % 2 == 0 and len(myve) != 8:
                    #B, H
                    if (com == 2 or com == 8) and (com + 1) not in moveX and (com - 1) not in moveX:
                        break
                    
                    #D, F
                    elif(com == 4 or com == 6) and (com + 3) not in moveX and (com - 3) not in moveX:
                        break

                    else:
                        i += 1
                        if i == 15: 
                            break

                elif com % 2 == 1:
                    #A, C
                    if (com == 1 or com == 3) and (com + 3) not in moveX and (com + 6) not in moveX:
                        break
                    
                    #C, I
                    elif (com == 3 or com == 9) and (com - 1) not in moveX and (com - 2) not in moveX:
                        break
                    
                    #G, I
                    elif (com == 9 or com == 7) and (com - 3) not in moveX and (com - 6) not in moveX:
                        break
                    
                    #A, G
                    elif (com == 7 or com == 1) and (com + 1) not in moveX and (com + 2) not in moveX:
                        break
                    
                    #AEI
                    elif com == 1 and 5 not in moveX and 9 not in moveX:
                        break
                    
                    #CEG
                    elif com == 3 and 5 not in moveX and 7 not in moveX:
                        break
                    
                    #GEC
                    elif com == 7 and 5 not in moveX and 3 not in moveX:
                        break
                    
                    #IEA
                    elif com == 9 and 5 not in moveX and 1 not in moveX:
                        break

                    else:
                        i += 1
                        if i == 15: 
                            break
            
            if 5 in myve :
                com = 5

            if 1 in moveO and 6 in moveO and len(myve) == 6:
                com = 2

            if 1 in moveO and 8 in moveO and len(myve) == 6:
                com = 4

            if (2 in moveO and 6 in moveO and 1 not in moveX and 9 not in moveX and 3 in myve) or (2 in moveO and 9 in moveO and 1 not in moveX and 6 not in moveX and 3 in myve) or (1 in moveO and 6 in moveO and 2 not in moveX and 9 not in moveX and 3 in myve):
                com = 3

            if (6 in moveO and 8 in moveO and 7 not in moveX and 3 not in moveX and 9 in myve) or (6 in moveO and 7 in moveO and 8 not in moveX and 3 not in moveX and 9 in myve) or (3 in moveO and 8 in moveO and 7 not in moveX and 6 not in moveX and 9 in myve):
                com = 9

            if (8 in moveO and 1 in moveO and 9 not in moveX and 4 not in moveX and 7 in myve) or (8 in moveO and 4 in moveO and 9 not in moveX and 1 not in moveX and 7 in myve) or (9 in moveO and 4 in moveO and 8 not in moveX and 1 not in moveX and 7 in myve):
                com = 7

            if (4 in moveO and 2 in moveO and 3 not in moveX and 7 not in moveX and 1 in myve) or (4 in moveO and 3 in moveO and 2 not in moveX and 7 not in moveX and 1 in myve) or (7 in moveO and 2 in moveO and 3 not in moveX and 4 not in moveX and 1 in myve):
                com = 1 

            if 1 in moveO and 9 in moveO and len(myve) == 6:
                    com = 6

            print('AI Suggested Move -> '+(chr(com+64)))
        else:
            print('AI Recommended Move -> '+str(chr(com+64)))
            
def mob():
    if not myve:
        exit()
    else: 
        global stat
        if stat == 1:
            global com
            com = 0
            while com not in myve:
                move()
            if com not in myve:
                messagebox.showerror('Programming Bug!', 'Please Call PyCoder@23')
            myve.remove(com)
            global bh
            if bh == "X":
                moveX.append(com)
            elif bh == "O":
                moveO.append(com)
            print("Computer's move -> "+str(chr(com+64)))
            print('Available moves -> ', end = '')
            for i in myve:
                print(chr(i+64), end = ' ')
            print('\n')

            if com == 1:
                lab1.config(bg='black')
                lab1.config(text = bh)
                lab1.config(relief = RIDGE)
            elif com == 2:
                lab2.config(bg='black')
                lab2.config(text = bh)
                lab2.config(relief = RIDGE)
            elif com == 3:
                lab3.config(bg='black')
                lab3.config(text = bh)
                lab3.config(relief = RIDGE)        

            elif com == 4:
                lab4.config(bg='black')
                lab4.config(text = bh)
                lab9.config(relief = RIDGE)
            elif com == 5:
                lab5.config(bg='black')
                lab5.config(text = bh)
                lab5.config(relief = RIDGE)
            elif com == 6:
                lab6.config(bg='black')
                lab6.config(text = bh) 
                lab6.config(relief = RIDGE)

            elif com == 7:
                lab7.config(bg='black')
                lab7.config(text = bh)
                lab7.config(relief = RIDGE)
            elif com == 8:
                lab8.config(bg='black')
                lab8.config(text = bh)
                lab8.config(relief = RIDGE)
            elif com == 9:
                lab9.config(bg='black')
                lab9.config(text = bh) 
                lab9.config(relief = RIDGE)

            check()
            if not myve:
                print('No move left!', end = ' ')

def press():
    global stat
    if stat == 1:
        global hi
        print('You pressed -> '+hi)
        
        x = ord(hi)-64
        if x in myve:
            myve.remove(x)
            global ch
            if ch == "X":
                moveX.append(x)
            elif ch == "O":
                moveO.append(x)
            print('Your move -> '+str(chr(x+64)))
            print('Available moves -> ', end = '')
            for i in myve:
                print(chr(i+64), end = ' ')
            if not myve:
                print('No move left!', end = ' ')
            print('\n')

            if x == 1:
                lab1.config(bg='black')
                lab1.config(text = ch)
                lab1.config(relief = RIDGE)
            elif x == 2:
                lab2.config(bg='black')
                lab2.config(text = ch)
                lab2.config(relief = RIDGE)
            elif x == 3:
                lab3.config(bg='black')
                lab3.config(text = ch)   
                lab3.config(relief = RIDGE)     

            elif x == 4:
                lab4.config(bg='black')
                lab4.config(text = ch)
                lab4.config(relief = RIDGE)
            elif x == 5:
                lab5.config(bg='black')
                lab5.config(text = ch)
                lab5.config(relief = RIDGE)
            elif x == 6:
                lab6.config(bg='black')
                lab6.config(text = ch) 
                lab6.config(relief = RIDGE)

            elif x == 7:
                lab7.config(bg='black')
                lab7.config(text = ch)
                lab7.config(relief = RIDGE)
            elif x == 8:
                lab8.config(bg='black')
                lab8.config(text = ch)
                lab8.config(relief = RIDGE)
            elif x == 9:
                lab9.config(bg='black')
                lab9.config(text = ch) 
                lab9.config(relief = RIDGE)
            
            check()
            mob()
            stat = 1
            
        else:
            print('Move already chosen!')
            print('Try moving from -> ', end = '')
            if not myve:
                print('No move left!', end = ' ')
            for i in myve:
                print(chr(i+64), end = ' ')
            print('\n')
        
    
Title = Label(root, text = 'Tic Tac toe', bg = 'cyan', fg = 'blue', font = ('Comic Sans MS', 40, 'bold'))
Title.place(x = 175, y= 40, anchor = CENTER)

lab1 = Button(root, text = 'A', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum1, relief = GROOVE)
lab1.place(x = 70, y= 130, anchor = CENTER)

lab2 = Button(root, text = 'B', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum2, relief = GROOVE)
lab2.place(x = 174, y= 130, anchor = CENTER)

lab3 = Button(root, text = 'C', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum3, relief = GROOVE)
lab3.place(x = 280, y= 130, anchor = CENTER)

lab4 = Button(root, text = 'D', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum4, relief = GROOVE)
lab4.place(x = 70, y= 230, anchor = CENTER)

lab5 = Button(root, text = 'E', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum5, relief = GROOVE)
lab5.place(x = 174, y= 230, anchor = CENTER)

lab6 = Button(root, text = 'F', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum6, relief = GROOVE)
lab6.place(x = 280, y= 230, anchor = CENTER)

lab7 = Button(root, text = 'G', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum7, relief = GROOVE)
lab7.place(x = 70, y= 330, anchor = CENTER)

lab8 = Button(root, text = 'H', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum8, relief = GROOVE)
lab8.place(x = 174, y= 330, anchor = CENTER)

lab9 = Button(root, text = 'I', bg = 'blue', fg = 'white', height = 2, width = 6, font = ('Comic Sans MS', 16, 'bold'), command = sum9, relief = GROOVE)
lab9.place(x = 280, y= 330, anchor = CENTER)

start()
root.mainloop()
