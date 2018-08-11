import arcade as ar
import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Arcade Rogue Tutorial Stage 2"
SPEED = 5
TILE_SIZE = 32
t2 = TILE_SIZE/2

class MyGame (ar.Window):
    
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        ar.set_background_color((ar.color.AMAZON))
        
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
        self.wall_list = ar.SpriteList()
        

        # Player-Info
        self.player_sprite = ar.Sprite("images/character.png")
        self.player_sprite.center_x = 10*TILE_SIZE + t2
        self.player_sprite.center_y = 7*TILE_SIZE + t2
        self.player_list.append(self.player_sprite)
        
        # Mauer
        wall = ar.Sprite("images/wall.png")
        wall.center_x = 5*TILE_SIZE + t2
        wall.center_y = 3*TILE_SIZE + t2
        self.wall_list.append(wall)
        
        wall = ar.Sprite("images/wall.png")
        wall.center_x = 4*TILE_SIZE + t2
        wall.center_y = 3*TILE_SIZE + t2
        self.wall_list.append(wall)
        
        # Eine einfache Physic Engine zur Kollisionserkennung
        self.physics_engine = ar.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        ar.start_render()
        self.player_list.draw()
        self.wall_list.draw()
    
    def update(self, delta_time):
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == ar.key.UP:
            self.player_sprite.change_y = SPEED
        elif key == ar.key.DOWN:
            self.player_sprite.change_y = -SPEED
        elif key == ar.key.LEFT:
            self.player_sprite.change_x = -SPEED
        elif key == ar.key.RIGHT:
            self.player_sprite.change_x = SPEED

    def on_key_release(self, key, modifiers):
        if key == ar.key.UP or key == ar.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == ar.key.LEFT or key == ar.key.RIGHT:
            self.player_sprite.change_x = 0



game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
ar.run()