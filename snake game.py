import time
import random
import turtle

delay = 0.1
score = 0
highestScore = 0


# Snake bodies
snakeBodies = []

# Getting screen / canvas for snake game
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=600, height=600)


# create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake's food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")  # food's inner colour
food.penup()
food.ht()
food.goto(0, 200)
food.st()

# score board
scoreBoard = turtle.Turtle()
scoreBoard.shape("square")
scoreBoard.fillcolor("black")
scoreBoard.penup()
scoreBoard.ht()
scoreBoard.goto(-250, -250)
scoreBoard.write(f"Score: {score}  | Highest Score: {highestScore}")

def moveUp():
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    if head.direction != "up":
        head.direction = "down"

def moveLeft():
    if head.direction != "right":
        head.direction = "left"

def moveRight():    
    if head.direction != "left":
        head.direction = "right"

def moveStop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

# event handling - key mappings
s.listen()        
s.onkey(moveUp, "Up")
s.onkey(moveDown, "Down")
s.onkey(moveLeft, "Left")
s.onkey(moveRight, "Right")
s.onkey(moveStop, "s")

# main loop
while True:
    s.update()  # to update screen
    # check conflict with screen's border
    if head.xcor() > 290:
        head.setx(-290)
    
    if head.xcor() < -290:
        head.setx(290)

    if head.ycor() > 290:
        head.sety(-290)
    
    if head.ycor() < -290:
        head.sety(290)

    # check conflict with food
    if head.distance(food) < 20:
        # move food to new distance / place
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # increase length of food
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        snakeBodies.append(body)  # append new body to nake

        # increase the score
        score += 10

        # change delay
        delay -= 0.001

        # update highest score
        if score > highestScore:
            highestScore = score

        scoreBoard.clear()
        scoreBoard.write(f"Score: {score} Highest Score: {highestScore}")

    for index in range(len(snakeBodies) - 1, 0, -1):
        x = snakeBodies[index - 1].xcor()
        y = snakeBodies[index - 1].ycor()

        snakeBodies[index].goto(x, y)
    
    if len(snakeBodies) > 0:
        x = head.xcor()
        y = head.ycor()
        snakeBodies[0].goto(x, y)
    move()

    # check conflict with snake's body
    for body in snakeBodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide bodies
            for body in snakeBodies:
                body.ht()
            snakeBodies.clear()

            score = 0
            delay = 0.1

            # update score board
            scoreBoard.clear()
            scoreBoard.write(f"Score:{score} | Highest Score: {highestScore}")
    
    time.sleep(delay)    

turtle.mainloop()