import arcade
from pvector import PVector

WIDTH = 600
HEIGHT = 600
TITLE = "Random Walk with Arcade"

class Walker():
    
    def __init__(self):
        # Position and Velocity
        self.position = PVector(WIDTH/2, HEIGHT/2)
        self.velocity = PVector(0, 0)
        # Farbe
        self.color = (255, 255, 178)
    
    def update(self):
        pass
    
    def draw(self):
        pass
    
arcade.open_window(WIDTH, HEIGHT, TITLE)
arcade.set_background_color((43, 62, 80))

walker = Walker()

arcade.start_render()

# All drawings here
for i in range(5000):
    walker.update()
    walker.draw()

arcade.finish_render()

arcade.run()