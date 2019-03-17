print("Enter user 1's choice")
a=input()
print("Enter user 2's choice")
b=input()
if a=="Rock" and b=="Rock":
	print("Same....Try again")
elif a=="Rock" and b=="Paper":
	print("B Wins")
elif a=="Rock" and b=="Scissor":
	print("A Wins")
elif a=="Paper" and b=="Rock":
	print("A Wins")
elif a=="Paper" and b=="Paper":
	print("Same....Try again")
elif a=="Paper" and b=="Scissor":
	print("B wins")
elif a=="Scissor" and b=="Paper":
	print("A Wins")
elif a=="Scissor" and b=="Rock":
	print("B wins")
elif a=="Scissor" and b=="Scissor":
	print("Same Try Again")
else:
	print("Invalid Input")