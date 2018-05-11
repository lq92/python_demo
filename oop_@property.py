'''
	对于私有属性的获取和设置需通过setter和getter函数分别来获取和设置，略显麻烦，Python提供了@property来获取和设置私有属性，可以编写简洁的代码
'''

import time
class Student(object): 
	def __init__(self, name, birth):   # 创建Student实例需传入name和birth参数
		self.__name = name
		self.__birth = birth
	@property
	def getName(self):    # getName是属性而不是方法
		return self.__name
	@getName.setter
	def getName(self, newName): 
		if not isinstance(newName, str): 
			raise ValueError('New name must be a string')
		self.__name = newName
	@property
	def getBirth(self): 
		return self.__birth
	@getBirth.setter
	def getBirth(self, newBirth): 
		if not isinstance(newBirth, int): 
			raise ValueError('New birth must be a int')
		self.__birth = newBirth
	@property
	def age(self):   # 只获取age属性
		return time.gmtime().tm_year - self.__birth

s1 = Student('Bill', 1992)
print(s1.getName, '\n')			
s1.getName = 'Gate'
print(s1.getName, '\n')
print(s1.age)			



class Screen(object): 
	@property
	def width(self): 
		return self.__width
	@width.setter
	def width(self, newWidth): 
		if not isinstance(newWidth, (int, float)): 
			raise ValueError('New width must be a int or float!')
		self.__width = newWidth
	@property
	def height(self): 
		return self.__height
	@height.setter
	def height(self, newHeight): 
		if not isinstance(newHeight, (int, float)): 
			raise ValueError('New height must be a int or float!')
		self.__height = newHeight
	@property
	def resolution(self): 
		return self.__width * self.__height			

s = Screen()  # 创建Screen实例的时候无需传入参数
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')	