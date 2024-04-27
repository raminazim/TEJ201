GrossIncome = int(input('Income: '))
IncomeTax = 0
NetIncome = 0

if GrossIncome <= 49231:
    IncomeTax = GrossIncome * 0.2005
elif GrossIncome <= 53359:
    IncomeTax = 9870.8155 + ((GrossIncome - 49231) * 0.2415)
elif GrossIncome <= 86698:
    IncomeTax = 10867.7275 + ((GrossIncome - 53359) * 0.2965)
elif GrossIncome <= 98463:
    IncomeTax = 20752.741 + ((GrossIncome - 86698) * 0.3148)
elif GrossIncome <= 102135:
    IncomeTax = 24456.363 + ((GrossIncome - 98463) * 0.3389)
elif GrossIncome <= 106717:
    IncomeTax = 25700.8038 + ((GrossIncome - 102135) * 0.3791)
elif GrossIncome <= 150000:
    IncomeTax = 27437.84 + ((GrossIncome - 106717) * 0.4341)
elif GrossIncome <= 165430:
    IncomeTax = 46226.9903 + ((GrossIncome - 150000) * 0.4497)
elif GrossIncome <= 220000:
    IncomeTax = 53165.8613 + ((GrossIncome - 165430) * 0.4829)
else:
    IncomeTax = 79517.7143 + ((GrossIncome - 220000) * 0.4985)

NetIncome = GrossIncome - IncomeTax

print('Gross: ' , GrossIncome)
print('Income Tax Owed: ' , IncomeTax)
print('Net Income: ' , NetIncome)

# I Want Some Credit For All The Math I Did For This Shit