l=6
m=7
n=8
o=9
for i in range(1,6):
	for k in range(5,0,-1):
		print(' '*k,f'{k}'f'{l}'f'{m}'f'{n}'f'{o}',end='\n')
		l=l-1
		m=m-1
		n=n-1
		o=o-1
		if l==6 or m==7 or n==8 or o==9:
			break
		