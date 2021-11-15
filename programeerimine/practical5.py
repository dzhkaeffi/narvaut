string = input("Enter your word: ")
# for word in string:
#     print((string * len(word)).upper())
strlen = len(string)
print((string.upper() + "\n") * strlen)