from turtle import Turtle, Screen
import time
import random

screen = Screen()

screen.bgcolor("green")
screen.title("Vitejte v hadi hre")
screen.setup(width=600, height=600)
screen.tracer = False

# Hadi hlava 

head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction = "stop"

# Potrava 

apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100, 100)

body_parts = []




# Funkce

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
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def move_up():
    head.direction = "up"

def move_down():
    head.direction = "down"

def move_right():
    head.direction = "right"

def move_left():
    head.direction = "left"

# Kliknuti na klavesy

screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

while True:
    
    if head.distance(apple) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        apple.goto(x, y)

        # Pridani casti tela
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)

    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)

    move()
    time.sleep(0.1)
    screen.update()





screen.exitonclick()

