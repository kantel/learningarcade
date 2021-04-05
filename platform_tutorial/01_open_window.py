# Platformer Game nach https://arcade.academy/examples/platform_tutorial/step_01.html - step_03.html
# Stage 1: Open a Window with ground and crates and add a moving Character

import arcade
import os

# Konstanten
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Arcade Platformer (Stage 1)"

# Skalierungs-Konstanten
CHARACTER_SCALING = 1
TILE_SCALING = 1

# Geschwindigkeit des Players in Pixel per Frame
PLAYER_MOVEMENT_SPEED = 5

# Farben
BLUE = (49, 197, 244)


class MyGame(arcade.Window):
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.wall_list = None
        self.player_list = None
        
        # Separate variable that holds the player sprite
        self.player_sprite = None
        
        arcade.set_background_color(BLUE)
    
    def setup(self):
        
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash = True)
        
        # Set up the player
        player_image = os.path.join("images", "player_idle.png")
        self.player_sprite = arcade.Sprite(player_image, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.bottom = 64
        self.player_list.append(self.player_sprite)
        
        # Create the ground
        for x in range(0, SCREEN_WIDTH + 1, 64):
            wall = arcade.Sprite(os.path.join("images", "grass_mid.png"), TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)
        
        # Put some crates on the ground
        coordinates = [[488, 96], [232, 96], [744, 96]]
        for coordinate in coordinates:
            wall = arcade.Sprite(os.path.join("images", "box_crate.png"), TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)
        
        # Create the »physics engine«
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
    
    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
    
    def on_update(self, delta_time):
        self.physics_engine.update()
        

window = MyGame()
window.setup()
arcade.run()