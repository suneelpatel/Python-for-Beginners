"""
Case: A website requires a user to input username and password to register. Write a program to check the validity of password given by user. Following are the criteria for checking password: 
1. At least 1 letter between [a-z] 
2. At least 1 number between [0-9] 
3. At least 1 letter between [A-Z] 
4. At least 1 character from [$#@] 
5. Minimum length of transaction password: 6 
6. Maximum length of transaction password: 12 

Hint: In case of input data being supplied to the question, it should be assumed to be a console input.

"""


print("Enter Password")

print("The password must be at least 6, and no more than 12 characters long")

password=input('Type your password here..:')

weak='Weak'
med='Medium'
strong='Strong'

if len(password)<6:
    print("password is too short It must be between 6 and 12 characters")
elif len(password)>12:
    print("password is too short It must be between 6 and 12 characters")
elif len(password)>=6 and len(password)<=12:
    print("Password ok ")
    if password.lower()==password or password.upper()==password or password.isalnum()==password:
        print("Password is:",weak)
    elif password.lower()==password and password.upper()==password or password.isalnum()==password:
        print("Password is:", med)
    else:
        password.lower()==password and password.upper()==password and password.isalnum()==password
        print("Password is:", strong)
