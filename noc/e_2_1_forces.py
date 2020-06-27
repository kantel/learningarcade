import arcade
import random
from pvector import PVector

WIDTH = 400
HEIGHT = 400
TITLE = "Forces (Wind and Gravity)"

class Mover():
    
    def __init__(self, m, x, y):
        self.mass = m
        self.radius = 16
        self.color = (239, 242, 63)
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
        self.mover = Mover(1, 40, HEIGHT - 40)
        self.wind = PVector(0.01, 0.0)
        self.gravity = PVector(0, -0.1)
    
    def on_draw(self):
        arcade.start_render()
        self.mover.draw()
    
    def on_update(self, delta_time):
        self.mover.apply_force(self.wind)
        self.mover.apply_force(self.gravity)
        self.mover.update()

MyWindow()
arcade.run()
