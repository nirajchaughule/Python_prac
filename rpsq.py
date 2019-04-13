import random
a= input("User A:Enter input").lower()
print("NO CHEATING\n"*10)
b=random.randint(0,2)

while(1):

	if a=='quit':
		print ('closing')
		break


	#rock

	if b==0:
		print("User B chose rock")

	#paper

	if b==1:
		print("User B chose paper")

	#scissor

	if b==2:
		print("User B chose scissor")

	if a=='quit':
		print ('closing')
		break
		if a:
			if a!="rock" and a!="paper" and a!="scissor":
				print("NOT VALID INPUT")
			if b==0 and a=="rock":
				print("Tie")
				if b==1 and a=="paper":
					print("Tie")
					if b==2 and a=="scissor":
						print("Tie")
			if b==0:
				if a == "paper":
					print("A wins")
				if a == "scissor":
					print("B wins")
			if b==1:
				if a == "paper":
					print("A wins")
				if a == "scissor":
					print("B wins")
			if b==2:
				if a == "paper":
					print("A wins")
				if a == "scissor":
					print("B wins")
		else:
			print("Please enter input")