import numpy as np 
import fractions
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())}) #将浮点转化为分数显示

class matrix():
    def __init__(self):
        print('调用matrix类...')
        
        pass

    #求逆矩阵
    def inv(self,a): 
        a = np.linalg.inv(a)
        print('a的逆矩阵是：\n',a)
        return a

    #求点乘
    def dot(self,a,b): 
        a = np.array(a) #[[1,2,3],[4,5,6],[7,8,8],[2,3,2]]
        b = np.array(b) #[[3,2,1,1],[3,1,2,3],[4,3,2,1]]
        c = np.dot(a,b)
        print('a和b的点乘积是:\n',c)
        return c

    #求转置
    def t(self,a): 
        c = np.array(a) #[[1,2,3],[4,5,6]]
        print('a的转置为:\n',c.T)
        return c

    #求行列式，手动输入
    def det_m(self,a):
        a = np.mat(a) #'1,2,3;3,2,1;1,2,3'
        a = np.linalg.det(a) 
        print('行列式a的值为：\n',a)
        return a

    #求行列式，调用
    def det_a(self,a):
        a = np.array(a)
        a = np.linalg.det(a) 
        return a