import turtle
import time
# 定义画出线条的函数
def drawLine(): 
	for i in range(2): 
		turtle.forward(300)
		turtle.right(90)
		turtle.forward(10)
		turtle.right(90)
# 定义画出星星的函数
def drawStar(): 
	for i in range(5): 
		turtle.forward(10)
		turtle.right(144)
# 定义画出星星背景的函数		
def drawStarBg(): 
	for i in range(2): 
		turtle.forward(130)
		turtle.right(90)
		turtle.forward(100)
		turtle.right(90)
# 画出线条
for i in range(1, 8): 
	turtle.fillcolor('red')
	turtle.pencolor('white')
	turtle.begin_fill()
	drawLine()
	turtle.end_fill()
	turtle.penup()
	turtle.goto(0, -30 * i)
# 画出星星背景
turtle.penup()
turtle.goto(0, 0)
turtle.fillcolor('blue')
turtle.begin_fill()
drawStarBg()
turtle.end_fill()		
# 画出星星
turtle.penup()
turtle.goto(0, 0)
def drawSix(j): 
	for i in range(6): 
		turtle.begin_fill()
		turtle.pencolor('white')
		turtle.fillcolor('white')
		turtle.penup()
		turtle.goto(i * 20 + 10, -10 * j -10)
		drawStar()
		turtle.end_fill()
def drawFive(j): 
	for i in range(5): 
		turtle.begin_fill()
		turtle.pencolor('white')
		turtle.fillcolor('white')
		turtle.penup()
		turtle.goto(i * 20 + 20, -10 * j -10)
		drawStar()
		turtle.end_fill()
for i in range(9): 
	if i % 2 == 0: 
		drawSix(i)
	else: 
		drawFive(i)		
time.sleep(10)	