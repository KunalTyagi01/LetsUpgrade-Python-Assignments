def print_month_name(x):
    if (x == 1):
        print("January")
        print("No. of days: 31 days")
    if (x == 2):
        print("Feburary")
        print("No. of days: 28/29 days")
    if (x == 3):
        print("March")
        print("No. of days: 31 days")
    if (x == 4):
        print("April")
        print("No. of days: 30 days")
    if (x == 5):
        print("May")
        print("No. of days: 31 days")
    if (x == 6):
        print("June")
        print("No. of days: 30 days")
    if (x == 7):
        print("July")
        print("No. of days: 31 days")
    if (x == 8):
        print("August")
        print("No. of days: 31 days")
    if (x == 9):
        print("September")
        print("No. of days: 30 days")
    if (x == 10):
        print("October")
        print("No. of days: 31 days")
    if (x == 11):
        print("November")
        print("No. of days: 30 days")
    if (x == 12):
        print("December")
        print("No. of days: 31 days")
    if (x < 1 or x > 12):
        print("Invalid input")

month = int(input("Enter the month number: "))
print_month_name(month)