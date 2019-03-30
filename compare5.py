print ("Enter the five numbers to be compared")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

if a>b:
	if a>c:
		if a>d:
			if a>e:
				print(f"{a} greatest")
if b>a:
	if b>c:
		if b>d:
			if b>e:
				print(f"{b} greatest")
if c>a:
	if c>b:
		if c>d:
			if c>d:
				print(f"{c} greatest")
if d>a:
	if d>b:
		if d>c:
			if d>e:
				print(f"{d} greatest")
if e>a:
	if e>b:
		if e>c:
			if e>d:
				print(f"{e} greatest")