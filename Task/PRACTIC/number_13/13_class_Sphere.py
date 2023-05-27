
import math

class Sphere:
    def __init__(self, radius=1.0, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def getVolume(self):
        self.volume = (4 / 3) * math.pi * math.pow(self.radius, 3)
        return self.volume

    def getSquare(self):
        self.square = math.pi * 4 * math.pow(self.radius, 2)

    def getRadius(self):
        return self.radius
