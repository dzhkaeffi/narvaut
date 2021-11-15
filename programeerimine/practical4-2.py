try:
    customers = int(input("Enter the number of customers: "))
except:
    print("Try using numbers!")
    exit()

i = 0
sum = 0
while i <= customers:
    if i % 2 != 0:
        sum += i
    i += 1
        
print('You will need to give away {} flowers.'.format(sum))