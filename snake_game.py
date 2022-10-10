#modules
from tkinter import *
import turtle
import time 
import random

delay = 0.1
score = 0
high_score = 0

#window screen
wn = turtle.Screen()
wn.title = ('Snake Game')
wn.bgcolor('Blue')

#width and height of the window screen
wn.setup(width=600, height=600)
wn.tracer(0)
#head of the snake
head = turtle.Turtle()
head.shape("circle")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
#food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

#score and high-score counter
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write ("Score : 0 High Score : 0", align="center", font= ("Arial", 24, "bold"))

#assignining key directions
def group():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction =="right":
        x = head.xcor()
        head.setx(x + 20)


#keyboard binding   
wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

#segment - (eat-food) reward
segments = []

#game logic
game_on = True
while game_on:
    wn.update()
    if head.xcor()  > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'green', 'black'])
        shapes = random.choice(['square', 'triangle', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score: {}".format(score, high_score), align="center", font= ("Arial", 24, "bold"))

    #random food location
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        #Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square') #tail shape
        new_segment.color('orange') # tail color
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 1

        #updating high-score if score value exceedes its value
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score: {}".format(score, high_score), align="center", font= ("candara", 24, "bold"))

    #checking for head collisions with body
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'Stop'
            colors = random.choice(['red', 'green', 'black'])
            shapes = random.choice(['square', 'triangle', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score: {}".format(score, high_score), align="center", font= ("Arial", 24, "bold"))
    time.sleep(delay)
wn.mainloop()

