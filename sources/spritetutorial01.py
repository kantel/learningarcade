import arcade as ar
import random as r
import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Arcade Sprite Tutorial Stage 1"

class MyGame (ar.Window):
    
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        ar.set_background_color(ar.color.AMAZON)
        
        # Hier wird die Maus im Spielefenster versteckt
        self.set_mouse_visible(False)
        
        # Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
        # Erspart einem das Herumgehample in TextMate mit dem os.getcwd()
        # und os.path.join()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
    def on_draw(self):
        ar.start_render()
    
game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
ar.run()