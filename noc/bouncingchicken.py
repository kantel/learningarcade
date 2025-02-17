"""
Bouncing Chicken
"""
import arcade
from pvector import PVector

# Constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
WINDOW_TITLE = "Bouncing Chicken"

# Create a window class. This is what actually shows up on screen
window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
# Position of the window (optional)
window.set_location(1980, 80)

class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        """ Call the parent class to set up the window """
        super().__init__()
        self.player_texture = None
        self.player_sprite = None
                
    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.player_texture = arcade.load_texture("data/chick.png")
        self.player_sprite = arcade.Sprite(self.player_texture, scale = 0.3)
        self.position = PVector(100, 100)
        self.player_sprite.position = self.position.x, self.position.y
        self.velocity = PVector(2.5, 2)
        self.radius = 20    # ≈ 136 * 0.3 / 2
        
        # SpriteList for our player
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        
        self.background_color = 59, 122, 87, 255

    def on_draw(self):
        """Render the screen."""
        self.clear()        
        self.player_list.draw()
    
    def on_update(self, delta_time):
        """Movement and Game Logic"""
        self.position += self.velocity
        
        if self.position.x > self.width - self.radius or self.position.x < self.radius:
            self.velocity.x *= -1
            
        if self.position.y > self.height - self.radius or self.position.y < self.radius:
            self.velocity.y *= -1
        
        self.player_sprite.position = self.position.x, self.position.y
        
game = GameView()
window.show_view(game)
game.setup()
arcade.run()
