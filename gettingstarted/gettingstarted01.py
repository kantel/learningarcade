# Getting started with the Arcade Game Library
# Stage 1: Hello Alien
import arcade
import os

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_TITLE = "👽 Hello Älien 👽"

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
        file_path = os.path.dirname(os.path.abspath(__file__))
        self.image_path = os.path.join(file_path, "images")
        os.chdir(file_path)
        
        # If you have sprite lists, you should create them here,
        # and set them to None
        self.player_list = None
        self.wall_list = None
        self.player_speed = 5
        
        self.player_sprite = None
        
        arcade.set_background_color((0, 80, 125))

    def setup(self):
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        
        # Set up the player
        alien_image = os.path.join(self.image_path, "alien.png")
        self.player_sprite = arcade.Sprite(alien_image)
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)
        
        # Set up the crate
        wall = arcade.Sprite(os.path.join(self.image_path, "box_crate.png"))
        wall.center_x = 200
        wall.center_y = 150
        self.wall_list.append(wall)

        # Create the »physics engine«
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        
        # Call draw() on all your sprite lists below
        self.wall_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        self.physics_engine.update()
        
        # Border checking
        if self.player_sprite.left >= SCREEN_WIDTH:
            self.player_sprite.right = 0
        elif self.player_sprite.right <= 0:
            self.player_sprite.left = SCREEN_WIDTH
        if self.player_sprite.bottom >= SCREEN_HEIGHT:
            self.player_sprite.top = 0
        elif self.player_sprite.top <= 0:
            self.player_sprite.bottom = SCREEN_HEIGHT
            
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = self.player_speed
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -self.player_speed
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -self.player_speed
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = self.player_speed
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

game = MyGame()
game.setup()
arcade.run()
