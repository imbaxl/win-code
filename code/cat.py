class cat():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title(),'在坐着.')

    def eat(self):
        print(self.name.title(),'在吃东西.')

    def play(self):
        print(self.name.title(),'在玩耍.')

