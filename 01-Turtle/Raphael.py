import turtle

turtle.speed(200)
turtle.bgcolor("black")
turtle.pencolor("blue")
turtle.begin_fill()

for x in range(1000):
  turtle.right(10)
  turtle.forward(300)
  turtle.right(170)
  turtle.forward(150)
  turtle.left(5)

turtle.end_fill()
turtle.done()
