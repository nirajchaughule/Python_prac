for i in range(5,1,-1):
	k=5
	for j in range (1,6):
			print(' ',end=f'{k}')
			k=k-1
			if k==1:
				for l in range(2,6):
					print(' ',end=f'{l}')
					l=l+1
	print(end=' \n')
print(' 5')

for i in range(1,5,):
	k=5
	for j in range (1,i+1):
			print(' ',end=f'{k}')
			k=k-1
	print(end=' \n')
print(' 5 4 3 2 1')
