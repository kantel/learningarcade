import arcade
import random
from pvector import PVector

WIDTH = 400
HEIGHT = 400
TITLE = "Motion 101 (Random Acceleration)"

class Mover():
    
    def __init__(self):
        self.radius = 16
        # Position und Velocity
        self.position = PVector(WIDTH/2, HEIGHT/2)
        self.velocity = PVector(0, 0)
        # Maximalgeschwindigkeit
        self.topspeed = 10
        # Farbe
        self.color = (239, 242, 63)
    
    def draw(self):
        arcade.draw_circle_filled(self.position.x, self.position.y, self.radius, self.color)
        arcade.draw_circle_outline(self.position.x, self.position.y, self.radius, arcade.color.BLACK)
    
    def update(self):
        # Acceleration
        self.acceleration = PVector.random2D()
        # self.acceleration.mult(0.5)
        self.acceleration.mult(random.randrange(0, 2))
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topspeed)
        self.position.add(self.velocity)
    
        if (self.position.x >= WIDTH + self.radius):
            self.position.x = -self.radius
        elif (self.position.x <= -self.radius):
            self.position.x = WIDTH - self.radius
        if (self.position.y >= HEIGHT + self.radius):
            self.position.y = -self.radius
        elif (self.position.y <= -self.radius):
            self.position.y = HEIGHT - self.radius

class MyWindow(arcade.Window):
    
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(((149, 224, 245)))
        self.mover = Mover()
    
    def on_draw(self):
        arcade.start_render()
        self.mover.draw()
    
    def on_update(self, delta_time):
        self.mover.update()

MyWindow()
arcade.run()
