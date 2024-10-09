import pyxel as px

class Tir:
    def __init__(self,x,y):
        self.x,self.y = x,y
        self.w,self.h = 1,4

    def update(self):
        self.y += -2

    def draw(self):
        px.blt(self.x, self.y, 0, 0, 0, 1, 4, px.COLOR_BLACK) #x,y,w,h,col

class Vaisseau:
    def __init__(self,rate=7,vies=1):
        self.x , self.y = 60,100
        self.w, self.h = 8,8
        self.rate = rate
        self.vies = vies
        
        self.tirs = []

    def update(self):
        if px.btn(px.KEY_RIGHT) and self.x<120:
            self.x += 1.5
        if px.btn(px.KEY_LEFT) and self.x>0:
            self.x += -1.5
        if px.btn(px.KEY_DOWN) and self.y<120:
            self.y += 1.5
        if px.btn(px.KEY_UP) and self.y>0:
            self.y += -1.5
        if px.btn(px.KEY_SPACE) and px.frame_count % self.rate == 0:
            self.tirs.append(Tir(self.x+4,self.y-4))
        for tir in self.tirs:
            tir.update()
    
    def draw(self):
         px.blt(self.x, self.y, 0, 8, 0, 8, 8, px.COLOR_BLACK) #x,y,w,h,col
         for tir in self.tirs:
             tir.draw()
             if tir.y < 0:
                 self.tirs.remove(tir)