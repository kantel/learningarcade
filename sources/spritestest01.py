import random
import arcade

WIDTH = 640
HEIGHT = 480

class MyGame(arcade.Window):
    
    def __init__(self, width, height):
        super().__init__(width, height, "Arcade Empty Template")
        arcade.set_background_color(arcade.color.AMAZON)
    
    def setup(self):
        pass
    
    def on_draw(self):
        arcade.start_render()
    
    def update(self, delta_time):
        pass

def main():
    game = MyGame(WIDTH, HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
    