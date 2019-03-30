print("Hello please enter three numbers:")
a=input()
b=input()
c=input()


if a>b:
	if a>c:
		print(f"{a} is greatest")
elif b>c:
	if b>a:
		print(f"{b} is greatest")
else:
	print(f"{c} is greatest")
        