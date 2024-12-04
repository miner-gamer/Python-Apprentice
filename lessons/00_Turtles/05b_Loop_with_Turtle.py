
"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(1)                           # Make the turtle move as fast, but not too fast. 

tina.forward(150)                       # Move tina forward by the forward distance
tina.left(90)                           # Turn tina left by the left turn

tina.forward(150)                       # Continue the last two steps three more times
tina.left(90)                           # to draw a square

tina.forward(19)
tina.left(90)

tina.forward(10)
tina.right(90)

tina.forward(150)
tina.forward(150)                       # Continue the last two steps three more times
tina.left(90)                           # to draw a square

tina.forward(19)
tina.left(90)

tina.forward(10)
tina.right(90)

tina.forward(150)
tina.forward(150)                       # Continue the last two steps three more times
tina.left(90)                           # to draw a square

tina.forward(35)
tina.forward(11)
tina.left(90)
tina.forward(160)
tina.right(80)
tina.forward(115)
tina.left(90)
tina.forward(100)





for i in range(10):
    import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

bob = turtle.Turtle()                  # Create a turtle named tina

bob.shape('turtle')                    # Set the shape of the turtle to a turtle
bob.speed(1)                           # Make the turtle move as fast, but not too fast. 

bob.forward(150)                       # Move tina forward by the forward distance
bob.left(90)                           # Turn tina left by the left turn

bob.forward(150)                       # Continue the last two steps three more times
bob.left(90)                           # to draw a square

bob.forward(150)
bob.forward(11)
bob.left(90)
bob.forward(50)
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tj = turtle.Turtle()
tj.shape('turtle')                    # Set the shape of the turtle to a turtle
tj.speed(1)                       # Create a turtle named tina
tj.forward(20)
tj.left(50)
tj.forward(200)
tj.forward(90)
tj.teleport(1)

    
    



turtle.exitonclick()                    # Close the window when we click on it
