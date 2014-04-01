fib1 = 1
fib2 = 2
end_sum = 0

while fib2 < 4000000:
    if fib2 % 2 == 0:
        end_sum += fib2
    next_fib_num = fib1 + fib2
    fib1 = fib2
    fib2 = next_fib_num

print end_sum
