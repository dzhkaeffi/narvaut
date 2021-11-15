word = input("Enter your word: ")
backwards = word[::-1]
if word == backwards:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
