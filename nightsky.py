from turtle import *
import random


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

def pickDir():
    return int(random.randrange(1,360))



bgcolor('navy')
for s in range(100):
    star(random.randrange(1,12), True, 'Yellow')
    up()
    right(pickDir())
    forward(random.randrange(25,200))
    down()

mainloop()
