import turtle

turtle.bgcolor("black")
screen = turtle.Screen()
screen.setup(600, 600)
flower = turtle.Turtle()
flower.speed(1000000000000000000000000000000)

colors = ['orange', 'purple', 'brown', 'green']

def draw_branch(branch_length, flower, color_index, colors):
    if branch_length > 5:
        flower.color(colors[color_index % len(colors)])
        flower.forward(branch_length)
        flower.right(25)
        draw_branch(branch_length - 15, flower, color_index + 1, colors)
        flower.left(50)
        draw_branch(branch_length - 15, flower, color_index + 1, colors)
        flower.right(25)
        flower.backward(branch_length)
    else:
        return

def draw_flower(colors, size):
    for _ in range(4):
        flower.left(90)
        flower.up()
        flower.goto(0, 0)
        flower.down()
        draw_branch(size, flower, _, colors)

def draw_flower2(colors, size):
    for _ in range(4):
        flower.left(95)
        flower.up()
        flower.goto(0, 0)
        flower.down()
        draw_branch(size, flower, _, colors)

def draw_flower3(colors, size):
    for _ in range(4):
        flower.left(100)
        flower.up()
        flower.goto(0, 0)
        flower.down()
        draw_branch(size, flower, _, colors)




def draw_branch1(branch_length, flower, color_index, colors):
    if branch_length > 0:
        flower.color(colors[color_index % len(colors)])
        flower.forward(branch_length)
        flower.right(45)
        draw_branch(branch_length - 15, flower, color_index + 1, colors)
        flower.left(90)
        draw_branch(branch_length - 15, flower, color_index + 1, colors)
        flower.right(45)
        flower.backward(branch_length)
    else:
        return

def draw_flower1(colors, size):
    for _ in range(8):
        flower.left(90)
        flower.up()
        flower.goto(0, 0)
        flower.down()
        draw_branch1(size, flower, _, colors)


flower.penup()
flower.goto(-200, -200)
flower.pendown()

draw_flower(colors, 85)
draw_flower2(colors, 85)
draw_flower3(colors, 85)

draw_flower(colors, 75)
draw_flower2(colors, 65)
draw_flower3(colors, 70)
#draw_flower1(colors, 60)



turtle.done()
