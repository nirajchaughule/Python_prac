a=int(input('Enter any number'))
if a>=22:
	print('please enter numbers between 0 and 21')
for i in range(a,22):

	if a==0:
		print('0 is even')
		break
	if a==1:
		print('1 is odd')
		break
	if a==4 or a==13:
		print(f'{a} is unlucky number')
		break
	if i%2==0:
		print(f'{i} is even')
		break
	else:
		print(f'{i} is odd')		
		break
	