def find_name(file):
    content = open(file)
    for line in content:
        print('Username is {}'.format(line[line.find("~") + 1:line.find("/", line.find("~") + 1)]))


name = input("Enter your file name [ex. urls.txt]: ")
find_name(name)
