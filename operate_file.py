'''
	读写文件操作
'''
with open('./file/file_text.txt', 'r') as fRead: 
	print(fRead.read())				# 一次性读取文件

with open('file/file_text.txt', 'r') as fRead: 
	for line in fRead.readlines(): 				# readline依次读取文件中的每一行，readlines返回文件内容每一行组成的list
		print(line, '\n', '------------------------------')	

with open('file/python.jpg', 'rw') as byteContent: 				# 'rw'表示读取文件中的二进制
	print(byteContent.read())

with open('file/file_text.txt', 'r', encoding = 'gbk', errors = 'ignore')				# encoding表示读取文件的编码为gbk，errors表示如果遇到编码错误则忽略错误	

with open('file/file_write.txt', 'w') as fileWrite: 				# w模式下写的文件是直接覆盖该文件原有的内容，若想追加则改为'a'模式，写入指定的字符编码则添加可选的第三个参数：encoding = 'xxx'
	fileWrite.write('This module is write!')

with open('file/file_write.txt', 'r') as fileRead: 				# 读取写入后的文件内容
	print(fileRead.read())