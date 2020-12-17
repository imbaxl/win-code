import pandas as pd 
class clean():
    def __init__(self, old_data):
        #导入csv变量
        self.old_data = old_data

    def clean(self):
        #csv文件是空DataFrame，全是columns，类型是Pandas.index，用tolist()方法转化为list
        data = self.old_data.columns.tolist()
        clean_df = pd.DataFrame(data,columns=['data'])

        #循环清除符号[]""
        for i in range(clean_df.shape[0]):
            if i != range(clean_df.shape[0]):
                clean_df.loc[i,'data'] = clean_df.loc[i,'data'].replace('[','')
                clean_df.loc[i,'data'] = clean_df.loc[i,'data'].replace(']','')
                clean_df.loc[i,'data'] = clean_df.loc[i,'data'].replace('"','')
            if clean_df.loc[i,'data'].count('.') == 2:
                clean_df.loc[i,'data'] = clean_df.loc[i,'data'].replace('.','$',1) #限制替换次数为1
                clean_df.loc[i,'data'] = clean_df.loc[i,'data'].replace('.','',1)
                clean_df.loc[i,'data'] = clean_df.loc[i,'data'].replace('$','.',1)
        #print('清洗方法完成：\n',clean_df.shape)
        return clean_df

        