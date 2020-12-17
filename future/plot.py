import matplotlib.pyplot as plt 
import scipy.stats as st
import pandas as pd 

'''获取系统中的字体列表
import matplotlib
a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

for i in a:
    print(i)
    '''
#学习matplotlib可视化

#用pandas读取数据
df1 = pd.read_excel('future/data/甲醇data.xlsx', index_col=0,)

#修改字体以支持中文显示
plt.rcParams['font.family']=['Heiti TC']

#图示标题
plt.title('甲醇连续合约历史波动')

#plt.plot(df1['最高价']-df1['最低价'], color='green',linewidth='2.0',linestyle='-')

#定义随机变量
mu = 0 #平均值
sigma = 1 #标准差
x = df1['收盘价']

plt.plot(x,color='blue',linewidth='1.0',linestyle='-')

plt.grid()
plt.show()

#想了解概率密度分布，但是按上述方法不太管用