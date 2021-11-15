def price_difference(initial, prmonth, months):
    final = prmonth * months
    if initial > final:
        return initial - final
    else:
        return final - initial

price_difference()

def first_plan():
    try:
        monthly = float(input("Monthly payment: "))
        period = int(input("Plan duration (in months): "))
    except:
        print("Invalid values!")
    return monthly * period


def second_plan():
    try:
        monthly2 = float(input("Monthly payment in second plan: "))
        period2 = int(input("Plan duration in second plan (in months): "))
    except:
        print("Invalid values!")
    return monthly2 * period2


try:
    init = float(input("Initial price: "))
except:
    print("Invalid values!")

if first_plan() > second_plan():
    print("The second plan is better!")
else:
    print("The first plan is better!")
