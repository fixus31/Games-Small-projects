from tkinter import * 
import random
import time

class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(550, 10, text=self.score, fill=color)
    def hit(self):
        self.score += 10
        self.canvas.itemconfig(self.id, text=self.score)

class Ball:
    def __init__(self, canvas, paddle,score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 240, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        # start location is random
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        #returns current height of canvas
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        # stop when hit the bottom
        self.hit_bottom = False

    def hit_paddle(self, pos):
        # paddle's coordinates
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <=  paddle_pos[3]:
                self.x += self.paddle.x
                self.score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1.5
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -1.5
        if pos[0] <= 0:
            self.x = 1.5
        if pos[2] >= self.canvas_width:
            self.x = -1.5

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 400)
        # starting position of the paddle
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.start = False
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<Button-1>', self.start_game)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, x):
        self.x = -2
    def turn_right(self, x):
        self.x = 2
    def start_game(self, x):
        self.start = True
        #Game over


tk = Tk()
tk.title("Game: Bouncing Ball")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=600, height=600, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'brown')
score = Score(canvas, 'blue')
ball = Ball(canvas, paddle, score,'red')

game_over = canvas.create_text(300, 300, text="Game Over",font="bold", state="hidden")

while True:
    if ball.hit_bottom == False and paddle.start == True:
        ball.draw()
        paddle.draw()
    if ball.hit_bottom == True:
        time.sleep(0.7)
        canvas.itemconfig(game_over, state='normal')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
