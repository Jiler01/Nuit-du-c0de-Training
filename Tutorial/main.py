import pyxel as px
from vaisseau import Vaisseau
from enemi import Enemi
from explosion import Explosion
from collide import collide

class App:
    def __init__(self,fps=60,window_size:dict={"x":128 ,"y":128}):
        self.f = open("bestscore.dat","r")
        self.bestscore = int(self.f.readline())
        self.vaisseau = Vaisseau(vies=3)
        self.enemis = []
        self.explosions = []
        self.score = 0
        self.s = fps
        self.passedAlert = 0
        self.window_size = window_size

        px.init(self.window_size["x"], self.window_size["y"], title="My Fist App",fps=fps)
        px.load("PYXEL_RESSOURCE_FILE.pyxres")
        px.run(self.update, self.draw)

    def update(self):
        if self.vaisseau.vies>=0:
            self.vaisseau.update()

            for explosion in self.explosions:
                if explosion.update():
                    self.explosions.remove(explosion)

            
            for frame_num,(speed,u,v) in {3:(0.25,16,0) , 3**2:(0.5,16,8), 3**4:(1,24,0)}.items(): #3**4:(1.5,px.COLOR_PURPLE)}
                if px.frame_count % self.s*frame_num == 0:
                    self.enemis.append(Enemi(speed,u,v))

            for enemi in self.enemis:
                if collide(enemi, self.vaisseau,type="rectangle").happens:
                    self.vaisseau.vies-=1
                    self.enemis.remove(enemi)
                    self.explosions.append(Explosion(enemi.x+enemi.w/2,enemi.y+enemi.h/2,12,6,px.COLOR_PURPLE))
                    self.explosions.append(Explosion(self.vaisseau.x+self.vaisseau.w/2,self.vaisseau.y+self.vaisseau.h/2,12,6,px.COLOR_YELLOW))
                    self.passedAlert = 5  
                if enemi.y>self.window_size["y"]:
                    self.vaisseau.vies-=1
                    try: self.enemis.remove(enemi)
                    except ValueError: pass
                    self.passedAlert = 5
                for tir in self.vaisseau.tirs:      
                    if collide(tir,enemi,type="rectangle").happens:
                        try: self.enemis.remove(enemi)
                        except ValueError: print("Error")
                        self.vaisseau.tirs.remove(tir)
                        self.score +=1
                        self.explosions.append(Explosion(enemi.x+enemi.w,enemi.y+enemi.h,12,6,px.COLOR_PURPLE))
                enemi.update()

        elif px.btn(px.KEY_TAB):
            self.score = 0
            self.vaisseau = Vaisseau(vies=3)
            self.enemis = []
            self.explosions = []
            self.passedAlert = 0

        

    def draw(self):
        px.cls(0)
        if self.vaisseau.vies>=0:

            for explosion in self.explosions:
                explosion.draw()
            self.vaisseau.draw()
            for enemi in self.enemis:
                enemi.draw()
            px.text(5,5, 'VIES:'+ str(self.vaisseau.vies), 7)
            px.text(5,15, 'SCORE:'+ str(self.score), 7)

            if self.passedAlert != 0:
                px.rectb(0,0,self.window_size["x"],self.window_size["y"],px.COLOR_RED)
                self.passedAlert -= 1
        else:
            px.text(5,5, f'GAME OVER\nSCORE: {self.score}', 7)
            px.text(10,120,"PRESS TAB TO REPLAY",px.COLOR_WHITE)
            if self.bestscore < self.score:
                self.f = open("bestscore.dat","w")
                self.f.write(str(self.score))
                self.f.close
                px.text(5,25,"NEW BESTSCORE !!",px.COLOR_LIME)
                
        
App()                        
