file = open("temps.txt")
fahr = []
for line in file:
    fahr.append(int(line)*9/5+32)
print("Minimum:", min(fahr))
print("Maximum:", max(fahr))
print("Average:", sum(fahr)/len(fahr))

