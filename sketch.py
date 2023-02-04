import turtle 
# Initialize the turtle
t = turtle.Turtle()
t.speed(10)

# Create a loop to draw shapes
for i in range(4):
    t.forward(100)
    t.right(90)

# Hide the turtle and exit the turtle window
t.hideturtle()
turtle.done()

