import pyxel as px
from Player import Player

class App:
    def __init__(self,fps=60,window_size:dict={"x":120 ,"y":120}):
        px.init(window_size["x"],window_size["y"],fps=fps,title="Little Tycoon")

        self.windowSize = window_size
        
        self.player = Player(60,60)

        px.load("PYXEL_RESOURCE_FILE.pyxres")
        px.run(self.update, self.draw)

    def update(self):
        self.player.update(self)

    def draw(self):
        px.cls(px.COLOR_BLACK)
        #px.bltm(0,0,0,0,0,256,256,px.COLOR_BLACK)
        px.text(5,5,f"{self.player.name} | Level: {self.player.level}",px.COLOR_WHITE)
        self.player.draw()

App()