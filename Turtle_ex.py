import turtle
import time

kedi = turtle.Turtle()
kedi.color('orange')
window = turtle.Screen()
window.bgcolor("#000000")
kedi.speed(5)
# speed = 0 no animation takes place
kedi.pensize(10)
kedi.penup()
# pull the pen up. no drawing when moving
kedi.goto(0, -100)
kedi.pendown()

#head 
for i in range(36):
  kedi.forward(30)
  kedi.left(10)
kedi.penup()

# eyes
kedi.penup()
kedi.goto(-80,90)
kedi.pendown()

kedi.left(90)
for i in range(45):
  kedi.forward(2)
  kedi.right(4)

kedi.penup()
kedi.goto(50,90)
kedi.pendown()

kedi.left(-180)
for i in range(45):
  kedi.forward(2)
  kedi.right(4)

# nose 
kedi.penup()
kedi.goto(0,50)
kedi.pendown()

kedi.setheading(0)

for i in range(5): 
  kedi.forward(25)
  kedi.right(120)
noseSt_x = kedi.xcor()
noseSt_y = kedi.ycor()

#mouth
kedi.left(120)
kedi.forward(10)
for i in range(4):

  kedi.right(16)
  kedi.forward(17)

kedi.penup()
kedi.goto(noseSt_x, noseSt_y)
kedi.pendown()
kedi.setheading(-60)

kedi.forward(10)
for i in range(4):
  kedi.left(16)
  kedi.forward(17)

kedi.penup()
kedi.goto(-19, -.10) 
kedi.pendown()
kedi.right(100)
for i in range(10):
  kedi.forward(12)
  kedi.left(21)

kedi.penup()
kedi.goto(114, 212) 
kedi.pendown()
kedi.forward(100)
kedi.left(120)
kedi.forward(75)

kedi.penup()
kedi.goto(-107, 193)
kedi.pendown()
kedi.setheading(75)
kedi.forward(100)
kedi.right(120)
kedi.forward(75)
kedi.ht()

time.sleep(5)
