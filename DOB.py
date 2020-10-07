import datetime
x = datetime.datetime.now()
#print(type(x.year))

DOB = input("enter your year of birth DD-MM-YYYY")
#water = []
water = [int(s) for s in DOB.split() if s.isdigit()]
#print("The numbers list is : " + str(water))
mnth = water[1:2]
# Destructuring list 'water' by assigning to abc
DOB_day, DOB_month, DOB_year = water
calculatedMnth = x.month - DOB_month
# converting negative numbers(integers) to positive
calculatedDay = x.day - DOB_day
calculatedYear = x.year - DOB_year
#Y = abs(Y)
print( "your", calculatedYear, "th, birthday will be in", calculatedDay, "days", "and", calculatedMnth, "months")
if calculatedMnth < 0:
    calculatedMnth = abs(calculatedMnth)
    realAge = calculatedYear - 1
    print("your current age is", realAge, "and your birthday this year is in ", calculatedMnth, "months and",
          calculatedDay, "days")
else:
    realAge = calculatedYear
    print("your current age is", realAge, "and your birthday was", calculatedMnth, "months and",
          calculatedDay, "days ago")

#answer = x - DOB

#print("you are", answer)

