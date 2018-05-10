#!/usr/bin/env python3   表示在mac/linux/unix上运行
# -*- ecoding: utf-8 -*-  表示Python2的字符集为utf-8

'This is a module' # 模块中的第一个字符串表示文档注释

__author__ = 'lq'  # 表明模块的作者

import sys  # 导入其他的模块

arg = sys.argv  # sys.argv表示Python命令行中接收到的参数，第一个参数总是为模块名，后续的参数根据用户输入，返回的是一个list

length = len(arg)

def test(): 
	if length == 1: 
		print('Hello, World!')
	elif length == 2: 
		print('Hello, %s'%arg[1])
	else: 
		print('You input too much arguments!')

# 当在命令行模式下运行该模块，Python会把一个特殊变量__name__设置为'__main__'，其他方式则否
if __name__ == '__main__': 
	test()				
