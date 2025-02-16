"""
Example 1.2: Bouncing Ball with Vectors (Numpy Version)
"""
import arcade
import numpy as np

# Constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
WINDOW_TITLE = "Bouncing Ball with Vectors (Numpy Version)"

window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
window.set_location(1980, 80)

class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        self.position = np.array([100, 100], dtype=np.float64)
        self.velocity = np.array([2.5, 2], dtype=np.float64) 
        self.radius = 24
        self.background_color = 59, 122, 87, 255
            
    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.position[0], self.position[1], self.radius, (255, 239, 0, 255))
        arcade.draw_circle_outline(self.position[0], self.position[1], self.radius, (0, 0, 0, 255), 2)
    
    def on_update(self, delta_time):
        self.position += self.velocity
        
        if self.position[0] > self.width - self.radius or self.position[0] < self.radius:
            self.velocity[0] *= -1
            
        if self.position[1] > self.height - self.radius or self.position[1] < self.radius:
            self.velocity[1] *= -1    

game = GameView()
window.show_view(game)
arcade.run()

    

