from easygui import *

arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

name = enterbox("What's your name?")
month = integerbox("What month were you born? *enter a number* ")
if name is None or month is None or name == "":
    msgbox("Why do you have to rebel, enter things like a normal human!!")
else:
    msgbox(name + " was born in the month which has " + str(arr[month - 1]) + " days!")
