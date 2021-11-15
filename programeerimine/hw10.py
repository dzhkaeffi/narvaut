dish = input("\nWhat dish would you like to have? - ")
print()
file = open("food.txt", 'r')

def check():
    containsdish = False
    f = open("food.txt")
    for line in f:
        if dish in line:
            containsdish = True
            break
    return containsdish

pricesstr = []
prices = []
if dish != "" and dish != " ":
    if check():
        for line in file:
            if line.__contains__(dish):
                    restaurant = line[:line.find("-")]
                    price = line[line.find(",")+1:]
                    print('You can have {} in {} for {} EUR.'.format(dish, restaurant.strip(), price.strip()))
                    pricesstr.append(str(price.strip())) 
                    prices.append(float(price.strip()))
                    minprice = min(pricesstr)
    else:
        print("This dish is not served in restaurants of Narva.")
        exit()
else:
    print('Input cannot be blank!')
    exit()
print()
print("Difference between minimum and average prices is {:.2f} EUR.".format(sum(prices)/len(prices)-min(prices)))
for line in open("food.txt"):
    if line.__contains__(dish):
        if line[line.find(",")+1:].strip() == minprice:
            restaurantmin = line[:line.find("-")]
            print('Minimum price {} EUR is in {}.'.format(minprice, restaurantmin.strip()))
print("Average price is {} EUR.".format(sum(prices)/len(prices)))


