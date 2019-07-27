# Case: Write a program, which will find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line.
# Hint: In case of input data being supplied to the question, it should be assumed to be a console input. Divide each digit with 2 and verify is it even or not.

values=[]

for i in range(1000,3001):
    s=str(i)
    if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0:
        values.append(s)
print(",".join(values))
