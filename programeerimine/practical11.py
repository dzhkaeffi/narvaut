import json
import os
try:
    dict = json.load(open("dictionary.txt", 'r'))
except:
    dict = dict()
while True:
    word = input("\nEnter a word (done to quit, reset to reset and quit): \033[1;32;40m").lower()
    print("\033[0;37;40m", end="")
    if word != 'done':
        if dict.get(word) is not None:
            print()
            print('{} means \033[1;32;40m{}\033[0;37;40m'.format(word, dict[word]))
        elif word == "reset":
            if os.path.exists("dictionary.txt"):
                os.remove("dictionary.txt")
                print("File deleted!")
                exit()
            else:
                print("File does not exist!")
        else:
            print('There is no information for {}'.format(word))
            dict[word] = input('What does {} mean? \033[1;32;40m'.format(word)).lower()
            print('\033[0;37;40m', end="")
    else:
        break
print('The dictionary has {} entries in it.'.format(len(dict)))
print('All records in the dictionary: \033[1;32;40m{}\033[0;37;40m'.format(dict))
json.dump(dict, open("dictionary.txt",'w+'))