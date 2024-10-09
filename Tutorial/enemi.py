import pyxel as px
from random import randint

class Enemi:
    def __init__(self,speed,u,v):
        self.x = randint(0, px.width - 8)
        self.y = 0
        self.w,self.h = 8,8
        self.speed = speed
        self.alive = True
        self.u = u
        self.v = v

    def draw(self):
        px.blt(self.x, self.y, 0, self.u, self.v, 8, 8, px.COLOR_BLACK) #x,y,w,h,col

    def update(self):
        self.y += self.speed