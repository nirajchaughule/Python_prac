a=int(input('Enter the number'))
if a==0 or a==1:
	print('not prime')
if a==2:
	print('number is prime')
for i in range(2,a):
	if a%i==0:
		print(f'{a} is not prime')
		break;
	elif i==a:
		break;
else:
	print(f'{a} is prime')