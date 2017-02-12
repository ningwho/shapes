from turtle import *

def circle(size):

  for x in range(360):
      forward(size/100)
      right(1)

circle(200)

mainloop()
