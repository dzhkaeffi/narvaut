def repeat(string, times):
    i = 0
    while i < times:
        print(string)
        i += 1

try:
    string = input("Enter your string: ")
    times = int(input("How many times to repeat: "))
    repeat(string, times)
except:
    print("Invalid values!")
    exit()