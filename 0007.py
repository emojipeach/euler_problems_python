def is_prime(test_number):
	if test_number == 1:
		return False
	elif test_number < 4:
			return True
	elif test_number % 2 == 0:
		return False
	else:
		x = int(test_number ** (1/2)) + 1
		for i in range(3, x, 2):
			if test_number % i == 0:
				return False
		return True

def next_prime(primes):
	x = max(primes)
	for i in range(x + 1, x + 100000):
		if is_prime(i):
			primes.append(i)
			return

def nth_prime(n):
	while n > len(primes):
		next_prime(primes)
	print(max(primes))

primes = [2, 3, 5]
nth_prime(10001)