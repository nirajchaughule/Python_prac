print("Hello please enter 4 numbers:")
a=input()
b=input()
c=input()
d=input()


if a>b:
	if a>c:
		if a>d:
			print(f"{d} is greatest")
elif b>c:
	if b>a:
		if b>d:
elif c>a:
	if c>b:
		if c>d:
			print(f"{c} is greatest")
else:
	print(f"{d} is greatest")	