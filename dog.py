import os
import turtle as t

def fwd(s):
	t.forward(s)

def left(s):
	t.left(s)

def right(s):
	t.right(s)

def up():
	t.pu()

def dwn():
	t.pd()

def sq(s):
	t.forward(s)
	t.left(90)
	t.forward(s)
	t.left(90)
	t.forward(s)
	t.left(90)
	t.forward(s)

def tri(s):
	t.forward(s)
	t.left(120)
	t.forward(s)
	t.left(120)
	t.forward(s)

def dog():
	#head
	fwd(50)
	left(90)
	fwd(50)
	left(90)
	fwd(35)
	#ear
	right(90)
	fwd(15)
	left(90)
	fwd(15)
	left(90)
	fwd(65)
	#body, legs, and tail
	right(90)
	fwd(100)
	left(90)
	fwd(15)
	right(90)
	fwd(50)
	left(90)
	fwd(5)
	left(90)
	fwd(50)
	right(90)
	fwd(30)
	left(90)
	fwd(20)
	right(90)
	fwd(50)
	left(90)
	fwd(20)
	left(90)
	fwd(50)
	right(90)
	fwd(40)
	right(90)
	fwd(50)
	left(90)
	fwd(20)
	left(90)
	fwd(100)
	#eyes
	up()
	right(90)
	fwd(35)
	left(90)
	fwd(35)
	dwn()
	sq(4)
	up()
	fwd(50)

dog()

t.exitonclick()
