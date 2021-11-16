import json
try:
    dict = json.load(open("dictionary.txt", 'r'))
except:
    dict = dict()
while True:
    word = input("\nEnter a word (done to quit): \033[1;32;40m").lower()
    print("\033[0;37;40m", end="")
    if word != 'done':
        if dict.get(word) is not None:
            print('{} means \033[1;32;40m{}\033[0;37;40m'.format(word, dict[word]))
        else:
            print('There is no information for {}'.format(word))
            dict[word] = input('What does {} mean? \033[1;32;40m'.format(word))
            print('\033[0;37;40m', end="")
    else:
        break
print('The dictionary has {} entries in it.'.format(len(dict)))
print('All records in the dictionary: \033[1;32;40m{}\033[0;37;40m'.format(dict))
json.dump(dict, open("dictionary.txt",'w+'))