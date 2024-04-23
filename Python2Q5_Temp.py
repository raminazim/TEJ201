#Name: Ramin
#Date: 04/30/24
#Title: Digit Seperate
#Purpose: Seperate Digits

change = int(input("Change: "))

quarters = change // 25
remainingCents = change % 25

dimes = remainingCents // 10
remainingCents %= 10

nickels = remainingCents // 5
remainingCents %= 5

pennies = remainingCents

print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
