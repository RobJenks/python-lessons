# Turtle game

## Getting started
This is a VERY simple program where you can move a shape around the screen. Your GPU will be fine ;) 

Copy the code from "turtle-game.py" into your IDE to get started. I've added some comments to the code explaining how it works.  You can ignore some of the sections which just do setup - they're not important.

## Things to look at first
Starting at the top you can see we call a few functions. On line 9 we call the "player.shape" function to decide what shape our player character will be.  Just below that, we set the color of the background and the character.

Below this you can see some functions called "move_right", "move_left" etc.  This is how the player moves. We'll add new code here first.

Below the movement functions you can see some lines like "screen.onkey(...)" . These lines tell python "when the player presses some key, call this function I've written".  E.g. the first line says "When the player presses "Left", run my "move_left" function

Try running the program.  You should see a window appears with a small shape inside. If you press the right arrow key, it should move. None of the other keys will work yet though

## Part 1: Movement controls
First step is to let the player move around. I've implemented the move_right function for you. We do three things:
* Get the current X coordinate of the player
* Add a small amount to it (10) 
* Set the X coordinate to the new value. That makes us move positive along the X axis

So if our (X, Y) position was (20, 20), when we press the right arrow we would get the current X value (20), add 10 to it, and then set our X coordinate to the new value (30).  Our new position is now (30, 20)

Try implementing the left, up & down functions.  Left should be very similar, we just want to go negative along the X axis.  Up & Down are the same idea, you just need to use different functions to get the current **Y** coordinate (player.**y**cor) and set the new **Y** coordinate (player.set**y**)

You can delete my "print(todo)" lines and replace them with the real code

## Part 2: Ultra graphics
Remember there were a few functions near the start of the program which set the player shape, and the colors on the screen.  Try changing those to make it more colourful

## Part 3: Adding new controls
To add a new control, you just need two things:
* Create a new function (e.g. copy the "move_left" function", and give it a new name)
* Add another "screen.onkey(..)" line below, along with the others. This says "when this key is pressed, call my function".  I added some comments there to show how. Important: your function needs to come first, then the onkey line below it 

### Idea 1 - Changing player colour
You already saw some functions to change the player color or shape. And now you know how to make things happen when a key is pressed.  So try adding a new control - when the player presses "R", the player turns Red

### Idea 2 - Speedup / slowdown
You're moving the player by 10 each time when the arrow keys are pressed.  If you change that number, they'd move faster or slower. You could add keys to change the player speed.  Hint: you may want to make a variable for the player_speed, and use it instead of "10" in the code.  Then your key function can change that "player_speed" variable

### Idea 3 - Drawing on the screen
The "turtle" character that we're using has two other functions: "pendown()" and "penup()"
  * `pendown()` puts the "pen down", i.e. when the player moves around, it will draw a line on the screen where it moves
  * `penup()` lifts the pen up, the opposite, so the player stops drawing lines where it moves any more

You may have seen that we called "penup()" at the very start of the program on line 6.  You could now add controls to put the pen down or up, so you can draw pictures on the screen as you move

### Idea 4 - Teleporter (Getting hard now) 
You already know how to change the player position - you're calling "setx" / "sety" at the moment to move them each time the key is pressed.  But you don't need to move them a little bit each time.  You could also add a "teleport" function which jumps them to a random position on the screen!

You want to pick a random position, and we've already seen how to get a random number in the dice program.  Take a look at your github for the `random.randint` function we used before. Remember it takes a minimum and a maximum value, and will choose a random value between them.

If you use this function twice - once to make a new X variable, another to make a new Y variable, you could then call the setx/sety functions to jump to a random position

Hint: the game window is 600 wide (X axis) by 400 tall (Y axis), so generate the random numbers carefully so you don't jump off the screen

