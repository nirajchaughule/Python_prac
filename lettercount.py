# a=input('Enter string')
# b=input('Enter letter')
# c=[]
# for i in range(len(c)):
# 	c.extend(a[i])
# print(c)
# e=c.count(b)
# print(e)
c=input('Enter the string:')
b=input('letter:')

def split(c):
	a=[]
	for i in range(len(c)):
		a.extend(c[i])
	print(a)

def string_count(c,b):
	split(c)
	e=c.count(b)
	print(e)
string_count(c,b)