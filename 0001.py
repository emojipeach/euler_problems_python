print("""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
""")

def sum_of_mults(a,b,z):
	multiple_as = list(range(a,z,a))
	multiple_bs = list(range(b,z,b))
	for multiple_b in multiple_bs:
		if multiple_b not in multiple_as:
			multiple_as.append(multiple_b)
	multiple_as.sort()
	total = sum(multiple_as)
	print('The sum of all multiples of', a, 'and', b, 'below', z, 'is', total)

sum_of_mults(3,5,1000)

# You can confirm plugging in 3, 5 and 10 gives an answer of 23 as described in the question 'sum_of_mults(3,5,10)'
