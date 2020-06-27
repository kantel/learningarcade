import arcade
import random
from pvector import PVector

WIDTH = 400
HEIGHT = 400
TITLE = "Gravity scaled by Mass"
NO_MOVERS = 12

colorlist = [(239, 242, 63), (198, 102, 230), (151, 87, 165), (129, 122, 198), (98, 199, 119), (239, 242, 63)]

class Mover():
    
    def __init__(self, m, x, y):
        self.mass = m
        self.radius = m*5
        self.color = random.choice(colorlist)
        self.location = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
    
    def draw(self):
        arcade.draw_circle_filled(self.location.x, self.location.y, self.radius, self.color)
        arcade.draw_circle_outline(self.location.x, self.location.y, self.radius, arcade.color.BLACK)
    
    def apply_force(self, force):
        f = PVector.sdiv(force, self.mass)
        self.acceleration.add(f)
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.acceleration.mult(0)
    
        if (self.location.x >= WIDTH - self.radius):
            self.location.x = WIDTH - self.radius
            self.velocity.x *= -1
        elif (self.location.x <= self.radius):
            self.location.x = self.radius
            self.velocity.x *= -1
        if (self.location.y >= HEIGHT - self.radius):
            self.location.y = HEIGHT - self.radius
            self.velocity.y *= -1
        elif (self.location.y <= self.radius):
            self.location.y = self.radius
            self.velocity.y *= -1

class MyWindow(arcade.Window):
    
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(((149, 224, 245)))
        self.movers = []
        for i in range(NO_MOVERS):
            self.movers.append(Mover(random.uniform(0.5, 2.5), 15, HEIGHT - 15))
            m = self.movers[i].mass
            self.gravity = PVector(0, -0.1*m)
        self.wind = PVector(0.005, 0.0)
        
    
    def on_draw(self):
        arcade.start_render()
        for mover in self.movers:
            mover.draw()
    
    def on_update(self, delta_time):
        for mover in self.movers:
            mover.apply_force(self.wind)
            mover.apply_force(self.gravity)
            mover.update()

MyWindow()
arcade.run()
