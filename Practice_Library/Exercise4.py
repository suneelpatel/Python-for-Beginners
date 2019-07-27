# Case: Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose if the entered string is: Python0325
# Then the output will be:
# LETTERS: 6
# DIGITS:4

s=input("Enter the sentence :")

d={'LETTER':0,'DIGIT':0}
for c in s:
    if c.isalpha():
        d['LETTER']+=1
    elif c.isdigit():
        d['DIGIT']+=1
    else:
        pass
print("LETTER:",d['LETTER'])
print('DIGIT:',d['DIGIT'])
