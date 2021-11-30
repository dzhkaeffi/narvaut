import re #regex

hand = open("war_and_peace.txt", encoding="utf8").read().replace('\n', ' ')

pattern = r'\bP\w+' # Words starting with P
patternfound = re.findall(pattern, hand)
for line in patternfound:
    print('Words Starting with "P":', line)

matches = re.findall(r'\b\w+\b', hand) # Words containing WAR
for match in matches:
    if re.search('war|wra|raw|rwa|awr|arw', match):
        print('Does contain any combination of "WAR": ', match)
    if re.search('(?i)[eiokl]', match):
        continue
    else:
        print('Does not contain "e, i, o, k, l":', match)
