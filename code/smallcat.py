from cat import cat

class smallcat(cat):
    def __init__(self,name,age):
        super().__init__(name,age)


    def milk(self):
        print(self.name.title(),'现在还在喂奶阶段')
        