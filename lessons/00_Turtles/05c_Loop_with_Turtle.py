
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape("turtle") 
tina.forward(90)
tina.left(20)
tina.penup()
tina.forward(20)
tina.pendown()
tina.right(30)
tina.forward(80)
tina.speed(0)
for i in range(4):
tina.circle(35)
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

turtle.exitonclick()