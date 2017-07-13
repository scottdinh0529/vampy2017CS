f = open("menu.txt", "w")

friedrice = 10
eggdropsoup = 7

def printtotal():
	print (noodlestotal)

def howmanynoodles():
	noodles = 8
	x = input("""How many do you want?
	""")
	noodlestotal = int(noodles) * int(x)
	f.write (str(x)+" Noodles "+".......... "+ str(noodlestotal))
	printtotal()


	

choice = input("""Ling Ling's China Buffet
Do you want noodles, fried rice, or egg drop soup?
""")
if choice == "noodles":
	 howmanynoodles()








