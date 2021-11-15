file = open(input("Enter file name [ex. list]: ")+".txt")
arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for line in file:
    separate = line.split(".")
    print(arr[int(separate[1])-1])


