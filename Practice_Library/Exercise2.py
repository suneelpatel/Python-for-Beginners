my_str=input("Enter your word: ")

words=my_str.split()
words.sort()

for word in words:
    print(word)

print("\nGood Bye")