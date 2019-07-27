num=int(input("Enter the number:"))

for i in range(1,num+1):
    res=num%i
    if res==0: #Nested if statement
        if i%2==0:
            print(i,"Factor is Even")
        else:
            print(i,"Factor is odd")


print("\nGood Bye")