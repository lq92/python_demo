# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
name = ['adam', 'LISA', 'barT']
def strToLower(string): 
	return str.upper(string[:1]) + str.lower(string[1:])
print(list(map(strToLower, name)))	

# 编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce
l = [3, 5, 7, 9]
def multi(x, y): 
	return x * y
def prod(list): 
	return reduce(multi, list)
print(prod(l))	