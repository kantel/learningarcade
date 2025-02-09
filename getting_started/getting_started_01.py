"""
Simple Platformer Game with Arcade
"""
import arcade

# Constants
WINDOW_WIDTH = 840
WINDOW_HEIGHT = 360
WINDOW_TITLE = "Erste Schritte mit Arcade 3.0"

TILE_SCALING = 0.5
TILE_SIZE = 32

PLAYER_SPEED = 5
GRAVITY = 1
PLAYER_JUMP = 20



class GameWorld(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        
        # Variable to hold our texture for our player
        self.player_texture = None
        
        # Separate variable that holds the player sprite
        self.player_sprite = None
        
        # SpriteList for our player
        self.player_list = None
        
        # SpriteList for our boxes and ground
        self.wall_list = None

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        
        self.player_texture = arcade.load_texture("data/gameboy_idle.png")
        
        self.player_sprite = arcade.Sprite(self.player_texture, scale = 0.65)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = WINDOW_HEIGHT + 100
        
        # SpriteList for our player
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        
        self.wall_list = arcade.SpriteList(use_spatial_hash = True)
        
        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, WINDOW_WIDTH, TILE_SIZE):
            wall = arcade.Sprite("data/grass001.png", scale = TILE_SCALING)
            wall.center_x = x
            wall.center_y = TILE_SIZE/2
            self.wall_list.append(wall)
        
        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[480, 48], [240, 48], [720, 48]]
        
        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite("data/box01.png", scale = TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)
        
        # Create a Platformer Physics Engine.
        # This will handle moving our player as well as collisions between
        # the player sprite and whatever SpriteList we specify for the walls.
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, walls=self.wall_list, gravity_constant=GRAVITY
        )

        # self.background_color = arcade.csscolor.CORNFLOWER_BLUE
        self.background_color = (128, 128, 128, 255)

    def on_draw(self):
        """Render the screen."""

        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()

        # Code to draw other things will go here
        self.wall_list.draw()
        self.player_list.draw()
    
    def on_update(self, delta_time):
        """Movement and Game Logic"""

        # Move the player using our physics engine
        self.physics_engine.update()
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        
        if key == arcade.key.ESCAPE:
            self.setup()
        
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        """Called whenever a key is released."""
        
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

def main():
    """Main function"""
    window = GameWorld()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()