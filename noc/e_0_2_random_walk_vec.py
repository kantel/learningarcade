import turtle as t
import random
from pvector import PVector

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(43, 62, 80)
wn.setup(width = 600, height = 600)
wn.title("Random Walk with Vectors")

walker = t.Turtle()
walker.speed(0)
walker.pensize(2)
walker.location = PVector(0, 0)

for step in range(5000):
    if step < 1000:
        walker.pencolor(255, 255, 178)
    elif step < 2000:
        walker.pencolor(254, 204, 92)
    elif step < 3000:
        walker.pencolor(253, 141, 60)
    elif step < 4000:
        walker.pencolor(240, 59, 32)
    else:
        walker.pencolor(189, 0, 38)
    
    roll = random.randint(1, 4)
    if roll == 1:
        walker.location.y += 3
    elif roll == 2:
        walker.location.x += 3
    elif roll == 3:
        walker.location.y -= 3
    elif roll == 4:
        walker.location.x -= 3
    walker.goto(walker.location.x, walker.location.y)

print("I did it, Babe!")

wn.mainloop()