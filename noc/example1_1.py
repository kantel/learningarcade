"""
Example 1.1: Bouncing Ball with No Vectors
"""
import arcade

# Constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
WINDOW_TITLE = "Bouncing Ball with No Vectors"

window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
window.set_location(1980, 80)

class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        self.circle_x = 100
        self.circle_y = 100
        self.radius = 24
        self.x_speed = 2.5
        self.y_speed = 2
        self.background_color = 59, 122, 87, 255
            
    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.circle_x, self.circle_y, self.radius, (255, 239, 0, 255))
        arcade.draw_circle_outline(self.circle_x, self.circle_y, self.radius, (0, 0, 0, 255), 2)
    
    def on_update(self, delta_time):
        self.circle_x += self.x_speed
        self.circle_y += self.y_speed
        
        if self.circle_x > self.width - self.radius or self.circle_x < self.radius:
            self.x_speed *= -1
            
        if self.circle_y > self.height - self.radius or self.circle_y < self.radius:
            self.y_speed *= -1    

game = GameView()
window.show_view(game)
arcade.run()

    
