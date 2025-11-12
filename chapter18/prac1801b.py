from turtle import *

colormode(255)

lt(90)
initial_width = 14
max_level = 15
initial_length = 120
branch_angle = 45

width(initial_width)

r = g = b = 0
pencolor(r, g, b)

pu()
bk(initial_length)
pd()
fd(initial_length)


def draw_tree(lth, level):
    global r, g, b
    w = width()

    width(w * 3 / 4)
    r = r + 10
    g = g + 20
    b = b + 30
    pencolor(r % 255, g % 255, b % 255)
    lth = lth * 3 / 4

    lt(branch_angle)
    fd(lth)
    if level < max_level:
        draw_tree(lth, level + 1)
    bk(lth)
    rt(2 * branch_angle)
    fd(lth)
    if level < max_level:
        draw_tree(lth, level + 1)
    bk(lth)
    lt(branch_angle)
    width(w)


speed("fastest")
draw_tree(initial_length, 4)
done()
