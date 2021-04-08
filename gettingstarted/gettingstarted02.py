# Getting started with the Arcade Game Library
# Stage 1: Hello Walking Alien
import arcade
import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "👽 Hello Walking Älien 👽"

RIGHT_FACING = 0
LEFT_FACING = 1

PLAYER_SPEED = 7

# Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)
image_path = os.path.join(file_path, "images")

def load_texture_pair(file_path):
    return[arcade.load_texture(file_path), arcade.load_texture(file_path, flipped_horizontally = True)]

class Alien(arcade.Sprite):
    
    def __init__(self):
        super().__init__()
        
        # Default to face-right
        self.character_face_direction = RIGHT_FACING
        self.current_texture = 0
        
        # Load textures for idle standing
        self.idle_texture_pair = load_texture_pair(os.path.join(image_path, "alien.png"))
        # Load texture pairs for walking
        self.walk_textures = []
        for i in range(2):
            texture = load_texture_pair(os.path.join(image_path, f"alien_walk{i}.png"))
            self.walk_textures.append(texture)
        # Set the initial texture
        self.texture = self.idle_texture_pair[0]
        # Set the hitbox
        self.set_hit_box(self.texture.hit_box_points)
    
    def update_animation(self, delta_time: float = 1/60):
        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING
    
        # Idle animation
        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return
    
        # Walking animation
        self.current_texture += 1
        # self.current_texture = int(self.current_texture)
        if self.current_texture >= 2:
            self.current_texture = 0
        self.texture = self.walk_textures[self.current_texture][self.character_face_direction]
            

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
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
        self.player_sprite = Alien()
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)
        
        # Set up the crate
        for i in range(5):
            wall = arcade.Sprite(os.path.join(image_path, "box_crate.png"))
            wall.center_x = 150 + i*64
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
        self.player_list.update_animation(delta_time)
        
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
