#Name: Ramin
#Date: 04/30/24
#Title: Digit Seperate
#Purpose: Seperate Digits

change = int(input("Change: "))

# Calculate the number of quarters
quarters = change // 25
remainingCents = change % 25

# Calculate the number of dimes
dimes = remainingCents // 10
remainingCents %= 10

# Calculate the number of nickels
nickels = remainingCents // 5
remainingCents %= 5

# The remaining cents will be the number of pennies
pennies = remainingCents

# Output the result
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
