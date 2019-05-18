print('Enter ur list')
d=[]
c=' '
while c!="q":
	c=input()
	d.append(c)
c.pop()
for j in range(0,len(d)):
	print(f'{j+1}.{d[j]}')