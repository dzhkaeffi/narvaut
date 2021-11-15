content = open("sample.txt")
valuesum = 0
linecount = 0
for line in content:
    linecount += 1
    try:
        value = int(line)
    except ValueError:
        value = 0
    valuesum += value
    print('{}.'.format(linecount), "*" * value)
print("In total {} stars".format(valuesum))