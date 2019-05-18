a=input('Enter the string')
def countlet():
	b=[]
	c=[]
	for i in range(len(a)):
		b.extend(a[i])
	print(b)
	for i in range(len(a)):
		r=0
		for j in range (len(a)):
			if b[i]==b[j]:
				r+=1
			if r>1:
				c.extend(b[j])
		print(f'{c[i]}-{r}')
countlet()
