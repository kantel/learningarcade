"""
Starting Template
"""
import arcade
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
SCREEN_TITLE = "Side Scroller 1"

def make_clouds():
    shape_list = arcade.ShapeElementList()
    shape_list.center_x = SCREEN_WIDTH/2
    for i in range(4):
        if i == 0:
            x = shape_list.center_x
            y = SCREEN_HEIGHT - 100                
        elif i == 1:
            x = shape_list.center_x
            y = SCREEN_HEIGHT - 150
        elif i == 2:
            x = shape_list.center_x - 50
            y = SCREEN_HEIGHT - 150
        else:
            x = shape_list.center_x + 50
            y = SCREEN_HEIGHT - 150
        shape = arcade.create_ellipse_filled(x, y, 50, 50, (255, 255, 255))
        shape_list.append(shape)
    return shape_list

def make_big_hills():
    shape_list = arcade.ShapeElementList()
    for i in range(3):
        shape = arcade.create_ellipse_filled(i*400, 60, 200, 200, (129, 122, 198))
        shape_list.append(shape)
    return shape_list

def make_small_hills():
    shape_list = arcade.ShapeElementList()
    for i in range(6):
        shape = arcade.create_ellipse_filled(i*200, 60, 100, 100, (146, 82, 161))
        shape_list.append(shape)
    return shape_list
    
class MyGame(arcade.Window):
    """
    Main application class.
    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        # Wolken
        self.clouds = make_clouds()
        # Große Hügel
        self.big_hills = make_big_hills()
        #Kleine Hügel
        self.small_hills = make_small_hills()
        arcade.set_background_color((49, 197, 244))
        
        self.set_mouse_visible(False)
        
        # Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
        # Erspart einem das Herumgehample in TextMate mit dem os.getcwd()
        # und os.path.join()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
    def setup(self):
        # Boden
        self.bottom_ground = arcade.create_rectangle_filled(SCREEN_WIDTH/2, 20, SCREEN_WIDTH, 40,
                             (248, 158, 80))
        self.top_ground = arcade.create_rectangle_filled(SCREEN_WIDTH/2, 50, SCREEN_WIDTH, 20,
                          (98, 199, 119))

    def on_draw(self):
        arcade.start_render()
        self.clouds.draw()
        self.big_hills.draw()
        self.small_hills.draw()
        self.bottom_ground.draw()
        self.top_ground.draw()
        

    def on_update(self, delta_time):
        # self.clouds.center_x -= 0.5
        if self.clouds.center_x < -SCREEN_WIDTH/2 - 150:
            self.clouds.center_x = SCREEN_WIDTH/2 + 150
        # self.big_hills.center_x -= 1.0
        # self.small_hills.center_x -= 1.5
       

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.ESCAPE:
            # Quit immediately
            arcade.close_window()



game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()
