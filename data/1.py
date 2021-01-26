import pandas as pd
 

df1 = pd.read_excel('data/1.xlsx',index_col=0) #商品数据10 商品编号3 条形码4
print(df1.head)

df2 = pd.read_excel('data/2.xlsx',index_col=0) #销售数据10 商品编号3 条形码4


#第一步：逐行匹配
j=0
for i in range(df2.shape[0]): #1-9000
    try:
        while df2.iloc[i,3] != df1.iloc[j,3]:
            j += 1
            if j == 29113 : pass
        df1.iloc[j,15] = df2.iloc[i,10]
        print(df1.iloc[j,15])
        #df1[j,10] = df2.iloc[i,10]
        
        j = 0
        if i >= 5000 : df1.to_excel('data/result.xlsx')
    except :
        pass
    

df1.to_excel('data/result.xlsx')