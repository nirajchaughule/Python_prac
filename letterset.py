a=input('Enter the string')
def countlet():
	b=[]
	
	for i in range(len(a)):
		b.extend(a[i])
	print(b)
	for i in range(len(a)):
		r=0
		for j in range (len(a)):
			if b[i]==b[j]:
				r+=1
		print(f'{b[i]}-{r}')
countlet()
