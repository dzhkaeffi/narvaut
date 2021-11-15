cents = int(input("Enter your amount of cents: "))
if cents < 100:
    print(cents, "cents")
elif (cents % 100) == 0:
    print(cents // 100, "euros")
else:
    print('{} euros and {} cents'.format(cents // 100, cents % 100))
