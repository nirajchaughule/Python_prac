import random
a=input("User A:Enter input")
b=random.randint(0,3)
if b==0:#rock
	print("User B chose rock")
if b==1:#paper
	print("User B chose paper")
if b==2:#scissor
	print("User B chose scissor")
if a:
	if b==0:
		if a==rock:
			print("Tie")
		if a==paper:
			print("A wins")
		if a==scissor:
			print("")
		else:
			print("Invalid input")
	if b==1:
		if a==rock:
			print("Tie")
		if a==paper:
			print("A wins")
		if a==scissor:
			print("")
		else:
			print("Invalid input")
	if b==2:
		if a==rock:
			print("Tie")
		if a==paper:
			print("A wins")
		if a==scissor:
			print("")
		else:
			print("Invalid input")
else:
	print("Please enter input")