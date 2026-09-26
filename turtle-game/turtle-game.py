# === Ignore this part - just setup stuff ===
import random
import turtle
screen = turtle.Screen()
screen.setup(600, 400)
player = turtle.Turtle()
player.penup()

# Set the player character shape (other shape options are "arrow", "turtle", "circle", "square", "triangle")
player.shape("square")

# Set the screen colours
screen.bgcolor("white")  # Background colour
player.color("black")    # Player colour


# === These functions make the player move ===

def move_right():
    # Get the current X coordinate of the player (player.xcor() gives you the current X coordinate)
    # We store our X coordinate in the variable "current_x"
    current_x = player.xcor()

    # Add 10 to our X position, so our X position will increase.  Store it in the "new_x" variable
    new_x = current_x + 10

    # Now we can call the "setx" function which sets our X coordinate. We give it the new X position that we just calculated
    player.setx(new_x) 


def move_left():
    # Need to implement this, it should be similar to move_right but we're going NEGATIVE in the X axis this time. So
    # we want to REDUCE our X coordinate
    print("todo")


def move_up():
    # Need to implement this. Up/down is the Y axis. player has "ycor" and "sety" methods, just like for the X axis above
    # e.g. player.ycor() will get the current Y coordinate of the player
    print("todo")


def move_down():
   # Just like above, you've got this 
   print("todo")


# This is where you enable player controls.  Don't worry about how it works exactly (not important). But you can 
# add a new key by adding new lines. You can see the "onkey" function takes two inputs
#  1. The first input is the name of your function which will run when they press the key (e.g. "move_left")
#  2. The second input is the key that they press. For example "W", "A", "Space", "Left" ("Left" in this example)
#
# So for example, you could write 'screen.onkey(teleport, "T")' to call your "teleport" function whenever the player presses "T"
screen.onkey(move_left, "Left")    # When the player presses the left arrow, call the "move_left" funciton
screen.onkey(move_right, "Right")  # When the player presses the right arrow, call the "move_right" function
screen.onkey(move_up, "Up")        # ...
screen.onkey(move_down, "Down")


# === Ignore this stuff, it just starts everything running ===
screen.getcanvas().focus_force()
screen.listen()
screen.mainloop()

