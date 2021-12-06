import datetime
from collections import Counter

file = open("bdays.txt")

counts = dict()
list = []

for line in file:
    year = line.split("-")[0]
    list.append(year)

for i in list:
    counts[i] = counts.get(i, 0) + 1

topthree = dict(Counter(counts).most_common(3))
print(topthree)
# print(counts)