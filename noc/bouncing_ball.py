import arcade
import random
from pvector import PVector

WIDTH = 400
HEIGHT = 400
TITLE = "Bouncing Ball"
NO_BALLS = 10

colorlist = [(239, 242, 63), (198, 102, 230), (151, 87, 165), (129, 122, 198), (98, 199, 119)]

class Ball():
    
    def __init__(self):
        self.radius = random.randrange(5, 20)
        # Position and Velocity
        x = random.randrange(self.radius, WIDTH - self.radius)
        y = random.randrange(self.radius, HEIGHT - self.radius)
        self.position = PVector(x, y)
        v_x = random.randrange(-10, 10)
        v_y = random.randrange(-10, 10)
        self.velocity = PVector(v_x, v_y)
        # Farbe
        self.color = random.choice(colorlist)
    
    def show(self):
        arcade.draw_circle_filled(self.position.x, self.position.y, self.radius, self.color)
        arcade.draw_circle_outline(self.position.x, self.position.y, self.radius, arcade.color.BLACK)
    
    def move(self):
        self.position.add(self.velocity)
    
        if (self.position.x > WIDTH - self.radius) or (self.position.x < self.radius):
            self.velocity.x *= -1
        if (self.position.y > HEIGHT - self.radius) or (self.position.y < self.radius):
            self.velocity.y *= -1

class BouncingBall(arcade.Window):
    
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(((149, 224, 245)))
        self.balls = []
        for _ in range(NO_BALLS):
            self.balls.append(Ball())
    
    def on_draw(self):
        arcade.start_render()
        
        for ball in self.balls:
            ball.show()
    
    def on_update(self, delta_time):
        
        for ball in self.balls:
            ball.move()

BouncingBall()
arcade.run()
