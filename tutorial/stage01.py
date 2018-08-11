import arcade as ar
import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Arcade Rogue Tutorial Stage 1"
TILE_SIZE = 32
t2 = TILE_SIZE/2

class MyGame (ar.Window):
    
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        ar.set_background_color((ar.color.AMAZON))   # Farben müssen ein Tupel () sein!
        
        # Hier wird die Maus im Spielefenster versteckt
        self.set_mouse_visible(False)
        
        # Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
        # Erspart einem das Herumgehample in TextMate mit dem os.getcwd()
        # und os.path.join()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
    def setup(self):
        # Sprite-Listen
        self.player_list = ar.SpriteList()

        # Player-Info
        self.player_sprite = ar.Sprite("images/character.png")
        self.player_sprite.center_x = 10*TILE_SIZE + t2
        self.player_sprite.center_y = 7*TILE_SIZE + t2
        self.player_list.append(self.player_sprite)
        
    def on_draw(self):
        ar.start_render()
        
        self.player_list.draw()
    
    def update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        if key == ar.key.UP:
            self.player_sprite.center_y += TILE_SIZE
        elif key == ar.key.DOWN:
            self.player_sprite.center_y -= TILE_SIZE
        elif key == ar.key.LEFT:
            self.player_sprite.center_x -= TILE_SIZE
        elif key == ar.key.RIGHT:
            self.player_sprite.center_x += TILE_SIZE


game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
ar.run()