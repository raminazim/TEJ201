import random # I Don't Know If We Allowed To Use Libraries 🤷‍♂️

NumOne = random.randint(1,10)
Op = random.randint(1,4)
NumTwo = random.randint(1,10)

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