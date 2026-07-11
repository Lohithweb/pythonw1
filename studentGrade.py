m1 = float(input("Enter Marks 1: "))
m2 = float(input("Enter Marks 2: "))
m3 = float(input("Enter Marks 3: "))

average = (m1 + m2 + m3) / 3

print("Average =", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: F")