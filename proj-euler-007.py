search_for_prime = 10001

def isPrime(n):
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    i = 3
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 2

    return True

j = 1
p = 2

while j < search_for_prime:
    p += 1
    if isPrime(p) == True:
        j += 1

print "The ", j, " prime is: ", p
    
