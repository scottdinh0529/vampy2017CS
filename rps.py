import random as r

cpu = r.randint(1, 3)

def game():	
	choice = input("""	1. rock
	2. paper
	3. scissors
	""")
	
	if cpu == 1 and choice == "1":
		print ("both chose rock. it is a tie.")
	
	elif cpu == 2 and choice == "2":
		print ("both chose paper. it is a tie.")

	elif cpu == 3 and choice == "3":
		print ("both chose scissors. it is a tie.")
	
	elif cpu == 1 and choice == "3":
		print ("CPU chose rock, you chose scissors. you lose.")
	
	elif cpu == 2 and choice == "1":
		print ("CPU chose paper, you chose rock. you lose.")
	
	elif cpu == 3 and choice == "2":
		print ("CPU chose scissors, you chose paper. you lose.")
	
	elif cpu == 1 and choice == "2":
		print ("you chose paper, cpu chose rock. you win.")

	elif cpu == 2 and choice == "3":
		print ("you chose scissors, CPU chose paper. you win.")

	elif cpu == 3 and choice == "1":
		print ("you chose rock, CPU chose scissors. you win.")

	game()

game()

