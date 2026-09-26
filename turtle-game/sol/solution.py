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
screen.bgcolor("yellow")  # Background colour
player.color("blue")    # Player colour


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
    current_x = player.xcor()
    new_x = current_x - 10
    player.setx(new_x)

def move_up():
    # Need to implement this. Up/down is the Y axis. player has "ycor" and "sety" methods, just like for the X axis above
    # e.g. player.ycor() will get the current Y coordinate of the player

    # You don't always need to create new variables for every step - you can combine functions together
    new_y = player.ycor() + 10
    player.sety(new_y)


def move_down():
    # Like above, we can combine functions together. But sometimes it's clearer to keep it on several lines
    player.sety(player.ycor() - 10)

def change_col():
    player.color("red")

def pen_up():
    player.penup()

def pen_down():
    player.pendown()

def teleport():
    new_x = random.randint(0, 600)
    new_y = random.randint(0, 400)
    player.setx(new_x)
    player.sety(new_y)


# This is where you enable player controls.  Don't worry about how it works exactly (not important). But you can 
# add a new key by adding new lines. You can see the "onkey" function takes two inputs
#  1. The first input is the name of your function which will run when they press the key (e.g. "move_left")
#  2. The second input is the key that they press. For example "w", "a", "space", "Left" ("Left" in this example)
#
# So for example, you could write 'screen.onkey(teleport, "t")' to call your "teleport" function whenever the player presses "t"
screen.onkey(move_left, "Left")    # When the player presses the left arrow, call the "move_left" funciton
screen.onkey(move_right, "Right")  # When the player presses the right arrow, call the "move_right" function
screen.onkey(move_up, "Up")        # ...
screen.onkey(move_down, "Down")
screen.onkey(change_col, "c")
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "d")
screen.onkey(teleport, "t")


# === Ignore this stuff, it just starts everything running ===
screen.getcanvas().focus_force()
screen.listen()
screen.mainloop()

