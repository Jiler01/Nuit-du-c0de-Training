import pyxel as px

class Explosion:
    def __init__(self,x,y,finish_r,r,color:int):
        self.x=x
        self.y=y
        self.finish_r = finish_r
        self.r = r
        self.color = color
    def update(self):
        if self.r == self.finish_r:
            ret = True
        else:
            ret = False
        self.r += 1
        return ret
    def draw(self):
        px.circb(self.x,self.y,self.r,col=self.color)