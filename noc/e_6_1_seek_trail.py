import arcade
from pvector import PVector

WIDTH = 640
HEIGHT = 360
TITLE = "Seeking a Target"

class Viehicle():
    
    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, 0)
        self.location = PVector(x, y)
        self.color = (98, 199, 119)
        self.r = 8.0
        self.maxspeed = 5
        self.maxforce = 0.1
        self.d = 25

def draw():
    pass