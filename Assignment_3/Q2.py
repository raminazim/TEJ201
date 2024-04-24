Movie = (input('Movie Name: '))
Rating = int(input('Movie Rating: '))

if Rating > 5:
    print('Invalid')
elif Rating > 4:
    print(Movie , ': ⭐⭐⭐⭐⭐')
elif Rating > 3:
    print(Movie , ': ⭐⭐⭐⭐')
elif Rating > 2:
    print(Movie , ': ⭐⭐⭐')
elif Rating > 1:
    print(Movie , ': ⭐⭐')
elif Rating > 0:
    print(Movie , ': ⭐')
else:
    print(Movie , ': No Star')
