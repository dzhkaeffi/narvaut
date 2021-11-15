arr = []
sum = 0
sqarr = []
evens = 0
while True:
    number = input("Enter a number: ")
    if number != "done":
        try:
            num = int(number)
            if (num % 2) == 0:
                evens += 1
        except ValueError:
            print("This is not a number or 'done'")
    else:
        break
    sum += num
    arr.append(num)
    arr.sort()
print('Maximum:', max(arr))
print('Minimum:', min(arr))
print('Sum:', sum)
for i in arr:
    sqarr.append(i**2)
print('Squares:', sqarr)
print('Even numbers:', evens)
