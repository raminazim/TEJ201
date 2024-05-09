Num = int(input('Enter a Number: '))
Factorial = 1
Counter = 1

if Num < 0:
     print('Invalid input')
else:
     print('Answer:', Num, end= '! =')

     while Counter <= Num:
          if Counter != 1:
               print('x',  end= ' ')

          print(Counter, end=' ')
          Factorial *= Counter

          Counter += 1

     print(' =', Factorial)

# Not Sure About Using 'end=' Parameters But Basically Doesn't Let It Make A New Line