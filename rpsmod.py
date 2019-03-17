a=input("Enter user 1's choice").lower()
print("*********CHEATING NOT ALLOWED*******\n\n\n"*100)
b=input("Enter user 2's choice").lower()
if a:
	if b:
		if(a==b):
  		   print("TIE")
#ROCK
		elif a=="rock":
			if b=="paper":
				print("B Wins")
			elif b=="scissor":
				print("A WINS")
			else:
				print("Invalid input")
#PAPER
		elif a=="paper":
			if b=="rock":
				print("A Wins")
			elif b=="scissor":
				print("B WINS")
			else:
				print("Invalid input")
#SCISSOR
		elif a=="scissor":
			if b=="rock":
				print("B WINS")
			elif b=="paper":
				print("A WINS")
			else:
				print("Invalid input")
		else:
			print("Invalid Input.Please try again")
	else:
		print("player 2 Enter something")
else:
 print("Players enter something")
