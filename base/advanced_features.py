	#	python advanced_features.py
print("\nList取值基本写法")
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(n):
	r.append(L[i])
	
print(r)

print("\nList取值Slice切片写法")
print(L[0:2])

L = list(range(100))
#print(L)
print(L[-10:])

print(L[10:20])
print(L[-50:-40])
print(L[10:20:2])
print(L[:])

print("\nTest")

'''
def trim(s):
	if s == "":
		return s
	elif s[1] == " ":
		return trim(s[1:])
	elif s[-1] == " ":
		return trim(s[:-1])
	return s
	
print(trim('ABC  '))
print(trim('      ABC  '))
print(trim('  A B  C  '))
'''

def trim(s):
	while s[0:1] == ' ':
		s = s[1:]
	while s[-1:] == ' ':
		s = s[:-1]
	return s

def trim1(s):
	while s[0:1] == ' ':
		s = s[1:]
	while s[-1:] == ' ':
		s = s[:-1]
	return s

print(trim('ABC  '))
print(trim('      ABC  '))
print(trim('  A B  C  '))

print(trim1('ABC  '))
print(trim1('      ABC  '))
print(trim1('  A B  C  '))