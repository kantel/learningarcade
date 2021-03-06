import random
import os
import arcade

WIDTH = 640
HEIGHT = 480
PLAYER_SPEED = 5

class MyGame(arcade.Window):
    
    def __init__(self, width, height):
        super().__init__(width, height, "Sprite Stage 3")
        arcade.set_background_color(arcade.color.AMAZON)
        
        # Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
        # Erspart einem das Herumgehample in TextMate mit dem os.getcwd()
        # und os.path.join()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
    
    def setup(self):
        # Sprite Lists
        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        
        # Player
        self.player = arcade.AnimatedWalkingSprite()
        
        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture("images/ftr2_rt1.gif"))
        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(arcade.load_texture("images/ftr2_lf1.gif"))
        self.player.stand_up_textures = []
        self.player.stand_up_textures.append(arcade.load_texture("images/ftr2_bk1.gif"))
        self.player.stand_down_textures = []
        self.player.stand_down_textures.append(arcade.load_texture("images/ftr2_fr1.gif"))
        self.player.walk_right_textures = []
        self.player.walk_right_textures.append(arcade.load_texture("images/ftr2_rt1.gif"))
        self.player.walk_right_textures.append(arcade.load_texture("images/ftr2_rt2.gif"))
        self.player.walk_left_textures = []
        self.player.walk_left_textures.append(arcade.load_texture("images/ftr2_lf1.gif"))
        self.player.walk_left_textures.append(arcade.load_texture("images/ftr2_lf2.gif"))
        self.player.walk_up_textures = []
        self.player.walk_up_textures.append(arcade.load_texture("images/ftr2_bk1.gif"))
        self.player.walk_up_textures.append(arcade.load_texture("images/ftr2_bk2.gif"))
        self.player.walk_down_textures = []
        self.player.walk_down_textures.append(arcade.load_texture("images/ftr2_fr1.gif"))
        self.player.walk_down_textures.append(arcade.load_texture("images/ftr2_fr2.gif"))
        
        self.player.texture_change_distance = 20     #20
        
        self.player.center_x = 320
        self.player.center_y = 240
        self.all_sprites_list.append(self.player)
        
        # Mauer
        wall = arcade.Sprite("images/wall.png")
        wall.center_x = 200
        wall.center_y = 200
        self.wall_list.append(wall)
        
        wall = arcade.Sprite("images/wall.png")
        wall.center_x = 232
        wall.center_y = 200
        self.wall_list.append(wall)
        
        wall = arcade.Sprite("images/wall.png")
        wall.center_x = 264
        wall.center_y = 200
        self.wall_list.append(wall)
        
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.wall_list)
    
    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()
        self.wall_list.draw()
    
    def update(self, delta_time):
        # self.all_sprites_list.update()
        self.all_sprites_list.update_animation()
        self.physics_engine.update()

    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = PLAYER_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

def main():
    game = MyGame(WIDTH, HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
    