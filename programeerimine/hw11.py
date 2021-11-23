import datetime

file = open("bdays.txt")

def weekday(date):
    return {
        '0': "Sunday",
        '1': "Monday",
        '2': "Tuesday",
        '3': "Wednesday",
        '4': "Thursday",
        '5': "Friday",
        '6': "Saturday",
    }[date]

list = []

for line in file:
    splitline = line.removesuffix("\n")
    splitline = splitline.split("-")
    date = datetime.datetime(int(splitline[0]), int(splitline[1]), int(splitline[2]))
    list.append(weekday(str(date.weekday())))
    
counts = dict()

for i in list:
    counts[i] = counts.get(i, 0) + 1

print(counts)


