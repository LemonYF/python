'''
recfunction.py
'''

def fact(n):
	if n == 1:
		return 1
	else:
		return n*fact(n-1)
		
print(fact(5))

'''print(fact(1000))

'''
print("\n尾递归,尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式")
def fact1(n):
	return fact_iter(n, 1)

def fact_iter(n, product):
	if n == 1:
		return product
	else:
		return fact_iter(n - 1, product * n)

print(fact1(5))

print("\nTest")
def hanoi(n, a = "a", b = "b", c = "c"):
	if n == 1:
		print(a, "->", c)
	else:
		hanoi(n-1, a, c, b )	#	移动n-1到缓冲区
		hanoi(1, a, b, c)		#	move the biggest from A to C
		hanoi(n-1, b, a, c)		#	move n-1 to target
	return 2
	
hanoi(2)