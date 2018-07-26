import arcade as ar
import random as r
import os

# Konstanten
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Arcade Sprite Tutorial Stage 6"

class Coin(ar.Sprite):
    
    def update(self):
        self.center_y -= 1
        
        # Wenn die Münzen das Spielfeld verlassen, werden sie an zufälliger Position
        # am oberen Spielfeldrand neu positionert
        if self.top < 0:
            self.reset()
    
    def reset(self):
        self.center_y = r.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = r.randrange(SCREEN_WIDTH)

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
        
    def setup(self):
        # Sprite-Listen
        self.player_list = ar.SpriteList()
        self.coin_list = ar.SpriteList()

        # Player-Info
        self.player_sprite = ar.Sprite("images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        
        # Münzen
        for i in range(COIN_COUNT):
            coin = Coin("images/coin_01.png", SPRITE_SCALING_COIN)
            coin.center_x = r.randrange(SCREEN_WIDTH)
            coin.center_y= r.randrange(SCREEN_HEIGHT)
            self.coin_list.append(coin)
        
        # Score
        self.score = 0
    
    def on_draw(self):
        ar.start_render()
        
        self.coin_list.draw()
        self.player_list.draw()
        
        output = f"Score: {self.score}"
        ar.draw_text(output, 10, SCREEN_HEIGHT - 20, ar.color.WHITE, 14)
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
    
    def update(self, delta_time):
        # Animation und Spiellogik
        self.coin_list.update()
        
        # Erstelle einer Liste aller Münzen, die mit dem Spieler kollidieren
        coins_hit_list = ar.check_for_collision_with_list(self.player_sprite, self.coin_list)
        
        # Lösche alle Münzen aus dieser Liste
        for coin in coins_hit_list:
            self.score += 1
            coin.reset()
    
game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
ar.run()