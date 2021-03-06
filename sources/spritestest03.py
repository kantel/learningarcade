import random
import os
import arcade

WIDTH = 640
HEIGHT = 480
PLAYER_SPEED = 5

class MyGame(arcade.Window):
    
    def __init__(self, width, height):
        super().__init__(width, height, "Sprite Stage 2")
        arcade.set_background_color(arcade.color.AMAZON)
        
        # Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
        # Erspart einem das Herumgehample in TextMate mit dem os.getcwd()
        # und os.path.join()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
    
    def setup(self):
        # Spieler
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("images/ftr2_fr1.gif")
        self.player_sprite.center_x = 320
        self.player_sprite.center_y = 240
        self.player_list.append(self.player_sprite)
        
        # Mauer
        self.wall_list = arcade.SpriteList()
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

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
    
    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.wall_list.draw()
    
    def update(self, delta_time):
        self.physics_engine.update()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_SPEED
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    game = MyGame(WIDTH, HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
    