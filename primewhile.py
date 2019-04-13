a=int(input('Enter the number'))
if a==0 or a==1:
	print('not prime')
if a==2:
	print('number is prime')
i=2
while i!=a:
		if a%i==0:
			print(f'{a} is not prime')
			break;
		elif i==a:
			break;
		else:
			print(f'{a} is prime')
			break;
		i=i+1