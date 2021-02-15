from tkinter import *
import random
import time

WIDTH = 1000
HEIGHT = 600

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Objects")
canvas.pack()

class Ball :
    def __init__(self):
        self.shape = canvas.create_oval(10, 10, 60, 60, fill = 'Green')
        self.xspeed = random.randrange(1, 10)
        self.yspeed = random.randrange(1, 10)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0 :
            self.yspeed = -self.yspeed

        if pos [2] >= WIDTH or pos[0] <= 0 :
            self.xspeed = -self.xspeed


newball = Ball()
newball1= Ball()
newball2 = Ball()
newball3 = Ball()
while True :
    newball.move()
    newball1.move()
    newball2.move()
    newball3.move()
    tk.update()
    time.sleep(0.01)
    
