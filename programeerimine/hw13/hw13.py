from tkinter import *
 
window = Tk()
window.title("The Ship")
window.resizable(False, False)
area = Canvas(window, width=700, height=500, background="white")
area.grid() 

# Sea
area.create_rectangle(0, 300, 800, 500, fill="#0C60A2")

# Ship
points = [120,170,550,170,500,300,180,300]
area.create_polygon(points, fill="gray", outline='black')
area.create_rectangle(160, 140, 510, 170, fill='gray')
area.create_rectangle(180, 120, 500, 140, fill='gray')
# First Pipe
area.create_rectangle(220, 100, 280, 120, fill='red')
area.create_rectangle(220, 80, 280, 100, fill='lightgray') 
# Second Pipe
area.create_rectangle(400, 100, 460, 120, fill='red')
area.create_rectangle(400, 80, 460, 100, fill='lightgray') 
# Safety Ring
area.create_oval(450, 200, 500, 250, fill="white")
area.create_oval(470, 220, 480, 230, fill="gray")
# Clouds
area.create_oval(265, 35, 290, 50, fill='#E2E2E2')
area.create_oval(280, 20, 315, 50, fill='#E2E2E2')

area.create_oval(445, 35, 460, 50, fill='#E2E2E2')
area.create_oval(455, 20, 495, 50, fill='#E2E2E2')
# Windows 
area.create_oval(180, 200, 200, 220, fill="lightblue")
area.create_oval(220, 200, 240, 220, fill="lightblue")
area.create_oval(260, 200, 280, 220, fill="lightblue")


window.mainloop()