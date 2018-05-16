import random
import arcade

WIDTH = 600
HEIGTH = 600

class MyGame(arcade.Window):
    
    def __init__(self):
        super().__init__(WIDTH, HEIGTH, "Sprite Stage 1")
    
    def on_draw(self):
        arcade.start_render()

def main():
    wn = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()
    