from tkinter import *
import random
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Mr. Stick Man Races for the Exit")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width = 600, height=600, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 600
        self.canvas_width = 600
        self.background = PhotoImage(file="background.gif")
        w = self.background.width()
        h = self.background.height()
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image( x * w, y * h, image=self.background, anchor='nw')
        self.sprites = []
        self.running = True
        self.tk.mainloop()

def mainloop(self):
    while True:
        if self.running == True:
            for sprite in self.sprites:
                sprite.move()
        self.tk.update_idletasks()
        self.tk.update()
        time.sleep(0.01)
    
g = Game()
g.mainloop()
#tk.mainloop()