# 用闭包实现一个自增函数：用nonlocal实现内部函数获取外部函数
# def increament(): 
# 	count = 0
# 	def counter(): 
# 		nonlocal count
# 		count += 1
# 		return count
# 	return counter
# i1 = increament()
# print(i1())		

def increament(): 
	def counter(): 
		count = 0
		while True: 
			count = count + 1
			yield count
	c = counter()
	def fn(): 
		return next(c)
	return fn	
i1 = increament()
print(i1())
print(i1())
print(i1())
print(i1())
print(i1(), '\n')
i2 = increament()
print(i2())
print(i2())
print(i2())
print(i2())
print(i2())
