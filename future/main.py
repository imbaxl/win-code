
from request import request
from clean import clean
from transfer import transfer

#获取期货数据，参考链接https://blog.csdn.net/dodo668/article/details/82382675?utm_medium=distribute.pc_relevant_download.none-task-blog-baidujs-1.nonecase&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-baidujs-1.nonecase

#r = re.get('http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=TA0').content
#df = pd.read_csv('future/data.csv',index_col=0)



#创建df1，将df数据清洗后转移到df1

#清洗格式


"""
clean_new = clean(df)

print(clean_new.shape)
print(df1.head())
clean_new.to_csv('future/data.csv')
"""
if __name__ == "__main__":
    #入口函数

    #请求数据
    new_request = request('TA0')
    new_request_content = new_request.get()

    #清洗数据
    new_clean = clean(new_request_content)
    #new_clean.clean().to_csv('future/data.csv')

    #切片转移数据
    new_transfer = transfer(new_clean.clean())
    new_transfer.trans()