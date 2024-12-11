import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=10000, height=100000)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

screen = turtle.Screen()
screen.setup(width=10000, height=100000)
screen.bgcolor('white')

t = turtle.Turtle()
t.penup()
t.shape("turtle")
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4)

def turtle_clicked(t, x, y):

    print('turtle clicked!')
    
    for i in range(0,360, 20):
        t.tilt(20)

t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))

turtle.done() # Important! Use `done` not `exitonclick` to keep the window open
