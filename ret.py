a=int(input('Enter your age'))
def ret(a):
	if a>65:
		print('Already retired')
	else:
		a=65-a
		print(f'Age left to retire is {a}')
ret(a)