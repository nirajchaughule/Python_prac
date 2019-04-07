import random
a=int(input("Enter your guess"))
b=random.randint(0,3)
for i in range(0,3):
	if (a<b):
		print('number is less')
		break
	elif(a>b):
		print('number is high')
		break
	else:
		print('guess is correct')
		break