"""
Simple Platformer Game with Arcade, Stage 2
"""
import arcade

# Constants
WINDOW_WIDTH = 944
WINDOW_HEIGHT = 360
WINDOW_TITLE = "Erste Schritte mit Arcade 3.0, Stage 2"

TILE_SCALING = 0.5
TILE_SIZE = 32
BL = -TILE_SIZE/2                  # Border left
BR = WINDOW_WIDTH + TILE_SIZE/2    # Border right
DIAMOND_SCALING = 0.5

PLAYER_SPEED = 5
GRAVITY = 1
PLAYER_JUMP = 20

# Create a window class. This is what actually shows up on screen
window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
# Position of the window (optional)
window.set_location(1980, 80)


class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class to set up the window
        super().__init__()
        self.background_color = arcade.color.AMAZON
        
        # Variable to hold our texture for our player
        self.player_texture = None
        
        # Separate variable that holds the player sprite
        self.player_sprite = None
        
        # SpriteList for our player
        self.player_list = None
        
        # SpriteList for our boxes and ground
        self.wall_list = None
        
        # SpriteList for diamonds the player can collect
        self.diamond_list = None
        
        # This variable will store our score as an integer.
        self.score = 0
        
        # This variable will store the text for score that we will draw to the screen.
        self.score_text = None
        
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

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
        self.diamond_list = arcade.SpriteList(use_spatial_hash=True)
        
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
            
        # Level border
        border_list = [[BL, 48], [BL, 80], [BL, 112], [BL, 144], [BL, 176],
                       [BL, 208], [BL, 240], [BL, 272], [BL, 304], [BL, 336], [BL, 368],
                       [BR, 48], [BR, 80], [BR, 112], [BR, 144], [BR, 176],
                       [BR, 208], [BR, 240], [BR, 272], [BR, 304], [BR, 336], [BR, 368]]
        for border in border_list:
            wall = arcade.Sprite("data/box01.png", scale = TILE_SCALING)
            wall.position = border
            self.wall_list.append(wall)
            
        
        # Add diamonds to the world
        for x in range(120, WINDOW_WIDTH, 240):
            diamond = arcade.Sprite("data/diamond01.png", scale = DIAMOND_SCALING)
            diamond.center_x = x
            diamond.center_y = 192
            self.diamond_list.append(diamond)
        
        # Create a Platformer Physics Engine.
        # This will handle moving our player as well as collisions between
        # the player sprite and whatever SpriteList we specify for the walls.
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, walls=self.wall_list, gravity_constant=GRAVITY
        )
        
        # Reset our score to 0
        self.score = 0

        # Initialize our arcade.Text object for score
        self.score_text = arcade.Text(f"Score: {self.score}", x = 10, y = 5)

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
        self.diamond_list.draw()
        self.player_list.draw()
        
        # Draw our Score
        self.score_text.draw()
    
    def on_update(self, delta_time):
        """Movement and Game Logic"""

        # Move the player using our physics engine
        self.physics_engine.update()
        
        # See if we hit any diamonds
        diamond_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.diamond_list
        )

        # Loop through each coin we hit (if any) and remove it
        for diamond in diamond_hit_list:
            # Remove the coin
            diamond.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)
            self.score += 75
            self.score_text.text = f"Score: {self.score}"
        
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
                 
        if key == arcade.key.ESCAPE:
            self.setup()
        
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP
                arcade.play_sound(self.jump_sound)

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
    game = GameView()
    window.show_view(game)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()