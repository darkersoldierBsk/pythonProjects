
"""
    List all prime numbers up to a given number
"""

last_num = int(input("What number are you looking for prime numbers up to? : "))
prime_nums = []

for i in range(2, last_num):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_nums.append(i)

print("The prime numbers between 0 ve " + str(last_num) + " are: " + str(prime_nums)[1:-1])
