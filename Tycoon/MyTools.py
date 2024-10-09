import os,json

class DATA:
    def __init__(self,name,*,default:dict={}):
        """
        name: the name of the file (will be stored under DATA folder) (without any extension)
        default: will be used only if no file exists. use overwrite to modify the stored value
        """
        self.path = "DATA/"+name+".json"
        if not os.path.exists(self.path):
            if not os.path.exists("DATA"):
                os.makedirs("DATA")
            self.overwrite(default)
        self.update()

    def update(self):
        self.value = json.load(open(self.path , "r"))
    
    def overwrite(self,value:dict):
        json.dump(value, open(self.path , "w"), indent=4, sort_keys=True)
        self.update()

    def push(self):
        self.overwrite(self.value)

    def delete(self):
        os.remove(self.path)