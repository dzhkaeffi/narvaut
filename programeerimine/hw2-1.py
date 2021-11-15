try:
    points = float(input("Enter the number of points: "))
    if points > 100:
        print("You cannot obtain so many points")
    elif points >= 66:
        print("The obtained points are enough to be considered for admission")
    elif points < 0:
        print("You cannot obtain negative points")
    elif points < 66:
        print("The obtained points are not enough to be considered for admission")
except:
    print("Please enter a number [0-100]")
