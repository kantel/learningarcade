# Platformer Game nach https://arcade.academy/examples/platform_tutorial/step_04.html - step_07.html
# Stage 1: Add gravity, scrolling, collect items and show the score

import arcade
import os

# Konstanten
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Arcade Platformer (Stage 2)"

# Skalierungs-Konstanten
CHARACTER_SCALING = 1
TILE_SCALING = 1
ITEM_SCALING = 1

# Geschwindigkeit des Players in Pixel per Frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# How many pixels to keep as a minimum margin between the player
# and the egde of the screen
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100

# Farben
BLUE = (49, 197, 244)
WHITE = (255, 255, 255)


class MyGame(arcade.Window):
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.wall_list = None
        self.item_list = None
        self.player_list = None
        
        # The physics engine
        self.physics_engine = None
                
        # Separate variable that holds the player sprite
        self.player_sprite = None
                
        arcade.set_background_color(BLUE)
    
    def setup(self):
        
        # Call these to restart the game
        
        # Keep track of the score
        self.score = 0
        
        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0
    
        
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash = True)
        self.item_list = arcade.SpriteList()
        
        # Set up the player
        player_image = os.path.join("images", "player_idle.png")
        self.player_sprite = arcade.Sprite(player_image, CHARACTER_SCALING)
        self.player_sprite.center_x = 32
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
        
        # Place some diamonds
        for x in range (96, SCREEN_WIDTH + 1, 256):
            diamond = arcade.Sprite(os.path.join("images", "diamond_gold.png"), ITEM_SCALING)
            diamond.center_x = x
            diamond.center_y = 96
            self.item_list.append(diamond)
        
        # Create the »physics engine«
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)
    
    def on_draw(self):
        arcade.start_render()
        
        # Draw our sprites
        self.wall_list.draw()
        self.item_list.draw()
        self.player_list.draw()
        
        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, SCREEN_HEIGHT - 36, WHITE, 24)
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
    
    def on_update(self, delta_time):
        self.physics_engine.update()
        
        # See if we hit any items
        item_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.item_list)
        # Loop throug each item we it (if any) and remove it
        for item in item_hit_list:
            item.remove_from_sprite_lists()
            self.score += 1
        
        # Manage Scrolling
        #Track if we need to change the viewport
        changed = False
        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True
        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True
        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True
        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True
        
        if changed:
            # Only scroll to integers
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)
            # Do the scrolling
            arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left,
                                self.view_bottom, SCREEN_HEIGHT + self.view_bottom)

window = MyGame()
window.setup()
arcade.run()