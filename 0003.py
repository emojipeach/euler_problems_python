print("""The prime factors of 13195 are 5, 7, 13 and 29.""")

print("""What is the largest prime factor of the number 600851475143 ?""")

def find_factors(a):
	for i in range(1,a-1):
		if a % i == 0:
			factors.append(i)

def test_for_prime(b):
	for i in range(3,b):
		if b % i == 0:
			break
	else:
		primes.append(b)

def highest_prime_factor(x):
	find_factors(x)
	for i in factors:
		test_for_prime(i)
	print(max(primes))

factors = []
primes = []

highest_prime_factor(600851475143)