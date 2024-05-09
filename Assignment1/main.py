# Ramin
# 04/27/24
# Assignment
# Gather input and create a "story"

# Input

strName = input('Name: ')
intAge = int(input('Age: '))
strColour = input('Favorite Colour: ')

# Process
# Convert age to different time measurements
intAgeMo = intAge * 12 
intAgeDay = intAge * 365 
intAgeHr = intAge * 8760 
intAgeMin = intAge * 525600

# Converting earth age to mars & jupiter
intAgeMars = intAge / 1.88
intAgeJup = intAge / 11.86 

# Cubing age
intAgeCube = intAge ** 3

# Seperating Age
intAgeTen = intAge // 10
intAgeUnit = intAge % 10

#Output

print('Hey There ' , strName , ' You are ' , intAge , ' Years Old!')
print('That Is ' , intAgeMo , ' Months, ' , intAgeDay , ' Days, ' , intAgeHr , ' Hours, & ' , intAgeMin , ' Minutes!')
print('In Mars, You Would Be ' , intAgeMars , ' Years Old!')
print('In Jupiter, You Would Be ' , intAgeJup , ' Years Old!')
print('Your Age Cubed is ' , intAgeCube)
print('You Are ' , intAgeTen , 'Decades Old. With An Extra ' , intAgeUnit , ' Years!')
print('Your Favorite Colour Is ' , strColour)
