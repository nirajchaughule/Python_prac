print("Hello please enter 4 numbers:")
a=input()
b=input()
c=input()
d=input()

if a>b and a>c and a>d:
	print(f"{a} greatest")
elif b>a and b>c and b>d:
	print(f"{b} greatest")
elif c>a and c>b and c>d:
	print(f"{c} greatest")
elif d>a and d>b and d>c:
	print(f"{d} greatest")