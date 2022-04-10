# Case-study #4
# Developers:   Grishaev G. (35%),
#               Abrarova V. (40%),
#               Zlobinskaya L. (55%)

import turtle
import local as lc


# Function that takes information about colors.
def get_color_choice():
    '''Function takes information about colors'''
    color = input(lc.ASK1)
    color = color.lower()
    while not color in list:
        n = color
        print("'", n, lc.NOTRIGHT, end='')
        color = input()
        color = color.lower()
    return color


# Function that translates color to English.
def color_eng(c):
    '''Function that translates color to English'''
    elist = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']
    ind = list.index(c)
    c = elist[ind]
    return c


# Function that takes information for quantity of hexes.
def get_num_hexagons():
    '''Function that takes information for quantity of hexes'''
    hexagons_num = input(lc.ASK2)
    while True:
        try:
            hexagons_num = int(hexagons_num)
            if hexagons_num >= 4 and hexagons_num <= 20:
                return hexagons_num
            else:
                hexagons_num = input(lc.NOTRIGHT2)
        except ValueError:
            hexagons_num = input(lc.NOTRIGHT2)


# In this block, the turtle just goes to make our mosaic to be in the middle.
def Draw(side_len, color_1, color_2, hexagons_num):
    '''Function draws hexes by taken information'''
    Lune = turtle.Turtle()
    Lune.speed(10)
    Lune.penup()
    Lune.right(180)
    Lune.forward(250)
    Lune.right(90)
    Lune.forward(200)
    Lune.pendown()

    # Line number, then a loop that draws these lines.
    a = 1
    while a <= hexagons_num:
        if a % 2 != 0:

            summ = (a + 1) // 2
            if summ % 2 == 0:

                # Choose a color, if the line is even with a multiplicity of 2.
                # Then we start not with 1, but with 2 colors, so these are exactly diagonal lines.
                color_1n = color_2
                color_2n = color_1
            else:
                color_1n = color_1
                color_2n = color_2

            # Hex number.
            b = 1
            while b <= hexagons_num:

                # Drawing hexes.
                if b % 2 != 0:
                    Lune.fillcolor(color_1n)
                    Lune.begin_fill()
                    c = 1
                    while c <= 5:
                        Lune.forward(side_len)
                        Lune.right(60)
                        c += 1
                    Lune.forward(side_len)
                    Lune.end_fill()
                    Lune.penup()
                    Lune.left(180)
                    Lune.forward(side_len)
                    Lune.left(60)
                    Lune.forward(side_len)
                    Lune.left(60)
                    Lune.pendown()
                    b += 1
                else:
                    Lune.fillcolor(color_2n)
                    Lune.begin_fill()
                    c = 1
                    while c <= 5:
                        Lune.forward(side_len)
                        Lune.right(60)
                        c += 1
                    Lune.forward(side_len)
                    Lune.penup()
                    Lune.end_fill()
                    Lune.left(180)
                    Lune.forward(side_len)
                    Lune.left(60)
                    Lune.forward(side_len)
                    Lune.left(60)
                    Lune.pendown()
                    b += 1
            if a != hexagons_num:
                Lune.left(120)
                Lune.forward(side_len)
                Lune.left(60)
                Lune.forward(side_len)
                Lune.left(180)
            a += 1
        else:

            # The same process but for odd ones.
            summ = a // 2
            if summ % 2 == 0:
                color_1n = color_1
                color_2n = color_2
            else:
                color_1n = color_2
                color_2n = color_1
            b = 1
            while b <= hexagons_num:
                if b % 2 != 0:
                    Lune.fillcolor(color_1n)
                    Lune.begin_fill()
                    c = 1
                    while c <= 5:
                        Lune.forward(side_len)
                        Lune.left(60)
                        c += 1
                    Lune.forward(side_len)
                    Lune.end_fill()
                    Lune.penup()
                    Lune.right(180)
                    Lune.forward(side_len)
                    Lune.right(60)
                    Lune.forward(side_len)
                    Lune.right(60)
                    Lune.pendown()
                    b += 1
                else:
                    Lune.fillcolor(color_2n)
                    Lune.begin_fill()
                    c = 1
                    while c <= 5:
                        Lune.forward(side_len)
                        Lune.left(60)
                        c += 1
                    Lune.forward(side_len)
                    Lune.end_fill()
                    Lune.penup()
                    Lune.right(180)
                    Lune.forward(side_len)
                    Lune.right(60)
                    Lune.forward(side_len)
                    Lune.right(60)
                    Lune.pendown()
                    b += 1
            if a != hexagons_num:
                Lune.right(120)
                Lune.forward(side_len)
                Lune.right(60)
                Lune.forward(side_len)
                Lune.right(180)
            a += 1


print(lc.MENU)
list = ['красный', 'синий', 'зеленый', 'желтый', 'оранжевый', 'пурпурный', 'розовый']

# Menu.
x = get_color_choice()
y = get_color_choice()
color_1 = color_eng(x)
color_2 = color_eng(y)
hexagons_num = get_num_hexagons()
side_len = 500 / (hexagons_num * 3 ** 0.5)
Draw(side_len, color_1, color_2, hexagons_num)