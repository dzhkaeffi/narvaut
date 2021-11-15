try:
    amount = float(input("The amount of money to convert? "))
    curr = input("Current currency: ")
    into = input("Exchange into: ")
    if (curr.lower() == "dollar" and into.lower() == "euro"):
        print(amount/1.17)
    elif (curr.lower() == "euro" and into.lower() == "dollar"):
        print(amount*1.17)
    else:
        print("The currency rate on 18.09.2018 at 16 p.m.: 1 € = $1.17")
except:
    print("The currency rate on 18.09.2018 at 16 p.m.: 1 € = $1.17")