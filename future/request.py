import requests as re
import pandas as pd 
import io

class request():
    def __init__(self, contract):
        #初始化，传参是连续合约代码
        self.contract = contract
        self.url = 'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=' + str(contract)


    def get(self):
        #获取url内容，并转为csv格式
        r= re.get(self.url).content
        df = pd.read_csv(io.StringIO(r.decode('utf-8')))
        return df

