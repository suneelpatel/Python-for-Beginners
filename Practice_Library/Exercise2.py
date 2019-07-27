# Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
# Hint: In case of input data being supplied to the question, it should be assumed to be a console input.

my_str=input("Enter your word: ")

words=my_str.split()
words.sort()

for word in words:
    print(word)

print("\nGood Bye")
