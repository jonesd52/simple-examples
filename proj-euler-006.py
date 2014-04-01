sum_of_squares = 0
squares_of_sums = 0
sums = 0

for i in range(1,101):
    sum_of_squares += i**2
    sums += i

squares_of_sums = sums**2

print squares_of_sums - sum_of_squares
