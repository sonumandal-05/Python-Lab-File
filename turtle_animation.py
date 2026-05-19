import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

pen = turtle.Turtle()   
pen.shape("turtle")
pen.color("green")
pen.speed(0)

for i in range(200):
    pen.forward(i)
    pen.right(91)
turtle.done()