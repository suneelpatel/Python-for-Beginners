# Case1: Write a program which will find factors of given number and find whether the factor is even or odd.
# Hint: Use Loop with if-else statements

num=int(input("Enter the number:"))

for i in range(1,num+1):
    res=num%i
    if res==0: #Nested if statement
        if i%2==0:
            print(i,"Factor is Even")
        else:
            print(i,"Factor is odd")


print("\nGood Bye")
