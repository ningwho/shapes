from turtle import *

def triangle(size, fill, color):
    if fill == True:
        fillcolor(color)
        begin_fill()
    else:
        pencolor(color)


    for t in range(3):

        left(120)
        forward(size)
    end_fill()

    makeSpace(size)
def square(size, fill, color):
    if fill == True:
        fillcolor(color)
        begin_fill()
    else:
        pencolor(color)


    for sq in range(4):
        left(90)
        forward(size)
    end_fill()

    makeSpace(size)
def pentagon(size, fill, color):
    if fill == True:
        fillcolor(color)
        begin_fill()
    else:
        pencolor(color)


    for p in range(5):
        left(72)
        forward(size)
    end_fill()

    makeSpace(size)
def hexagon(size, fill, color):
    if fill == True:
        fillcolor(color)
        begin_fill()
    else:
        pencolor(color)



    for h in range(6):
        left(60)
        forward(size)
    end_fill()

    makeSpace(size)
def star(size, fill, color):
    if fill == True:
        fillcolor(color)
        begin_fill()
    else:
        pencolor(color)


    for x in range(5):

        right(144)
        forward(size)
        left(72)
        forward(size)
    end_fill()
    makeSpace(size)


def circle(size, fill, color):
    if fill == True:
        fillcolor(color)
        begin_fill()
    else:
        pencolor(color)



    for x in range(360):
        forward(size/100)
        right(1)
    end_fill()

    makeSpace(size)
def octagon(size, fill, color):
    if fill == True:
        fillcolor(color)
        begin_fill()
    else:
        pencolor(color)


    for x in range(8):
        forward(size)
        left(45)
    end_fill()
    makeSpace(size)


def makeSpace(size):
    up()
    forward(size*2)
    down()

def startPoint():
    left(180)
    up()
    forward(400)
    down()
    right(180)
