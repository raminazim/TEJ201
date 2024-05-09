Combo1 = 28
Combo2 = 8
Combo3 = 5

print('Lock has been locked, unlock it.')

while True:
    Num1 = int(input('Number 1: '))
    Num2 = int(input('Number 2: '))
    Num3 = int(input('Number 3: '))

    if Num1 == Combo1 and Num2 == Combo2 and Num3 == Combo3:
        print("Unlocked")
        break
    else:
        print("Incorrect")
