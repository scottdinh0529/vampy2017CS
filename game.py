import random

class Player():
	self.hp = 100
	self.weapon = Nothing
	self.potions = 0

playerIG = Player()

def start():
	print ("You wake up in a dungeon.")
	print ("There is one room to your right and to your left")
	print ("1. Go left")
	print ("2. Go right")
	lr = input ("->")
	if lr == "1":
		startleft()
	elif lr == "2":
		startright()
	else:
		start()

def startleft():
	print ("You find a chest in the room.")
	print ("Will you open the chest?")
	print ("1. Open")
	print ("2. Leave the room")
	choice = input("->")
	if choice == "1":
		chestopen1()
	elif choice == "2":
		startroom()
	else:
		startleft()

def chestopen1():
	print ("You opened the chest.")
	print ("You found a rusty broadsword.")
	print ("Will you equip it?")
	print ("1. Yes")
	print ("2. No")
	choice = input("->")
	if choice == "1":
		self.weapon = rustybroadsword
	elif choice  == "2":
		print ("You have left the room.")
		startroom()
	else:
		chestopen1()


	

#missing startright(), startrooom()
		
	
	
