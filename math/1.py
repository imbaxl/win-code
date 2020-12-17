import numpy as np



#np.matrix类型和np.ndarray类型互换（矩阵和N=2维数组互换）
np5 = np.matrix('1,2,3;4,5,6;7,8,9')
np5 = np.asarray(np5)

#np.eye属性求对角线为1，其他位置为0的矩阵
np2 = np.eye(N=3,M=4,k=1,dtype=float) #k是从第一行第k个开始索引对角线
print('np2:\n',np2)

#np.identity属性求单位矩阵
np3 = np.identity(4,dtype=float)#参数是阶数
print('np3:\n',np3)

#np.rand创建随机矩阵
np4 = np.random.rand(5,4)
print('np4:\n',np4)
