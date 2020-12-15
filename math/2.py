import pandas as pd 
import numpy as np

#np.T属性求转置
np1 = np.array([[1,2,3],[4,5,6]])
print('np1:\n',np1.T)

#np.eye属性求对角线为1，其他位置为0的矩阵
np2 = np.eye(N=3,M=4,k=1,dtype=float) #k是从第一行第k个开始索引对角线
print('np2:\n',np2)

#np.identity属性求单位矩阵
np3 = np.identity(4,dtype=float)#参数是阶数
print('np3:\n',np3)

#np.rand创建随机矩阵
np4 = np.random.rand(5,4)
print('np4:\n',np4)

#np.matrix类型和np.ndarray类型互换（矩阵和N=2维数组互换）
np5 = np.matrix('1,2,3;4,5,6;7,8,9')
np5 = np.asarray(np5)

#np.dot矩阵乘积
np6_1 = np.array([[1,2,3],[4,5,6],[7,8,8],[2,3,2]])
np6_2 = np.array([[3,2,1,1],[3,1,2,3],[4,3,2,1]])
np6_3 = np.dot(np6_1,np6_2)
print('np6_1和np6_2的点乘积是:\n',np6_3)

#np.linalg.inv()计算逆矩阵
np7_1 = np.mat('4,9;3,7')
np7_2 = np.linalg.inv(np7_1)
print('np7_1的逆矩阵是：\n',np7_2)

