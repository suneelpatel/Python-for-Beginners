# Case: Design a code which will find the given number is Palindrome number or not.
# Hint: Use built-in functions of string.

my_str=input("Enter the Value: ")  # change this value for a different output

my_str=my_str.casefold() # make it suitable for caseless comparison

rev_str=reversed(my_str) # reverse the string

if list(my_str)==list(rev_str): # check if the string is equal to its reverse
    print("It is palindrome")
else:
    print("It is not palindrome")
