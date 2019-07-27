
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