#Check Leap Year

yearInput = int(input("Please enter a year:"))

points = 0

if (yearInput % 100 == 0):
    if (yearInput % 400 == 0):
        points += 1
else:
    if (yearInput % 4 == 0):
        points += 1

if points > 0:
    print("This year is a leap year")
else:
    print("This year is not a leap year")

    
