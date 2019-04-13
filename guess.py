import random;
a=input('please enter ur guess between 0 and 2 \n')
f=2
b=random.randint(0,2)
for i in range (0,2):
	if a==b:
		print('\nguess is correct')
		f=f-1
		break;
	else:
		print(f'\nplease try again.{f} chances left')
		f=f-1
		a=input('\nplease enter your guess again')
	if f==0:
		print('\nSorry guess times exceeded. Bye')
		break;