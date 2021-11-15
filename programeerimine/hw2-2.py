try:
    month = int(input("Enter the number of a month: "))
    year = int(input("Please enter a year: "))
    if month >= 1 and month <= 12:    
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days = [31,29,31,30,31,30,31,31,30,31,30,31]
            print("That month has", days[month-1], "days in it (leap year).")
        else:
            days = [31,28,31,30,31,30,31,31,30,31,30,31]
            print("That month has", days[month-1], "days in it (common year).")            
    else: 
        print("The number of a month must be in the range [1-12]")
except:
    print("Please enter a number")


