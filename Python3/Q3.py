import random

NumOne = random.randint(1,11)
Op = random.randint(1,5)
NumTwo = random.randint(1,11)

if Op == 1:
    Ans = NumOne + NumTwo
    Op = str('+')
elif Op == 2:
    Ans = NumOne - NumTwo
    Op = str('-')
elif Op == 3:
    Ans = NumOne * NumTwo
    Op = str('*')
elif Op == 4:
    Ans = NumOne / NumTwo
    Op = str('/')

UsrAns = int(input(print('Answer: ' , NumOne , Op , NumTwo)))

if UsrAns > Ans:
    print('Too High')
elif UsrAns < Ans:
    print('Too Low')
else:
    print('Correct')
