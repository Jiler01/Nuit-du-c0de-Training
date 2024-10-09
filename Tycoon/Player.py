import pyxel as px
from MyTools import DATA
import os

class Player:
    def __init__(self, x, y):
        self.name = os.environ["LOGNAME"].capitalize()
        print("a")

        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

        self.wallet = DATA("Player.wallet",default={"gallions":0,"noises":0,"mornilles":0})

        self.skins = {"0": {"left":(0,0),  "right":(8,0)},
                      "10":{"left":(0,8),  "right":(8,8)},
                      "20":{"left":(0,16), "right":(8,16)}}
        self.eyeSide = "right"

        self.xp = 0        
        self.__lastxp = 125
        self.level = 0

        self.flags = {"levelup":0}
        
    def update(self,App):
        if px.btn(px.KEY_LEFT):
            self.eyeSide = "left"
            if (self.x>0) :self.x -= 2
        if px.btn(px.KEY_RIGHT):
            self.eyeSide = "right"
            if self.x+self.h<App.windowSize["x"]: self.x += 2
        if px.btn(px.KEY_UP) and self.y>0:
            self.y -= 2
        if px.btn(px.KEY_DOWN) and self.y+self.h<App.windowSize["y"]:
            self.y += 2

        if self.xp >= self.__lastxp*2:
            self.__lastxp = self.__lastxp *2
            self.level += 1
            self.on("levelup")
            self.xp = self.xp - self.__lastxp

    def draw(self):
        for levelrequired in self.skins.keys():
            if self.level >= int(levelrequired):
                todraw = self.skins[levelrequired]

        u,v = todraw[self.eyeSide]
        px.blt(self.x,self.y,0,u,v,8,8,px.COLOR_BLACK)

    def on(self, flag:str, val:int=1):
        self.flags[flag] = val
    
    def off(self, flag:str, val:int=None):
        if val is None: self.flags[flag] = 0
        else: self.flags[flag]-=val

    def transaction(self, gallions:int=0, noises:int=0, mornilles:int=0):
        if self.wallet.value["gallions"] > gallions and self.wallet.value["noises"] > noises and self.wallet.value["mornilles"] > mornilles:
            self.wallet.value["gallions"] -= gallions
            self.wallet.value["noises"] -= noises
            self.wallet.value["mornilles"] -= mornilles
            return True
        else:
            return False
        
    def save(self):
        self.wallet.push()