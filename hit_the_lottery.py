n = int(input())

bills = [100, 20, 10, 5, 1]

counter = 0

for bill in bills:
    counter += n // bill
    n %= bill

print(counter)