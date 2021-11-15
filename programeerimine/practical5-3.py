firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
email = input("Please enter your e-mail: ")
occupation = input("Please enter your occupation: ")
for line in range (1, 8):
    if line == 1 or line == 7:
        print("+" + "-" * 30 + "+")
    elif line == 3:
        print("|" + (firstname.title() + " " + lastname.title() + " - " + email).center(30) + "|")
    elif line == 5:
        print("|" + occupation.center(30) + "|")
    else:
        print("|" + "".center(30) + "|")
