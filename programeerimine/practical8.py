from turtle import *
print("List of available colors can be found here https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html")
bgcolor(input("Enter desired background color [ex. green]: "))
color(input("Enter desired line color [ex. white]: "))
pensize(int(input("Enter desired line width [rec. 1-5]: ")))

for i in range(4): # this loop is just for the sake of showing that everything works
    forward(180)
    left(90)

exitonclick()