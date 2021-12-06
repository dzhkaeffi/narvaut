from tkinter import *
from tkinter import font 
 
window = Tk()
window.title("The Ship")
area = Canvas(window, width=700, height=500, background="white")
area.grid() 
 
 # фон - белый, мне просто захотелоось добавить волны :)

# основа 1
area.create_polygon(30,160,  300,160,  300,200,  60,200, fill="#79674E", outline = 'black')

# основа 2
area.create_polygon(30,160,  300,160,  200,300,  60,200, fill="#79674E", outline = 'black')

# основа 3
area.create_rectangle(200, 160, 500, 300, fill="#79674E", outline = 'black')

# основа 4
area.create_rectangle(450, 100, 600, 550, fill="#79674E", outline = 'black')

# мачта 1
area.create_line(370, 20, 370, 160, width=15, fill="#3D2E19")

# мачта 2
area.create_line(200, 20, 200, 160, width=15, fill="#3D2E19")

# парус 1
area.create_line(355, 5, 355, 150, width=20, fill="#CB430C")

# парус 2
area.create_line(185, 5, 185, 150, width=20, fill="#CB430C")

# волны
area.create_rectangle(0, 4600, 5000, 300, fill="#2B89D3")

window.mainloop()