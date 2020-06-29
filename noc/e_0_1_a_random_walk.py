import arcade
from pvector import PVector
import random

WIDTH = 600
HEIGHT = 600
TITLE = "Random Walk mit der Arcade-Bibliothek"

class Walker():
    
    def __init__(self):
        # Position and Velocity
        self.location = PVector(WIDTH/2, HEIGHT/2)
        self.prev_location = PVector(WIDTH/2, HEIGHT/2)
        self.velocity = PVector(0, 0)
        # Farbe
        self.color = (255, 255, 178)
        self.count = 0
        self.paused = False
        self.stepsize = 4
    
    def update(self):
        self.prev_location.set(self.location)
        self.count += 1
        if self.count <= 1500:
            self.color = (255, 255, 178)
        elif self.count <= 3000:
            self.color = (254, 204, 92)
        elif self.count <= 4500:
            self.color = (253, 141, 60)
        elif self.count <= 6000:
            self.color = (240, 59, 32)
        elif self.count <= 7500:
            self.color = (189, 0, 38)
        if self.count >= 7500:
            self.paused = True
        roll = random.randint(1, 4)
        if roll == 1:
            self.location.y += self.stepsize
        elif roll == 2:
            self.location.x += self.stepsize
        elif roll == 3:
            self.location.y -= self.stepsize
        elif roll == 4:
            self.location.x -= self.stepsize
            
        
    def draw(self):
        arcade.draw_line(self.prev_location.x, self.prev_location.y,
        self.location.x, self.location.y, self.color, 2)
    

class MyWindow(arcade.Window):
    
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.walker = Walker()
        arcade.set_background_color((43, 62, 80))
        arcade.start_render()
        
    def on_draw(self):
        self.walker.draw()
    
    def on_update(self, delta_time):
        if self.walker.paused:
            return
        self.walker.update()



MyWindow()
arcade.run()