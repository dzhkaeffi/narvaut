import string
import random
import array
from tkinter import *
from tkinter import scrolledtext
from tkinter.messagebox import showinfo

# Window Settings
root = Tk()
root.title('Password Generator')
# root.wm_attributes('-alpha', 0.7)
root.geometry('400x200')
root.resizable(width=False, height=False)
history = []

# History
def showHistory():
    return None
# GUI
def printScale(v):
    Range.delete(0, "end")
    Range.insert(0, v)
def copy():
    root.clipboard_clear()
    root.clipboard_append(entryPassword.get())
    showinfo("Window","Password has been copied to clipboard!")
def generate():
    # pass = []
    # choice = []
    # password = ''
    return None



# PASSWORD ENTRY BOX
entryPassword = Entry(root, font=("Arial Bold", 10), width="30")
entryPassword.grid(column=0, row=0)

# MAX_LEN SLIDER
Range = Entry(root, font=("Arial Bold", 10), width="2")
passRange = Scale(root, label='Password length (min 4 - max 24)', from_=4, to=24, orient=HORIZONTAL,
                  font=("Arial Bold", 10), length=180, showvalue=0, tickinterval=4, command=printScale)
passRange.grid(column=0, row=4, ipadx=20), Range.grid(column=1, row=4), Range.insert(0, 4)

# Buttons
bGenerate = Button(root, font=("Arial Bold", 10), text="Generate",fg='darkred').grid(column=1, row=0)
bCopy = Button(root, font=("Arial Bold", 10), text="Copy", fg='green', command=copy).grid(column=2, row=0)
bHistory = Button(root, font=("Arial Bold", 10), text="History").grid(column=3, row=0)

# CheckBoxes
varUp = BooleanVar()
varLo = BooleanVar()
varDi = BooleanVar()
varSy = BooleanVar()

checkUp = Checkbutton(root, text='Uppercase', font=("Arial Bold", 10), var= varUp, command=generate).grid(column=0, row=5)
checkLo = Checkbutton(root, text='Lowercase', font=("Arial Bold", 10), var= varLo, command=generate).grid(column=0, row=6)
checkDi = Checkbutton(root, text='Numbers', font=("Arial Bold", 10), var= varDi, command=generate).grid(column=0, row=7)
checkSy = Checkbutton(root, text='Symbols', font=("Arial Bold", 10), var= varSy, command=generate).grid(column=0, row=8)

# Password Generator
digits = string.digits
locase = string.ascii_lowercase
upcase = string.ascii_uppercase
symbols = string.punctuation

'''
Easy - LO, UP
Medium - LO, UP, DIGITS 
Difficult - LO, UP, DIGITS, SYMBOLS
'''
    


# Start UI
root.mainloop()


