personalcode = input("Enter your personal code: ")
try:
    int(personalcode)
except:
    print("Enter correct personal code!")
    exit()

if (int(personalcode[0]) % 2) == 0:
    print("The person is a female")
else:
    print("The person is a male")