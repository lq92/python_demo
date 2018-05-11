'''
	Python是一门动态语言，程序可以在运行时动态的添加属性和方法
	***在实例上动态添加的属性和方法，对于其他实例是不可见的，若要对所有的实例都可见的话，那在父类中动态添加属性和方法***
	
'''
class School(object): 
	def __init__(self, name): 
		self.name = name

def sayName(self): 
	return self.name

s1 = School('Bill')
# 在实例上添加属性
s1.age = 23
print(s1.age, '\n')
# 在实例上添加方法
from types import MethodType
s1.sayName = MethodType(sayName, s1)
print(s1.sayName(), '\n')

s2 = School('Gate')
print(dir(s1), '\n') # s1上有自定义的name/age属性和sayName方法
print(dir(s2), '\n') # s2上只有自定义的name属性

def dynamicMethod(self): 
	return 'I\'m a dynamic method!'
School.dynamicMethod = dynamicMethod

print(s1.dynamicMethod(), '\n')
print(s2.dynamicMethod(), '\n')


'''
	__slots__属性：限制实例添加的属性，对类的属性没有影响，对继承的子类也不影响，除非子类中也添加__slots__属性来限制子类实例添加的属性
'''

class Teacher(object): 
	__slots__ = ('name', 'age')
	def sayName(self): 
		return self.name


t1 = Teacher()
t1.name = 'Gate'
t1.age = 34
print(dir(t1), '\n')
print(t1.sayName())

t2 = Teacher()
t2.name = 'Jack'
t2.age = 40
#t2.salary = 5000 # Throw AttributeError
print(dir(t2), '\n')	