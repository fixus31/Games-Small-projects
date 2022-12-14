from tkinter import * 
import random
import time

tk = Tk()
tk.title("Game: Bouncing Ball")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=600, height=600, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
tk.mainloop()
