# I did use Adam's work as reference.
totalpoints = int(input('Please enter the number of points: '))

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def coordinates(point):
    x = input(f"Please enter x coordinate for {point}. point: ")
    y = input(f"Please enter y coordinate for {point}. point: ")
    return (int(x), int(y))

coords = []
for i in range(totalpoints):
    coords.append(coordinates(i+1))

print(coords)

lenghts = {}
for i in range(len(coords) - 1):
    for x in range(len(coords)):
        if i != x:
            lenghts[f'{i+1} and {x+1}'] = distance(coords[i][0], coords[i][1], coords[x][0], coords[x][1])

print(lenghts)
print(f'Points {min(lenghts, key=lenghts.get)} are the closest to each other')
