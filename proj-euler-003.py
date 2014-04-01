prime_factors = set()

the_number = 600851475143

i = 1

while i < the_number:
    if the_number % i == 0:
        prime_factors.add(i)
    elif i > (the_number / 2):
        break
    i += 1

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True    

while True:
    test = max(prime_factors)
    if isprime(test) == True:
        break

print test
