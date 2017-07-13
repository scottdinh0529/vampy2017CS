global a = 0
global b = 0
global c = 0
global d = 0
global e = 0
def q1():
	q1 = input("""What is your type of gameplay?
	a. make lots of dudes and go wide
	b. counter everything and not let your opponent play magic
	c. kill everything
	d. burn things like hitler
	e. big dudes
	""")
	
	if q1 == "a":
		a += 1
		q2()
	if q1 == "b":
		b += 1
		q2()
	if q1 == "c":
		c += 1
		q2()
	if q1 == "d":
		d += 1
		q2()
	if q1 == "e":
		e += 1
		q2()
	else:
		print ("try again")
	
def q2():
	q2 = input("""What is important to you?
	a. order and peace
	b. knowledge
	c. power
	d. passion
	e. big and natural things
	""")
	
	if q2 == "a":
		a += 1
		q3()
	if q2 == "b":
		b += 1
		q3()
	if q2 == "c":
		c += 1
		q3()
	if q2 == "d":
		d += 1
		q3()
	if q2 == "e":
		e += 1
		q3()

def q3():
	q3 = input("""Which of these is your favorite creature?
	a. Archangel Avacyn
	b. Consecrated Sphinx
	c. Griselbrand
	d. Young Pyromancer
	e. Primeval Titan
	""")

	if q2 == "a":
		a += 1
		q4()
	if q2 == "b":
		b += 1
		q4()
	if q2 == "c":
		c += 1
		q4()
	if q2 == "d":
		d += 1
		q4()
	if q2 == "e":
		e += 1
		q4()

def q4()
	q4 = input("""Which of the following is the best mechanic?
	a. Populate
	b. Buyback
	c. Morbid
	d. 
	e. 
q1()

print (a)
print (b)
print (c)
print (d)
print (e)


