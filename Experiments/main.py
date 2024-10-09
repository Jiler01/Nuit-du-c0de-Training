import pyxel as px
import os,json
import numpy as np

class Data:
    def __init__(self,name:str,*,default:dict={}):
        self.path = f"AppData/{name}.json"

        if not os.path.exists(self.path):
            if not os.path.exists("AppData"):
                os.makedirs("AppData")
            self.value = default
            self.push()

        self.pull()

    def push(self):
        with open(self.path,"w") as file:
            json.dump(self.value,file,indent=4,sort_keys=True)

    def pull(self):
        with open(self.path,"r") as file:
            self.value = json.load(file)
        

class Entity:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.update_relatives()

    def setter_dec(setter):
        def wrapper(self,value):
            setter(self,value)
            self.update_relatives()
        return wrapper

    @setter_dec
    def set_top(self,value):
        self.y = value

    @setter_dec
    def set_bottom(self,value):
        self. y = value - self.h

    @setter_dec
    def set_right(self,value):
        self.x = value

    @setter_dec
    def set_left(self,value):
        self.x = value - self.w

    def update_relatives(self):
        self.top = self.y
        self.bottom = self.y + self.h
        self.right = self.x + self.w
        self.left = self.x

    def overX(self,rect):
        return rect.right >= self.left and rect.left <= self.right

    def overY(self,rect):
        return rect.top <= self.bottom and rect.bottom >= self.top

    def collide(self,rect):
        return self.overY(rect) and self.overX(rect)
    
class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 8, 8)
        self.reset_jump()
        self.reset_gravity()
        self.current_jumps = []

    def reset_gravity(self):
        self.gravity_token = 0

    def reset_jump(self):
        self.left_jumps = 2

    def out_getter(self,rect,cases_to_reset_gravity:list[str],cases_to_reset_jump:list[str]):
        pass

    def handle_gravity(self,game):
        if self.collide(game.floor):
            self.set_bottom(game.floor.top)
            self.reset_gravity()
            self.reset_jump()
            return np.array([0,0])

        self.gravity_token +=  game.GRAVITY
        return np.array([0,self.gravity_token])

    def handle_user_jumps(self):
        if px.btnp(px.KEY_SPACE) and self.left_jumps > 0:
            self.left_jumps -= 1
            return self.jump(True,40)
        return self.jump(False)

    def jump(self,new,height=0):
        result = np.array([0,0])
        height = -height

        if new:
            self.current_jumps.append(np.array([0,height]))
        for i, _ in enumerate(self.current_jumps):
            result = np.add(result,self.current_jumps[i]/5)
            self.current_jumps[i][1] -= self.current_jumps[i][1]/5
        
        return result

    def handle_user_moves(self,game):
        result = np.array([0,0])
        if px.btn(px.KEY_RIGHT):
            result = np.add(result,np.array([2,0]))
        if px.btn(px.KEY_LEFT):
            result = np.add(result,np.array([-2,0]))
        return result
    
    def update(self,game):
        self.update_relatives()
        vector = np.array([0,0])
        for toadd in [self.handle_gravity(game),self.handle_user_jumps(),self.handle_user_moves(game)]: #
            vector = np.add(vector,toadd)

        #print(vector,self.x,self.y)
        self.x += vector[0]
        self.y += vector[1]

        print(self.x,self.y)

    def draw(self):
        px.rect(self.x,self.y,self.w,self.h,px.COLOR_CYAN)




class Game:
    def __init__(game):
        px.init(128,128,title="MyLab")

        game.GRAVITY = 0.25
        game.floor = Entity(0,128,128,128)
        game.walls = [Entity(30,120,8,8)]
        game.player = Player(64,64)

        px.run(game.update,game.draw)

    def update(game):
        game.frame_count = px.frame_count
        game.player.update(game)

    def draw(game):
        px.cls(px.COLOR_BLACK)
        game.player.draw()
        px.rect(30,120,8,8,px.COLOR_RED)

Game()