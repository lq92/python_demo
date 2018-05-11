'''
	定义一个私有属性：在属性前加双下划线(__)，这样的属性外部无法读取

	在外部获取私有属性：定义新的方法来获取私有属性
	在外部修改私有属性：定义新的方法来修改私有属性
	约定：当属性以单下划线(_)开头的属性，视为私有属性，实际外部是可以访问和修改的

	当在类的外部设置过私有变量后(instance.__property = xxx)，可以通过instance._class__property获取到私有变量，否则报错
'''

class Student(object): 
	def __init__(self, name, age, score): 
		self.__name = name
		self.age = age
		self._score = score
	def print_name(self): 
		return self.__name
	def get_name(self): 
		return self.__name
	def set_name(self, newName): 
		self.__name = newName		

s1 = Student('Bill', 23, 98)
print(s1.age)
# print(s1.__name)  # Throw AttributeError		
s1.__name = 'Gate' # 此时只是在s1上添加了一个__name属性，而不是修改本身s1上的__name属性
print(s1.print_name(), s1.__name, s1._Student__name) # print 'Bill' 'Gate'

print(s1.get_name(), '\n')

s1.set_name('Jack')
print(s1.get_name(), '\n')

print(s1._score)
s1._score = 60
print(s1._score)