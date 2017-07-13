def bubble(items):
	for t in range(len(items)-1):
		for i in range(len(items)-1):
			if items[i] > items[i+1]:
				temp = items[i]
				items[i] = items[i + 1]
				items[i+1] = temp

def reversebubble(items):
	for t in range(len(items)-1):
		for i in range(len(items)-1):
			if items[i] < items[i+1]:
				temp = items[i]
				items[i] = items[i + 1]
				items[i+1] = temp

def merge(items):
	if len(items) < 2:
		return
	
	mid = int(len(items) / 2)
	left = []
	right = []
	for i in range(0, mid):
		left.append(items[i])
	for i in range(mid, len(items)):
		right.append(items[i])
	
	merge(left)
	merge(right)
	
	L = 0
	R = 0
	M = 0
	
	while L < len(left) and R < len(right):
		if left[L] < right[R]:
			items[M] = left[L]
			L += 1
			M += 1
		else:
			items[M] = right[R]
			R += 1
			M += 1
	
	while L < len(left):
		items[M] = left[L]
		L += 1
		M += 1

	while R < len(right):
		items[M] = right[R]
		R += 1
		M += 1

def shuffle(items):
	"""
	Shuffles the items in O(n) time
	"""
	for i in range(len(items)):
		index = random.randint(1, len(items)-1)
		temp = items [i]
		items[i] = items[index]
		items[index] = temp

		
		

