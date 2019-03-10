a=int(input("Enter your marks"))
if a>35:
	if a<=50 and a>=35:
		print("C")
	elif a>=51 and a<=60:
		print("B")
	elif a>=61 and a<=74:
		print("A")
	elif a>=75 and a<=100:
		print("Distinction")
	elif a>101:
		print("Out of limit")
else:
	print("bye")
