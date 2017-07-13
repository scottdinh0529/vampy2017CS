import random as r

num = r.randint(1, 100)

guess = input("Guess a number... ")

while True:
	if guess == str(num):
		print ("You guessed it right")

	elif guess > str(num):
		print ("Too high")
	
	else:
		print ("Too low")

