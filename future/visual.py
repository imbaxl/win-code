import matplotlib.pyplot as plt
import pandas as pd 

class visual():
    def __init__(self, data):
        #data是导入整个dataframe的变量
        self.data = data
        self.data = pd.read_excel(self.data,index_col=0)
        #需要简单的可视化

    def 





    
#contract manual filepath:
filepath = 'future/data/PTAdata.xlsx'
new_visual = visual(filepath)