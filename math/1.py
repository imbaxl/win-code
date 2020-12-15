import numpy as np

#用mat方法创建行列式
a = np.mat('1,2,3;3,2,1;1,2,3') 

#用linalg.det计算行列式的值
a_result = np.linalg.det(a)
print(a_result)