filename = input("Enter your file name [ex. names.txt]: ")
linecount = 0
try:
    file = open(filename)
    for line in file:
        linecount += 1
        print('{}.'.format(linecount), line, end="")

except:
    print("No such file")


