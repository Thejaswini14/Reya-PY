import turtle

# Set up the screen and turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Loop 4 times to draw each side of the square
for _ in range(4):
    my_turtle.forward(100)  # Move forward by 100 pixels
    my_turtle.right(90)     # Turn right by 90 degrees

# Keep the window open until clicked
screen.exitonclick()