
from request import request
from clean import clean
from transfer import transfer
from settings import settings
from visual import visual

#获取期货数据，参考链接https://blog.csdn.net/dodo668/article/details/82382675?utm_medium=distribute.pc_relevant_download.none-task-blog-baidujs-1.nonecase&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-baidujs-1.nonecase


if __name__ == "__main__":
    #入口函数
    new_settings = settings()
    
    #请求数据
    
    #for key,value in new_settings.dict.items(): #字典迭代
    for key,value in new_settings.single.items(): #单个合约代码

        new_request = request(key)
        new_request_content = new_request.get()

        #清洗数据
        new_clean = clean(new_request_content)

        #数据重整
        new_transfer = transfer(new_clean.clean())
        new_transfer.trans()

    
    
    new_visual = visual()

        #可视化
        #数学分析

    
