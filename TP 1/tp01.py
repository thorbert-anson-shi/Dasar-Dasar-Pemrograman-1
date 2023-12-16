import turtle
import math

title = "Super Mario Towers"
screen = turtle.Screen()

turtle.speed(100)
turtle.delay(0)

# Input Validation
# ======================================================
tower_amt = screen.numinput(title, "Desired number of towers (integer)", minval=1)
# tower amount (min 1)
while math.ceil(tower_amt) > tower_amt:
    tower_amt = screen.numinput(
        title, "The value you entered was not an integer! Try again", minval=1
    )

if tower_amt != 1:
    # distance between towers (min 2 units max 5 units)
    separation = screen.numinput(
        title, "Distance between towers (integer)", minval=2, maxval=5
    )
    while math.ceil(separation) > separation:
        separation = screen.numinput(
            title,
            "The value you entered was not an integer! Try again",
            minval=2,
            maxval=5,
        )

    # layer diff between towers (min 2 max 5)

    layer_diff = screen.numinput(
        title, "Layer difference per tower (integer)", minval=2, maxval=5
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

# block width (max 35 units)
block_width = screen.numinput(title, "Brick width (float)", minval=1, maxval=35)

# block height (max 25 units)
block_height = screen.numinput(title, "Brick height (float)", minval=1, maxval=25)

# first tower layers (max 25 layers)
start_layers = screen.numinput(
    title, "Number of starting layers (integer)", minval=1, maxval=25
)
while math.ceil(start_layers) > start_layers:
    start_layers = screen.numinput(
        title,
        "The value you entered was not an integer! Try again",
        minval=1,
        maxval=25,
    )

# tower width (max 10 blocks)
tower_block_width = screen.numinput(
    title, "Tower width (integer):", minval=1, maxval=10
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
final_tower_layers = int(start_layers + tower_amt * layer_diff)

layer_nums = [
    i for i in range(int(start_layers), final_tower_layers + 1, int(layer_diff))
]
print(layer_nums)

# the size of the screen is equal to the (number of towers * (width of each tower + separation distance between towers)) between towers
# can't forget about padding
turtle.screensize(
    tower_amt * (block_width * (tower_block_width + separation)) + 150,
    final_tower_layers * block_height + 150,
)

print(turtle.screensize())

turtle.colormode(255)

turtle.penup()
turtle.goto((-(turtle.screensize()[0] - 150) / 2), -(turtle.screensize()[1] - 150) / 2)

block_total = 0

for tower in range(int(tower_amt)):
    turtle.fillcolor(218, 127, 101)
    if tower == 0:
        pass
    else:
        turtle.goto(
            turtle.pos()
            + [block_width * separation, -layer_nums[tower - 1] * block_height]
        )
    # make tower
    # move the separation distance
    for layer in range(layer_nums[tower]):
        # draw layer
        for brick in range(int(tower_block_width)):
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
            # print brick
            # fill color
        turtle.penup()
        turtle.goto(turtle.pos() + [-block_width * tower_block_width, block_height])
        # move up one layer
    turtle.goto(turtle.pos() + [-block_width / 2, 0])
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
    turtle.backward(block_width / 2)

turtle.goto(0, -turtle.screensize()[1] / 2)
turtle.write(
    f"Turtle has finished printing with {block_total} blocks.",
    align="center",
    font=["Arial", 20, "normal"],
)

turtle.done()
