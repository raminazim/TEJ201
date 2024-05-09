Item1 = Item2 = Item3 = Item4 = Item5 = 0
Price1, Price2, Price3, Price4, Price5 = 1, 1, 1, 1, 1
Total1 = Total2 = Total3 = Total4 = Total5 = 0.0
SubTotal = Tax = Total = 0.0
Money = Change = 0.0

print("Welcome")
print("Item 1: $1")
print("Item 2: $1")
print("Item 3: $1")
print("Item 4: $1")
print("Item 5: $1")

Item1 = int(input("Item 1 Quantity: "))
Item2 = int(input("Item 2 Quantity: "))
Item3 = int(input("Item 3 Quantity: "))
Item4 = int(input("Item 4 Quantity: "))
Item5 = int(input("Item 5 Quantity: "))

Total1 = Item1 * Price1
Total2 = Item2 * Price2
Total3 = Item3 * Price3
Total4 = Item4 * Price4
Total5 = Item5 * Price5
SubTotal = float(Total1 + Total2 + Total3 + Total4 + Total5)
Tax = (13 / 100) * SubTotal
Total = Tax + SubTotal
Total = round(Total, 2)
SubTotal = round(SubTotal, 2)

print("                      Receipt")
print("Item 1 Ordered                    ", Item1)
print("Item 1 Total Price                ", Total1, "$")
print("Item 2 Ordered                    ", Item2)
print("Item 2 Total Price                ", Total2, "$")
print("Item 3 Ordered                    ", Item3)
print("Item 3 Total Price                ", Total3, "$")
print("Item 4 Ordered                    ", Item4)
print("Item 4 Total Price                ", Total4, "$")
print("Item 5 Ordered                    ", Item5)
print("Item 5 Total Price                ", Total5, "$")
print("Sub Total                         ", SubTotal, "$")
print("Total                             ", Total, "$")

Money = float(input("User Pay: "))
Change = Money - Total
Change = round(Change, 2)
print("Change: ", Change)
