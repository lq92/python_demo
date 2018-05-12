'''
	多重继承——一个子类可以同时获得多个父类的所有功能
		注意：多重继承时，如果后一个父类中有和前一个父类中同名的属性/方法，最终继承的是前一个父类的属性/方法
'''

class Animal(object): 
	def __init__(self, name): 
		self.name = name

class Bird(Animal): 
	def __init__(self, name): 
		Animal.__init__(self, name)
	def catchWorm(self): 
		print('I\'m catching worms!')	

class Mammal(Animal): 
	def __init__(self, name): 
		Animal.__init__(self, name)
	def drinkingMilk(self): 
		print('I\'m drinking milk!')	

class FlyingMixin(object): 
	def flying(self): 
		print('I\'m flying!')

class RunningMixin(object): 
	def running(self): 
		print('I\'m running!')	

class Dog(Mammal, RunningMixin):				# 继承Mammal类和RunningMixin类 
	def __init__(self, name): 
		Mammal.__init__(self, name)

class Magpie(Bird, FlyingMixin):				# 继承Bird类和FlyingMixin类 
	def __init__(self, name): 
		Bird.__init__(self, name)

d = Dog('Eddi')
d.drinkingMilk()				# 调用Mammal类中的方法  
d.running()				# 调用RunningMixin类中的方法

m = Magpie('Sandi')
m.catchWorm()				# 调用Bird类中的方法				
m.flying()				# 调用FlyingMixin类中的方法														