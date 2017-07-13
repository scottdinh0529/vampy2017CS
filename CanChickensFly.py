def q1():
	answer = input("Am I an object or a place? Y/N: ")
	if answer == "Y":
		q2()
	elif answer == "N":
		q4()
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q1()

def q2():
	answer = input("Am I bigger than a PC? Y/N: ")
	if answer == "Y":
		q3()
	elif answer == "N":
		q9()
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q2()

def q3():
	answer = input("Am I a building? Y/N: ")
	if answer == "Y":
		q7()
	elif answer == "N":
		q8()
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q3()

def q4():
	answer = input("Am I human? Y/N: ")
	if answer == "Y":
		q5()
	elif answer == "N":
		q6()
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q4()

def q5():
	answer = input("Am I fictional? Y/N: ")
	if answer == "Y":
		q12()
	elif answer == "N":
		q13()
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q5()

def q6():
	answer = input("Could you fit me in a coffee mug? Y/N: ")
	if answer == "Y":
		q14()
	elif answer == "N":
		q15()
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q6()

def q7():
	answer = input("Am I a salon? Y/N: ")
	if answer == "Y":
		print ("I am a salon")
	elif answer == "N":
		print("I am a bowling alley")
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q7()

def q8():
	answer = input("Am I New York? Y/N: ")
	if answer == "Y":
		print("I am NY")
	elif answer == "N":
		print("I am an umbrella")
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q8()

def q9():
	answer = input("Do you consume me? Y/N: ")
	if answer == "Y":
		q10()
	elif answer == "N":
		q11()
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q9()

def q10():
	answer = input("Am I a pizza? Y/N: ")
	if answer == "Y":
		print("I am a pizza")
	elif answer == "N":
		print("I am a bar of soap")
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q10()

def q11():
	answer = input("Am I a hat? Y/N: ")
	if answer == "Y":
		print("I am a hat")
	elif answer == "N":
		print("I am a computer")
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q11()

def q12():
	answer = input("Am I Santa? Y/N: ")
	if answer == "Y":
		print("I am Santa")
	elif answer == "N":
		print("I am James Bond")
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q12()

def q13():
	answer = input("Am I Michael Jackson? Y/N:")
	if answer == "Y":
		print("I am Michael Jackson")
	elif answer == "N":
		print ("I am Brittany Spears")
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q13()

def q14():
	answer = input("Am I a rat? Y/N: ")
	if answer == "Y":
		print("I am a rat")
	elif answer == "N":
		print("I am a frog")
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q14()

def q15():
	answer = input("Am I a chicken? Y/N: ")
	if answer == "Y":
		print("I am a chicken")
	elif answer == "N":
		print("I am a dracula")
	else:
		print("YOU'RE AN IDIOT. READ THE QUESTION")
		q4()

q1()
