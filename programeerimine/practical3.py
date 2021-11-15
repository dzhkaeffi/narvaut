def screen_diagonal(distance):
    size = distance*100*0.39/2.5
    return size
try:
    distance = float(input("Enter the distance from the screen in meters: "))
except:
    print("Enter a valid distance!")
    exit()
print('Screen diagonal should be {} inches long.'.format(int(screen_diagonal(distance))))
# print("Screen diagonal should be "+str(int(screen_diagonal(distance)))+" inches long.")
