def sum_squares(a):
	b = 0
	for i in range(1,a+1):
		b = b + (i ** 2)
	return b
	
def square_sum(a):
	b = 0
	for i in range (1,a+1):
		b = b + i
	return b ** 2

def compute(a):
	ans = square_sum(a) - sum_squares(a)
	return ans
	
print(compute(100))