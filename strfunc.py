a=input('please enter the string \t \n')
b=input('please enter the letter to be checked in string \t')
def stringchck(a,b):
	count=0
	for i in (a):
		if i==b:
			count=count+1
	print(f'\n {count}')
stringchck(a,b)