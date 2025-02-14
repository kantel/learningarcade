"""
Arcade Template v2
"""
import arcade

# Constants
WINDOW_WIDTH = 840
WINDOW_HEIGHT = 360
WINDOW_TITLE = "Arcade Herdplatte v2"

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
        self.background_color = arcade.color.AMAZON
        
    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass
    
    def on_draw(self):
        """Render the screen."""
        self.clear()
    
    def on_update(self, delta_time):
        """Movement and Game Logic"""
        pass
    
def main():
    game = GameView()
    window.show_view(game)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
    