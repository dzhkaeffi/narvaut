file = open("prices.txt")
prices = []
data = file.readlines()
for i in range(len(data)):
    try:
        int(data[i])
        print(data[i-1].replace("\n", ""), "OK!")
        prices.append(data[i-1])
        prices.append(data[i])
    except ValueError:
        if i % 2 != 0:
            print("Could not convert the price of '{}'.".format(data[i-1].replace("\n", "")))
        continue

for i in range(len(prices)):
    if i % 2 != 0:
        prices[i] = str((int(prices[i]) - 0.01))+"\n"

f = open("new_prices.txt", "w+")
for data1 in prices:
    f.write(data1)
f.close()