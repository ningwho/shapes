from turtle import *

def octagon(size):
    for x in range(8):
        forward(size)
        left(45)


octagon(100)

mainloop()
