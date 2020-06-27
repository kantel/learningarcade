import turtle as t
import random

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(43, 62, 80)
wn.setup(width = 600, height = 600)
wn.title("Random Walk")

walker = t.Turtle()
walker.speed(0)
walker.pensize(2)
walker.pencolor(255, 255, 178)

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
        walker.seth(0)
    elif roll == 2:
        walker.seth(90)
    elif roll == 3:
        walker.seth(180)
    elif roll == 4:
        walker.seth(270)
    walker.fd(3)

print("I did it, Babe!")

wn.mainloop()