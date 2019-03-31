a=int(input("Enter the number to be checked"))
if a==2:
	print("Prime number");
elif a==0 or a==1:
	print("not a prime")
for i in range (2,a):
	if a%i==0:
		print ("Num is not prime")
		break
	else:
		print("Num is prime")
	if a%(i+1)==0:
		print("Not prime")