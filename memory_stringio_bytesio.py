'''
	对内存操作——有操作字符串和二进制两种
		字符串——StringIO
		二进制——BytesIO
		stream position——流位置的概念，当初始化传入字符串的时候stream position的位置是0，当写入字符串的时候stream position的位置是写入字符串的长度
			1. 可以通过tell()方法查看stream position的值
			2. 可以通过seek(position)方法设置值，当设置position后，则read()方法从该position位置往后读取
			3. 当调用write方法写入数据后stream position的值是根据写入的字符串长度变化的
			4. 调用read()后stream position的值指向最后
			5. 调用getvalue()后stream position的值与调用getvalue()之前相同
'''

from io import StringIO, BytesIO

# 未初始化数据
s1 = StringIO()
print('Before s1 write, s1\'s stream position is: ', s1.tell())
s1.write('Hello, Python!')
print('After s1 write, s1\'s stream position is: ', s1.tell())				# read读取的是stream position之后的内容，写入是position为字符串的长度
if s1.read() == '': 
	print('s1\'s read content is: empty!')
else: 	
	print('s1\'s read content is: ', s1.read())
if s1.getvalue() == '': 
	print('s1\'s getvalue content is: none')
else: 
	print('s1\'s getvalue content is: ', s1.getvalue())	

print('+++++++++++++++++++++++++++++++++')	

b1 = BytesIO()
b1.write('Python编程'.encode())
print('b1 getvalue: ', b1.getvalue())
print('Before seek: ')
print('b1 read: ', b1.read())
b1.seek(0)
print('After seek: ')
print('b1 read: ', b1.read())


print('---------------------------------')
# 初始化数据
s2 = StringIO('This is first string')
print('Before s2 write, but set initial content, s2\'s stream position is: ', s2.tell())
print('I\'m reading the content: ', s2.read())				# read()方法读取完数据后stream position会移到最后	
print('After reading, the stream position is: ', s2.tell())				# 固这里的stream position等于初始化字符串的长度			
s2.write('This is second string')
print('After s2 write, but set initial content, s2\'s stream position is: ',s2.tell())
#s2.seek(0)
print('I\'m calling the getvalue function: ', s2.getvalue())
print('After getvalue, the stream position is: ', s2.tell())
s2.write('Test')
print('s2 read: ', s2.read())
print('s2 getvalue: ', s2.getvalue())
print('s2 read: ', s2.read())

print('+++++++++++++++++++++++++++++++++')	

b2 = BytesIO(b1.getvalue())
print(b2.getvalue().decode('utf-8'))
