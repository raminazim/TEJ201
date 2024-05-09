import random

Num = 0
Num1, Num2, Num3 = 0.0, 0.0, 0.0
intCounter = 0

while Num < 3:
    Num = int(input(print("Enter Number < 3: ")))

while True:
    random.seed()
    Num1 = random.randint(1, Num)
    Num2 = random.randint(1, Num)
    Num3 = random.randint(1, Num)
    intCounter += 1

    if Num1 != Num2 and Num1 != Num3 and Num2 != Num3:
        break

print("Num 1:", Num1, "  Num 2:", Num2, "  Num 3:", Num3, "  Attempts:", intCounter)
