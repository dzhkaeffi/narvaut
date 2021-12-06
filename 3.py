from tkinter import *
from tkinter import scrolledtext
import string
import random

def copy():
    root.clipboard_clear()
    root.clipboard_append(entryPassword.get())
def printScale(v):
    Range.delete(0, "end")
    Range.insert(0, v)
def savePass(pasHistory, password):
    pasHistory.append(password)
def showHistory():
    pH = ''
    for i in passHistory:
        pH += i + '\n'
    newWindow = Toplevel(root)
    newWindow.title("")
    group1 = LabelFrame(newWindow, text="History", padx=5, pady=5)
    group1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=E + W + N + S)
    newWindow.columnconfigure(0, weight=1)
    newWindow.rowconfigure(1, weight=1)
    group1.rowconfigure(0, weight=1)
    group1.columnconfigure(0, weight=1)
    T = scrolledtext.ScrolledText(group1, width=40, height=10)
    T.grid(row=0, column=0, sticky=E + W + N + S)
    T.insert(END, pH)

def my_upd():
    if var.get() == 1:
        varUpp.set(True), varLow.set(True), varNum.set(False), varSym.set(False)
        generate()
    elif var.get() == 2:
        varUpp.set(True), varLow.set(True), varNum.set(True), varSym.set(True)
        generate()
    elif var.get() == 3:
        varUpp.set(True), varLow.set(True), varNum.set(True), varSym.set(True)
        generate()
def lL(pas):
    while True:
        char = random.choice(string.ascii_lowercase)
        if char != 'l' or var.get() != 2:
            break
    pas.append(char)
def cL(pas):
    while True:
        char = random.choice(string.ascii_uppercase)
        if char != 'I' and char != 'O' or var.get() != 2:
            break
    pas.append(char)
def num(pas):
    while True:
        char = str(random.randint(0, 9))
        if char != '1' and char != '0' or var.get() != 2:
            break
    pas.append(char)
def sC(pas):
    while True:
        char = random.choice(string.punctuation)
        if char != '|' or var.get() != 2:
            break
    pas.append(char)

def generate():
    pas = []
    choice = []
    password = ''
    if int(Range.get()) > 99:
        character = int(99)
    elif int(Range.get()) < 1:
        character = int(1)
    else:
        character = int(Range.get())

    if varLow.get():
        choice.append('1')
    if varUpp.get():
        choice.append('2')
    if varNum.get():
        choice.append('3')
    if varSym.get():
        choice.append('4')

    if int(Range.get()) < 4:
        while character > 0:
            for i in random.choice(choice):
                if i == '1':
                    lL(pas)
                if i == '2':
                    cL(pas)
                if i == '3':
                    num(pas)
                if i == '4':
                    sC(pas)
                character -= 1

    elif int(Range.get()) >= 4:
        if varLow.get():
            lL(pas)
            character -= 1
        if varUpp.get():
            cL(pas)
            character -= 1
        if varNum.get():
            num(pas)
            character -= 1
        if varSym.get():
            sC(pas)
            character -= 1
        while character > 0:
            for i in random.choice(choice):
                if i == '1':
                    lL(pas)
                if i == '2':
                    cL(pas)
                if i == '3':
                    num(pas)
                if i == '4':
                    sC(pas)
                character -= 1

    random.shuffle(pas)
    for i in pas:
        password += i
    entryPassword.delete(0, "end")
    entryPassword.insert(0, password)
    savePass(passHistory, password)
    bonus = checkDiff(password)
    difLine(bonus)

def Requirement(upL, lowL, num, symbol):
    R = 0
    if upL >= 1:
        R += 1
    if lowL >= 1:
        R += 1
    if num >= 1:
        R += 1
    if symbol >= 1:
        R += 1
    return R
def checkDiff(password):
    upL = lowL = num = symbol = mid = repeat = conUpL = conLowL = conNum = lastChar = 0
    for char in password:   #counter
        if char.isalpha():
            if char.islower():
                lowL += 1
                if lastChar == char:
                    conLowL += 1
            if char.isupper():
                upL += 1
                if lastChar == char:
                    conUpL += 1
        if char.isdigit():
            num += 1
            if lastChar == char:
                conNum += 1
        if char in string.punctuation:
            symbol += 1
        if password.count(char) > 1:
            repeat += 1
        lastChar = char
    for char in password[1:-1]:
        if char.isdigit() or char in string.punctuation:
            mid += 1

    bonus = (len(password) * 4) + (num * 4) + (symbol * 6) + (mid * 2)  # ++++++
    if upL != 0:
        bonus += (len(password) - upL) * 2
    if lowL != 0:
        bonus += (len(password) - lowL) * 2
    if len(password) >= 8 and Requirement(upL, lowL, num, symbol) >= 3:
        bonus += (Requirement(upL, lowL, num, symbol) + 1) * 2
    if upL + lowL == len(password):     # ------
        bonus -= len(password)
    elif num == len(password):
        bonus -= len(password)
    bonus -= (repeat + (conUpL * 2) + (conLowL * 2) + (conNum * 2))
    return bonus

def difLine(bonus):
    difficulty = Canvas(root, width=250, height=10, bg='white')
    difficulty.grid_forget()
    difficulty = Canvas(root, width=250, height=10, bg='white')
    if bonus >= 100:
        difficulty.create_line(2, 7, 252, 7, fill='green', width=10)    # 100%
    elif bonus >= 80:
        difficulty.create_line(2, 7, 202, 7, fill='light green', width=10)  # 80%
    elif bonus >= 60:
        difficulty.create_line(2, 7, 152, 7, fill='gold', width=10)   #60%
    elif bonus >= 40:
        difficulty.create_line(2, 7, 102, 7, fill='orange', width=10)   #40%
    elif bonus < 40:
        difficulty.create_line(2, 7, 52, 7, fill='red', width=10)   #20%
    difficulty.create_line(52, 0, 52, 100, fill='white', width=3)
    difficulty.create_line(102, 0, 102, 100, fill='white', width=3)
    difficulty.create_line(152, 0, 152, 100, fill='white', width=3)
    difficulty.create_line(202, 0, 202, 100, fill='white', width=3)
    difficulty.grid(row=1)


root = Tk()
root.title("Password generator")
root.geometry("400x250")
root.resizable(0, 0)
var = IntVar()
passHistory = []

entryPassword = Entry(root, font=("Arial Bold", 10), width="35")
entryPassword.grid(column=0, row=0)
bCopy = Button(root, text="Copy", font=("Arial Bold", 10), command=copy).grid(column=1, row=0)
butReset = Button(root, text="Reset", font=("Arial Bold", 10), command=generate).grid(column=2, row=0)
history = Button(root, text="Show history", font=("Arial Bold", 10), command=showHistory).grid(column=1, row=1)

Range = Entry(root, font=("Arial Bold", 10), width="3")
passRange = Scale(root, label='Password length (minimum 4-maximum 99)', from_=4, to=99, orient=HORIZONTAL,
                  font=("Arial Bold", 10), length=220, showvalue=0, tickinterval=91, command=printScale)
passRange.grid(column=0, row=4, ipadx=20), Range.grid(column=1, row=4), Range.insert(0, 4)
easySay = Radiobutton(root, text='Easy to say', value=1, variable=var, font=("Arial Bold", 10), command=my_upd)
easyRead = Radiobutton(root, text='Easy to read', value=2, variable=var, font=("Arial Bold", 10), command=my_upd)
allChar = Radiobutton(root, text='All characters', value=3, variable=var, font=("Arial Bold", 10), command=my_upd)
easySay.grid(column=0, row=5), easyRead.grid(column=0, row=6), allChar.grid(column=0, row=7)

varUpp = BooleanVar()
varLow = BooleanVar()
varNum = BooleanVar()
varSym = BooleanVar()
chkUpp = Checkbutton(root, text='Uppercase', font=("Arial Bold", 10), var=varUpp,
                     command=generate).grid(column=1, row=5)
chkLow = Checkbutton(root, text='Lowercase', font=("Arial Bold", 10), var=varLow,
                     command=generate).grid(column=1, row=6)
chkNum = Checkbutton(root, text='Numbers', font=("Arial Bold", 10), var=varNum,
                     command=generate).grid(column=1, row=7)
chkSym = Checkbutton(root, text='Symbols', font=("Arial Bold", 10), var=varSym,
                     command=generate).grid(column=1, row=8)

var.set(3), varUpp.set(True), varLow.set(True), varNum.set(True), varSym.set(True)
generate()
root.mainloop()
