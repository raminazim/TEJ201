C = int(input("Change: "))

Q = C // 25
RC = C % 25

D = RC // 10
RC %= 10

N = RC // 5
RC %= 5

P = RC

print("Quarters:", Q)
print("Dimes:", D)
print("Nickels:", N)
print("Pennies:", P)