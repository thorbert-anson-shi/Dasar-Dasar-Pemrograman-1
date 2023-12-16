import turtle
import math

title = "Super Mario Towers"
screen = turtle.Screen()

# Just for ease of debugging and use
turtle.speed(0)
turtle.delay(0)

# Input Validation
# ======================================================
"""
The while loops are used to validate that the values entered by the user
are integers

If a number is a decimal (i.e. 2.4), the math.ceil() function would round it up to 3
which is not equal to 2.4

The only time where the math.ceil() function would return the number itself is
when the number is an integer due to the definition of the ceil function

        - Return the smallest integer greater than or equal to n.
"""

tower_amt = screen.numinput(title, "Desired number of towers (integer)", minval=1)
# Tower amount (min 1)
while math.ceil(tower_amt) > tower_amt:
    tower_amt = screen.numinput(
        title, "The value you entered was not an integer! Try again", minval=1
    )

if tower_amt != 1:
    # Distance between towers (min 2 units max 5 units)
    separation = screen.numinput(
        title, "Distance between towers (in blocks)", minval=2, maxval=5
    )
    while math.ceil(separation) > separation:
        separation = screen.numinput(
            title,
            "The value you entered was not an integer! Try again",
            minval=2,
            maxval=5,
        )

    # Layer diff between towers (min 2 max 5)

    layer_diff = screen.numinput(
        title, "Layer difference per tower (in blocks)", minval=2, maxval=5
    )
    while math.ceil(layer_diff) > layer_diff:
        layer_diff = screen.numinput(
            title,
            "The value you entered was not an integer! Try again",
            minval=2,
            maxval=5,
        )

else:
    separation = 0
    layer_diff = 0

# Block width (max 35 units)
block_width = screen.numinput(title, "Width of block (float)", minval=1, maxval=35)

# Block height (max 25 units)
block_height = screen.numinput(title, "Height of block (float)", minval=1, maxval=25)

# First tower layers (max 25 layers)
start_layers = screen.numinput(
    title, "Number of layers on leftmost tower", minval=1, maxval=25
)
while math.ceil(start_layers) > start_layers:
    start_layers = screen.numinput(
        title,
        "The value you entered was not an integer! Try again",
        minval=1,
        maxval=25,
    )

# Tower width (max 10 blocks)
tower_block_width = screen.numinput(
    title, "Tower width (in blocks):", minval=1, maxval=10
)
while math.ceil(tower_block_width) > tower_block_width:
    tower_block_width = screen.numinput(
        title,
        "The value you entered was not an integer! Try again",
        minval=1,
        maxval=10,
    )

# Beginning of Turtle Script
# =====================================================================

# Create a list of layer heights per tower
if tower_amt > 1:
    final_tower_layers = int(start_layers + tower_amt * layer_diff)

    layer_nums = [
        i for i in range(int(start_layers), final_tower_layers + 1, int(layer_diff))
    ]
else:
    layer_nums = [int(start_layers)]
    final_tower_layers = start_layers

# Adjusting the size of the screen to be dynamic to the number of towers
# Can't forget about padding
turtle.screensize(
    tower_amt * ((block_width * (tower_block_width + separation)))
    - block_width * separation
    + 150,
    final_tower_layers * block_height + 150,
)

# Enable use of rgb(255, 255, 255) color format
turtle.colormode(255)

turtle.penup()
# Move turtle to leftmost side of window + padding
turtle.goto(
    (-(turtle.screensize()[0] + separation / 2 - 150) / 2),
    -(turtle.screensize()[1] - 150) / 2,
)

# Brick counter
block_total = 0

for tower in range(int(tower_amt)):
    # Translated from hex code
    turtle.fillcolor(218, 127, 101)
    if tower == 0:
        pass
    else:
        # Move the separation distance
        turtle.goto(
            turtle.pos()
            + [block_width * separation, -layer_nums[tower - 1] * block_height]
        )
    # Make tower
    for layer in range(layer_nums[tower]):
        # Per layer
        for brick in range(int(tower_block_width)):
            turtle.pendown()
            turtle.begin_fill()
            # Per brick
            for i in range(2):
                turtle.forward(block_width)
                turtle.right(90)
                turtle.forward(block_height)
                turtle.right(90)
            turtle.end_fill()

            block_total += 1
            turtle.forward(block_width)
        turtle.penup()
        # Move up one layer
        turtle.goto(turtle.pos() + [-block_width * tower_block_width, block_height])

    # Position turtle for head of tower
    turtle.goto(turtle.pos() + [-block_width / 2, 0])
    # Change fill color
    turtle.fillcolor(105, 52, 36)
    for brick in range(int(tower_block_width + 1)):
        turtle.pendown()
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(block_width)
            turtle.right(90)
            turtle.forward(block_height)
            turtle.right(90)
        turtle.end_fill()

        block_total += 1
        turtle.forward(block_width)
    turtle.penup()

    # Mushroom
    # ========================================

    # Center turtle on each tower
    turtle.backward(block_width * (tower_block_width + 1) / 2)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()

    # Draw a yellow square

    side_length = block_width * tower_block_width / 3
    turtle.forward(side_length / 2)
    for _ in range(3):
        turtle.left(90)
        turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length / 2)
    turtle.end_fill()
    turtle.penup()

    turtle.fillcolor("red")

    # Go to middle top of yellow square to draw semicircle
    turtle.goto(turtle.xcor(), turtle.ycor() + side_length)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(side_length)
    turtle.left(90)
    turtle.circle(side_length, 180)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.end_fill()
    turtle.penup()

    # Go back to original position to make sure program doesn't break
    turtle.goto(
        turtle.xcor() + tower_block_width * block_width / 2,
        turtle.ycor() - side_length,
    )


# Make turtle go to bottom middle of the window and write the closing message
turtle.goto(0, -turtle.screensize()[1] / 2)
turtle.write(
    f"{int(tower_amt)} Super Mario tower{' has' if tower_amt==1 else 's have'} been printed with {block_total} blocks.",
    align="center",
    font=["Arial", 20, "normal"],
)

turtle.done()

# Ide validasi input integer berdasarkan math.ceil() didapatkan dari perbincangan bersama Anders Willard Leo
