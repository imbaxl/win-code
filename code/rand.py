import numpy as np 
import random as rn

class money():
    def __init__(self,basic,max):
        self.basic = basic
        self.max = max

    def begin(self):
        print('现在有的钱是：',self.basic,'元,直到',self.max,'元后就会停止加钱')

    def increase(self):
        current = 0
        count = 0
        while current < self.max:
            random = rn.random()
            current += random
            count += 1
            print('现在有',current,'元,经过第',count,'次增加')
        print('当前的钱有',current,'元,满足吗？')
