answer = 0

for i in range(1000):
    if i%3 == 0:
        answer += i
    elif i%5 == 0:
        answer += i

print answer
