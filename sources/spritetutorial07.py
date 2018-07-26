import arcade as ar
import random as r
import os
import math

# Konstanten
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Arcade Sprite Tutorial Stage 7"

class Coin(ar.Sprite):
    
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.rotate_angle = 0
        
        self.circle_angle = 0      # Winkel in Radians
        self.circle_radius = 0     # Orbit-Radius in Pixeln
        self.circle_speed = 0.008  # Geschwindigkeit in Radians per Frame
        # Zentrum des Orbits
        self.circle_center_x = 0
        self.circle_center_y = 0
    
    def update(self):
        # Neue Position berechnen
        self.center_x = (self.circle_radius*math.sin(self.circle_angle) +
                         self.circle_center_x)
        self.center_y = (self.circle_radius*math.cos(self.circle_angle) +
                         self.circle_center_y)
        self.circle_angle += self.circle_speed
        
        # Rotieren
        self.angle += self.rotate_angle
        if self.angle > 359:
            self.angle -= 360

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
            coin.circle_center_x = r.randrange(SCREEN_WIDTH)
            coin.circle_center_y = r.randrange(SCREEN_HEIGHT)
            coin.rotate_angle = r.randrange(-2, 3)
            coin.circle_radius = r.randrange(10, 200)
            coin.circle_angle = r.random()*2*math.pi
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
            coin.kill()
    
game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
ar.run()
