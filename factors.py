a=int(input("Enter the number"))
n=a
if n==1:
	print('1 is factor')
for i in range(2,a):
	if n%2==0:
		print('2 is factor')
		n=n/2
	elif n%3==0:
		print('3 is factor')
		n=n/3
	elif n%5==0:
		print('5 is factor')
		n=n/5
	elif n%7==0:
		print('7 is factor')
		n=n/7
	elif n==1:
		break
	else:
		print(f'1 and {n} is a factor')
		break