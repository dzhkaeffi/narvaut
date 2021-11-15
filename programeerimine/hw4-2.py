def number_of_days(month):
    if 1 <= month <= 12:
        days = [31, "28/29", 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        print('That month has {} days in it.'.format(days[month - 1]))
    else:
        print("The number must be in the range of 1-12")

while True:
    month = input("Enter number of a month or word 'done': ")
    if month.lower() != "done":
            try:
                number_of_days(int(month))
            except:
                print("Enter a number!")
    else:
        break