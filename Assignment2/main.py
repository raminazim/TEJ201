import random

intQ1Num1 = random.randint(0, 26)
intQ1Num2 = random.randint(0, 26)
intQ1Ans = intQ1Num1 + intQ1Num2

intQ2Num1 = random.randint(0, 26)
intQ2Num2 = random.randint(0, 26)
intQ2Ans = intQ2Num1 - intQ2Num2

intQ3Num1 = random.randint(0, 26)
intQ3Num2 = random.randint(0, 26)
intQ3Ans = intQ3Num1 * intQ3Num2

intQ4Num1 = random.randint(0, 26)
intQ4Num2 = random.randint(1, 26)
intQ4Ans = intQ4Num1 / intQ4Num2

intQ5Num1 = random.randint(0, 26)
intQ5Num2 = random.randint(0, 10)
intQ5Ans = intQ5Num1 ** intQ5Num2

intScore = 0

print(intQ1Num1 , '+' , intQ1Num2)
intUsrInput = int(input())

if intUsrInput == intQ1Ans:
     print('Correct')
     intScore += 3
else:
     print(intQ1Num1, '+', intQ1Num2)
     intUsrInput = int(input())
     if intUsrInput == intQ1Ans:
          print('Correct')
          intScore += 2
     else:
          if intUsrInput > intQ1Ans:
               print('Answer Too High')
               print(intQ1Num1, '+', intQ1Num2)
               intUsrInput = int(input())
               if intUsrInput == intQ1Ans:
                    print('Correct')
                    intScore += 1
               else:
                    print('Answer was ' , intQ1Ans)
          else:
               print('Answer Too Low')
               print(intQ1Num1, '+', intQ1Num2)
               intUsrInput = int(input())
               if intUsrInput == intQ1Ans:
                    print('Correct')
                    intScore += 1
               else:
                    print('Answer was ' , intQ1Ans)

print(intQ2Num1 , '-' , intQ2Num2)
intUsrInput = int(input())

if intUsrInput == intQ2Ans:
     print('Correct')
     intScore += 3
else:
     print(intQ2Num1, '-', intQ2Num2)
     intUsrInput = int(input())
     if intUsrInput == intQ2Ans:
          print('Correct')
          intScore += 2
     else:
          if intUsrInput > intQ2Ans:
               print('Answer Too High')
               print(intQ2Num1, '-', intQ2Num2)
               intUsrInput = int(input())
               if intUsrInput == intQ2Ans:
                    print('Correct')
                    intScore += 1
               else:
                    print('Answer was ' , intQ2Ans)
          else:
               print('Answer Too Low')
               print(intQ2Num1, '-', intQ2Num2)
               intUsrInput = int(input())
               if intUsrInput == intQ2Ans:
                    print('Correct')
                    intScore += 1
               else:
                    print('Answer was ' , intQ2Ans)

print(intQ3Num1 , '*' , intQ3Num2)
intUsrInput = int(input())

if intUsrInput == intQ3Ans:
     print('Correct')
     intScore += 3
else:
     print(intQ3Num1, '*', intQ3Num2)
     intUsrInput = int(input())
     if intUsrInput == intQ3Ans:
          print('Correct')
          intScore += 2
     else:
          if intUsrInput > intQ3Ans:
               print('Answer Too High')
               print(intQ3Num1, '*', intQ3Num2)
               intUsrInput = int(input())
               if intUsrInput == intQ3Ans:
                    print('Correct')
                    intScore += 1
               else:
                    print('Answer was ' , intQ3Ans)
          else:
               print('Answer Too Low')
               print(intQ3Num1, '*', intQ3Num2)
               intUsrInput = int(input())
               if intUsrInput == intQ3Ans:
                    print('Correct')
                    intScore += 1
               else:
                    print('Answer was ' , intQ3Ans)

print(intQ4Num1 , '/' , intQ4Num2)
intUsrInput = int(input())

if intUsrInput == intQ4Ans:
     print('Correct')
     intScore += 3
else:
     print(intQ4Num1, '/', intQ4Num2)
     intUsrInput = int(input())
     if intUsrInput == intQ4Ans:
          print('Correct')
          intScore += 2
     else:
          if intUsrInput > intQ4Ans:
               print('Answer Too High')
               print(intQ4Num1, '/', intQ4Num2)
               intUsrInput = int(input())
               if intUsrInput == intQ4Ans:
                    print('Correct')
                    intScore += 1
               else:
                    print('Answer was ' , intQ4Ans)
          else:
               print('Answer Too Low')
               print(intQ4Num1, '/', intQ4Num2)
               intUsrInput = int(input())
               if intUsrInput == intQ4Ans:
                    print('Correct')
                    intScore += 1
               else:
                    print('Answer was ' , intQ4Ans)

print(intQ5Num1, '**', intQ5Num2)
intUsrInput = int(input())

if intUsrInput == intQ5Ans:
     print('Correct')
     intScore += 3
else:
     print(intQ5Num1, '**', intQ5Num2)
     intUsrInput = int(input())
     if intUsrInput == intQ5Ans:
          print('Correct')
          intScore += 2
     else:
          if intUsrInput > intQ5Ans:
               print('Answer Too High')
               print(intQ5Num1, '**', intQ5Num2)
               intUsrInput = int(input())
               if intUsrInput == intQ5Ans:
                    print('Correct')
                    intScore += 1
               else:
                    print('Answer was ', intQ5Ans)
          else:
               print('Answer Too Low')
               print(intQ5Num1, '**', intQ5Num2)
               intUsrInput = int(input())
               if intUsrInput == intQ5Ans:
                    print('Correct')
                    intScore += 1
               else:
                    print('Answer was ', intQ5Ans)

print('Final Score: ' , intScore , '/15')
print('Percentage' , intScore/15 , '%')
if intScore > 10:
     print('Great Job')
elif intScore > 5:
     print('Good Job')
else:
     print('Do Better...')