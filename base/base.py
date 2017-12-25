"""
age = 20
if age >= 18:
	print('adult')
else:
	print('teen')
age = age - 3
if age >= 18:
	print('adult')
else:
	print('teen')

while age > 0:
	age = int(input('请输入你的年龄:'))
	if age >= 18:
		print('adult')
	else:
		print('teen')

height = 1.75
weight = 80.5
BMI = 80.5/(1.75*1.75)
if BMI > 32:
	print('严重肥胖')
elif BMI > 28:
	print('肥胖')
elif BMI > 25:
	print('过重')
elif BMI > 18.5:
	print('正常')
else:
	print('过轻')
	
confim = input('是否继续计算BMI？继续请输入Y，退出请按任意键！')	
	
while confim == 'y':
	height = float(input('请输入你的身高:'))
	weight = float(input('请输入你的体重:'))
	BMI = weight/(height*height)
	if BMI > 32:
		print('严重肥胖')
	elif BMI > 28:
		print('肥胖')
	elif BMI > 25:
		print('过重')
	elif BMI > 18.5:
		print('正常')
	else:
		print('过轻')
	confim = input('是否继续计算BMI？继续请输入Y，退出请按任意键！')	
"""
L = ['A','B','C']
for x in L:
	print(x)

X = 0
while X < int(len(L)):
	print(L[X])
	X = X+1
	if X > 1:
		break

print('\n');		
		
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
print(d["Michael"])
d['Michael'] = 0
print(d["Michael"])
if 'Bob' in d:
	print('Bob在此')
	x = d.get('Tracy', -1)
	if x == -1:
		print('Trac不在此')
	else:
		print('Tracy在此')
d1 = {'Michael': 95, 'Bob': 75, 'Tracy': 85,'Tracy': 84}
print(d1['Tracy'])

print('\n');

s = set(['A','B','C'])
print(s)

print('\n');

n1 = 255
n2 = 1000

x1 = hex(n1)
print(x1)
print("zheshi",x1)

def my_plus(x,y):
	a = x + y
	
	if a > 10:
		pass
	else:
		print("hello")
	return a

a = my_plus(1,2)
print(a)


print('\n');	
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

print('\n');

def qua(a,b,c):
	delta = b*b-4*a*c
	if delta < 0:
		print("此方程无解")
	if delta > 0:
		x1 = (-b+math.sqrt(delta))/(2*a)
		x2 = (-b-math.sqrt(delta))/(2*a)
		print("该方程的解为",x1,x2)
	if delta == 0:
		x1 = (-b-math.sqrt(delta))/(2*a)
		print("该方程的解为",x1)
'''		
a = int(input("输入a的值"))
b = int(input("输入b的值"))
c = int(input("输入c的值"))

r = qua(a,b,c)
'''

def power(x):
    return x * x
