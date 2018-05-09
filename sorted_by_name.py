'''
	利用sorted可以对list进行排序，该函数接收默认的list参数和可选的key = sort_fn(排序函数)，以及可选的reverse = True开启反向排序三个参数
'''
l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def sortedByName(tuple): 
	return str.lower(tuple[0])
print(sorted(l, key = sortedByName)) # reverse = True可以反向排序	

def sortedByScore(tuple): 
	return tuple[1]
print(sorted(l, key = sortedByScore))	