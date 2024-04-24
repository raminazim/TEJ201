Num = int(input(print('Enter Number: ')))

if Num > 999:
     print('Invalid')
elif Num > 99:
     print('3 Digit')
elif Num > 9:
     print('2 Digit')
else:
     print('1 Digit')