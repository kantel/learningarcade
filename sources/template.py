import arcade as ar

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Arcade Template"

class MyGame (ar.Window):
    
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        ar.set_background_color((43, 62, 80))   # Farben müssen ein Tupel () sein!
        
    def setup(self):
        print("Hallo Arcade!")
    
    def on_draw(self):
        ar.start_render()
    
    def update(self, delta_time):
        pass
        # print("Hallo Update!")

game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
ar.run()