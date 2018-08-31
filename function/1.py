"""

函数的参数：
	- 默认参数：有赋值就算赋值的参数
	- 可变参数
	- 关键字参数
	- 命名关键字参数

"""

def f1(a, b = 5, c = 10):
	return a + b * 2 + c *  3
print("参数默认值：")	
print(f1(1,2,3))		#a=1,b=2,c=3
print(f1(100,200))		#a=100,b=200,c=10
print(f1(100))			#a=100,b=5,c=10

#-----------------------------------------------------------------------------

def f2(*args):
	sum = 0
	for num in args:
		sum += num
	return sum
print("可变参数：")
print(f2(1 , 2 , 3))	
print(f2())

#------------------------------------------------------------------------------

def f3(**kw):
	if 'name' in kw:
		print('欢迎你%s!' % kw['name'])
	elif 'tel' in kw:
		print('你的联系电话是：%s!' % kw['tel'])
	else:
		print('没找到你的个人信息！')
param = {'name': 'Ray' , 'age': 20}

print("关键字参数：")
f3(**param)
f3(name='Ray', age=20, tel='123')
f3(user='Ray', age=20, tel='123')
f3(user='Ray', age=20, mobile='123')
		
		
