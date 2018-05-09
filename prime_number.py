'''
	0- 100的质数：埃拉托色尼筛选法步骤：
		1. 把2的倍数删除(保留2本身)
		2. 把3的倍数删除(保留3本身)
		3. 把5的倍数删除(保留5本身)
		4. 把7的倍数删除(保留7本身)
		5. .....
		6. 把list中的数按照上述步骤删除
'''

'''
	函数prime接收一个要保留素数的list
	1. 找到list中最大值，用于限制循环条件
	2. 定义removeTwo函数，先去除2的倍数
	定义filterNumber函数，用于filter过滤，该函数依次接收list项数，并返回不能整除2/3/5/7或者是2/3/5/7本身
'''
def prime(arr): 
	max_number = max(arr)
	def removeTwo(x): 
		return x % 2 != 0 or x == 2
	arr = list(filter(removeTwo, arr))	
	i = 1
	while i < max_number: 
		i += 2
		def filterNumber(x): 
			return x % i != 0 or x == i 
		arr = list(filter(filterNumber, arr))
	return arr		
print(prime([x for x in range(2, 100)]))
# return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]