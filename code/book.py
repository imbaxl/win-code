import pandas as pd


class book():
    def __init__(self,name,type,difficult,language,status):
        #将实参的变量传递到类中，供方法使用
        self.name = name
        self.type = type
        self.difficult = difficult
        self.language = language
        self.status = status
        print('读取数据表...')
        self.df = pd.read_excel('0.xlsx',index_col=0)

    
    def bought(self):
        print('当前的书名为',self.name.title())
        self.status = '已购买'
        print(self.name.title(),'的当前状态修改为：',self.status.title())



    def save(self):
        print('储存到数据表中...')
        df1 = pd.DataFrame(
            {'name':self.name.title(),
            'type':self.type.title(),
            'difficult':self.difficult.title(),
            'language':self.language.title(),
            'status':self.status.title()},index=[0]
            )
        self.df = self.df.append(df1,ignore_index=True)
        dataframe = self.df.to_excel('0.xlsx')
        print('储存完成')
        return dataframe

    def show(self):
        print('当前的数据表有以下书籍:\n',self.df)
        