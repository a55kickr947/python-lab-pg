import math
class triangle:
    def __init__(self):
        self.breadth=0
        self.height=0
    def triangle1(self,breadth,height):
        self.breadth=breadth
        self.height=height
    def areatri1(self):
        self.areatri=0.5*self.breadth*self.height
    def tridisplay(self):
        print("area of triangle is:",self.areatri,"square units")
        
class rectangle:
    def __init__(self):
        self.breadth=0
        self.length=0
    def rectangle1(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def arearect1(self):
        self.arearect=self.breadth*self.length
    def rectdisplay(self):
        print("area of rctangle is:",self.arearect,"square units")
class circle:
    def __init__(self):
        self.rad=0
    def circle1(self,rad):
        self.rad=rad
    def areacir1(self):
        self.areacir=self.rad*self.rad*math.pi
    def cirdisplay(self):
        
        
        
