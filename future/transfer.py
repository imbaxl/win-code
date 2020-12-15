import pandas as pd
import numpy as np 

class transfer():

    def __init__(self, data):
        self.data = data
    

    def trans(self, value):
        df0 = self.data
        df1 = pd.DataFrame(data=np.zeros((int(df0.shape[0]/6),6)),columns=['日期','开盘价','最高价','最低价','收盘价','成交量'])

        #求出日期数，每日期单位6，外加0，即shape(0)/6+1
        i = j = k = 0 #k是列序号，j是行序号，i是原行序号
        count = int(df0.shape[0]/6)

        for j in range(count):
            for k in range(6):
                df1.iloc[j,k] = df0.iloc[i,0]
                i += 1
        
        df1.to_excel('future/data/%sdata.xlsx' % (value))


        #数据强制转换为浮点型
        for i in range(len(df1.columns.tolist())):
            if i == 0:
                pass
            else : 
                df1.iloc[:,i] = df1.iloc[:,i].astype('float')


        print('合约%s的数据导出完毕...' %(value))
        