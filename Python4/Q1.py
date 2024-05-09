
Name = input('Name: ')
intGrades = int(input('# of Grades: '))
TotalGrade = 0
AverageGrade = 0
LetterGrade = ''
GradeNum = 1


while GradeNum <= intGrades:
     dblGrade = float(input('Grade: ' + str(GradeNum) + ': '))
     TotalGrade += dblGrade
     GradeNum += 1

AverageGrade = TotalGrade / intGrades
AverageGrade = round(AverageGrade)

if AverageGrade >= 90:
     LetterGrade = 'A'
elif AverageGrade >= 80:
     LetterGrade = 'B'
elif AverageGrade >= 70:
     LetterGrade = 'C'
elif AverageGrade >= 60:
     LetterGrade = 'D'
else:
     LetterGrade = 'F'

print()
print('Hello', Name)
print('Average:', AverageGrade, '%')
print('Letter Grade:', LetterGrade)


if LetterGrade == 'A':
     print('Great')
elif LetterGrade == 'B':
     print('Good')
elif LetterGrade == 'C':
     print('Nice')
elif LetterGrade == 'D':
     print('Cool')
elif LetterGrade == 'F':
     print('Loser')
