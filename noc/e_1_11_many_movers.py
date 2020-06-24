import arcade
import random
from pvector import PVector

WIDTH = 400
HEIGHT = 400
TITLE = "Many Movers follow Mouse"
NO_MOVERS = 15

colorlist = [(239, 242, 63), (198, 102, 230), (151, 87, 165), (129, 122, 198), (98, 199, 119)]

class Mover():
    
    def __init__(self):
        self.radius = random.randrange(10, 20)
        self.mouse = PVector(200, 200)
        # Position und Velocity
        x = random.randrange(self.radius, WIDTH - self.radius)
        y = random.randrange(self.radius, HEIGHT - self.radius)
        self.position = PVector(x, y)
        v_x = random.randrange(-10, 10)
        v_y = random.randrange(-10, 10)
        self.velocity = PVector(v_x, v_y)
        # Maximalgeschwindigkeit
        self.topspeed = 10
        # Farbe
        self.color = random.choice(colorlist)
        
    def draw(self):
        arcade.draw_circle_filled(self.position.x, self.position.y, self.radius, self.color)
        arcade.draw_circle_outline(self.position.x, self.position.y, self.radius, arcade.color.BLACK)
    
    def update(self):
        dir = self.mouse - self.position
        dir.normalize()
        dir.mult(0.5)
        self.acceleration = dir
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
        self.movers = []
        for _ in range(NO_MOVERS):
            self.movers.append(Mover())
    
    def on_draw(self):
        arcade.start_render()
        
        for mover in self.movers:
            mover.draw()
    
    def on_update(self, delta_time):
        for mover in self.movers:
            mover.update()

    def on_mouse_motion(self, x, y, dx, dy):
        for mover in self.movers:
            mover.mouse = PVector(x, y)

MyWindow()
arcade.run()