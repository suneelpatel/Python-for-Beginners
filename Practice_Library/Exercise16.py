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
