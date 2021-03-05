import pandas as pd
from pandas.core.frame import DataFrame

df = pd.read_excel('work/1.xlsx')
print(df.shape[0])

content1 = '厂家：',df.iloc[0,3],'\n','强度等级：',df.iloc[0,8],'\n','代表批量：',df.iloc[0,5],'\n','取样过程：','在施工现场进行取样并制成3块15cm×15cm×15cm标准养护混凝土抗压试块，现场检测位置的抽取和检测过程符合规范要求，一切情况正常。'


df1 = DataFrame(content1)

df2 = pd.read_excel('work/2.xls',index_col=0)

for i in range(df.shape[0]):
    df2.iloc[i,0] = df.iloc[i,4]
    data = '厂家：'+str(df.iloc[i,3])+'\n'+'强度等级：'+str(df.iloc[i,8])+'\n'+'代表批量：'+str(df.iloc[i,5])+'\n'+'取样过程：'+'在施工现场进行取样并制成3块15cm×15cm×15cm标准养护混凝土抗压试块，现场检测位置的抽取和检测过程符合规范要求，一切情况正常。'
    #data = '厂家：'+df.iloc[0,3]+'强度等级：'+df.iloc[0,8]+'代表批量：'+df.iloc[0,5]+'取样过程：'+'在施工现场进行取样并制成3块15cm×15cm×15cm标准养护混凝土抗压试块，现场检测位置的抽取和检测过程符合规范要求，一切情况正常。'
    print(data)
    df2.iloc[i,1] = data




df2.to_excel('work/3.xls')