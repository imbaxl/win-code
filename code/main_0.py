from cat import cat    
from smallcat import smallcat

#实例化类，不用传self
my_cat = cat('柠檬','2岁')
her_cat = cat('酸菜','5岁')
his_cat = cat('冬瓜','3岁')

#访问属性

print('我的猫名字叫',my_cat.name.title())
print('我的猫今年',str(my_cat.age))

#调用方法
my_cat.sit()
my_cat.eat()
my_cat.play()

print('我们总共有',my_cat.name.title(),her_cat.name.title(),his_cat.name.title(),'的猫')
her_cat.play()
my_cat.eat()
his_cat.sit()

#调用父类
small_cat = smallcat('南瓜','0.3岁')
small_cat.eat()
print(small_cat.name.title(),'现在已经',small_cat.age.title())
small_cat.milk()