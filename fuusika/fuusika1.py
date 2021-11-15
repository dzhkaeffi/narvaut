import math

def poltodec():
    radius = float(input("Enter radius: "))
    angle = float(input("Enter the angle in degrees: "))

    angle = angle * math.pi/180

    x = radius * math.cos(angle)
    y = radius * math.sin(angle)

    print('Carthesian coordinate is: x = %0.2f, y = %0.2f' %(x,y))

def dectopol():
    x = float(input("Enter value of x: "))
    y = float(input("Enter value of y: "))

    radius = math.sqrt(x**2+y**2)

    try:
        angle = math.atan(y/x)
    except: 
        angle = 0
    if x < 0 and y == 0:
        angle = 180
    else:
        angle = 180 * angle/math.pi
        if x < 0 and y > 0:
            angle = angle - 90
    if x == 0 and y > 0:
        angle = 90
    if x == 0 and y < 0:
        angle = 270
    if x < 0 and y < 0:
        angle = angle + 180
    if x > 0 and y < 0:
        angle = angle - 270
    if angle < 0:
        angle = -angle

    print('Polar coordinate is: radius = %0.2f, theta = %0.2f' %(radius,angle))


func = input("Input start (polar/decartes): ")

if func.lower() == "polar": 
    poltodec()
else: 
    dectopol()

