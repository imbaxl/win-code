from pandas.core.frame import DataFrame
from book import book
import pandas as pd

#df = pd.DataFrame(columns=['name','type','difficult','language','status'])
#df.to_excel('0.xlsx')

#实例化book

"""
newbook = book('人格心理学','心理学','中等难度','中文','未购买')
print(newbook.name.title(),newbook.type.title(),newbook.difficult.title(),newbook.language.title(),newbook.status.title())

newbook.bought()

newbook.save()
"""
#通过在循环下，获得用户输入的变量转为实例化的形参
def book_input():
    name = input('请输入书籍名称')
    type = input('请输入书籍类型')
    difficult = input('请输入书籍难度')
    language = input('请输入书籍语言')
    status = input('请输入购买状态')
    newbook = book(name,type,difficult,language,status)
    return newbook

def book_choice(func):
    var = 1
    while var == 0:
        var = input('当前选择的书籍是：',newbook.name.title(),'请输入要选择的操作，【0】退出，【2】改为')


if __name__ == "__main__":
    book_input_new = book_input()
    book_input_new.save()
    book_input_new.show()
    #book_choice_new = book_choice(newbook)