import pandas as pd
import numpy as np 

class transfer():

    def __init__(self, data):
        self.data = data
    

    def trans(self):
        df0 = self.data
        df1 = pd.DataFrame(data=np.zeros((int(df0.shape[0]/6),6)),columns=['日期','开盘价','最高价','最低价','收盘价','成交量'])

        #求出日期数，每日期单位6，外加0，即shape(0)/6+1
        i = j = k = 0 #k是列序号，j是行序号，i是原行序号
        count = int(df0.shape[0]/6)

        for j in range(count):
            for k in range(6):
                df1.iloc[j,k] = df0.iloc[i,0]
                i += 1
        
        print(df1.shape)
        df1.to_csv('future/data.csv')
        return df1

    #PTA，2015年7月2日数据出错    4862	 5080	4852	5068.0004
