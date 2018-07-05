def compute():
	for a in range(1,333):
		for b in range(a,a+333):
			c = 1000 - a - b
			if a**2 + b**2 == c**2:
				print('a:' + str(a) + ' b:' + str(b) + ' c:' + str(c))

compute()