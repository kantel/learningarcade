import arcade
import random
from pvector import PVector

WIDTH = 940
HEIGHT = 315
TITLE = "Forces for many Objects"
NO_MOVERS = 12

colorlist = [(240, 80, 37), (248, 158, 80), (248, 239, 34), (240, 99, 164), (146, 82, 161), (129, 122, 198), (98, 199, 119)]

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
        arcade.set_background_color((49, 197, 244))
        self.movers = []
        for _ in range(NO_MOVERS):
            self.movers.append(Mover(random.uniform(0.5, 2.5), 15, HEIGHT - 15))
        self.wind = PVector(0.01, 0.0)
        self.gravity = PVector(0, -0.1)
    
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
