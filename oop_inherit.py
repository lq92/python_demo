'''
	定义一个父类，子类可以从父类中继承方法和属性

	初始化实例的时候接收三个参数: self/name/age

	定义一个类
		语法: class Name(inherit)，inherit表示要继承的父类

		初始化属性: 在父类中定义__init__方法，def __init__(self, property1, property2, ...)，__init__方法第一个参数是self，后续的参数表示要添加到实例的属性，self表示创建的实例，在子类中继承父类的属性直接调用inherit.__init__(self, property1, property2, ...)
		
		特性: 允许动态添加/修改数据
'''
class School(object): 
	def __init__(self, name, age): 
		self.name = name
		self.age = age
	def sayName(self): 
		print('I\'m %s'%self.name)

class Teacher(School): 
	def __init__(self, name, age, salary): 
		School.__init__(self, name, age)
		self.salary = salary
	def saySalary(self): 
		print('今天发了%s元工资'%self.salary)

class Student(School): 
	def __init__(self, name, age, score): 
		School.__init__(self, name, age)
		self.score = score
	def sayScore(self): 
		print('%s这次考试考了%d分'%(self.name, self.score))				

s1 = Student('Bill', 14, 92)
s1.sayName()
s1.sayScore()
s1.favio = 'Basketball'  # 添加实例属性，由该实例私有
print(s1.favio)
s2 = Student('Jack', 15, 78)
# print(s2.favio) # Throw AttributeError
s2.name = 'Smith' # 修改实例属性
print(s2.sayScore())

t1 = Teacher('Gate', 28, 3800)
t1.sayName()
t1.saySalary()
