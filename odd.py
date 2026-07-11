num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

prime = True

if num <= 1:
    prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

if prime:
    print("Prime Number")
else:
    print("Not a Prime Number")