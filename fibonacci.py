# 函数生成斐波那契
# 接收参数n => 几个斐波那契数列
# 函数体定义的参数a, b, c; 分别表示数列的前一项(用于和b相加计算出后一项的值), b表示实际的数列值, c用于控制循环条件
def fibo(n): 
	a, b, c = 0, 1, 0
	while c < n: 
		print(b)
		a, b = b, a + b
		c += 1
	return 'Done'
fibo(8)		


# generator生成斐波那契
# 注意: 此时函数的返回值无法返回,是因为for in循环的generator是不会抛出StopIterator错误(即generator超出迭代的错误)
def fibo(n): 
	a, b, c = 0, 1, 0
	while c < n: 
		yield b
		a, b = b, a + b
		c += 1
	return 'Done'
g = fibo(8)
for i in g: 
	print(i)

# 此时函数的返回值可以返回,用except捕获错误
def fibo(n): 
	a, b, c = 0, 1, 0
	while c < n: 
		yield b
		a, b = b, a + b
		c += 1
	return 'Done'
g = fibo(8)
while True: 
	try: 
		print(next(g))
	except StopIteration as e: 
		print(e.value)
		break

