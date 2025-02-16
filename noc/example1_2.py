"""
Example 1.2: Bouncing Ball with Vectors
"""
import arcade
from pvector import PVector

# Constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
WINDOW_TITLE = "Bouncing Ball with Vectors"

window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
window.set_location(1980, 80)

class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        self.position = PVector(100, 100)
        self.velocity = PVector(2.5, 2)
        self.radius = 24
        self.background_color = 59, 122, 87, 255
            
    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.position.x, self.position.y, self.radius, (255, 239, 0, 255))
        arcade.draw_circle_outline(self.position.x, self.position.y, self.radius, (0, 0, 0, 255), 2)
    
    def on_update(self, delta_time):
        self.position += self.velocity
        
        if self.position.x > self.width - self.radius or self.position.x < self.radius:
            self.velocity.x *= -1
            
        if self.position.y > self.height - self.radius or self.position.y < self.radius:
            self.velocity.y *= -1    

game = GameView()
window.show_view(game)
arcade.run()

    

