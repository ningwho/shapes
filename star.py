from turtle import *

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


star(100, False, 'red')

mainloop()
