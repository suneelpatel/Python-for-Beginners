# Case: Write a for loop that prints all elements of a list and their position in the list. 
# a = [4,7,3,2,5,9] 

# Hint: Use Loop to iterate through list elements.


a = [4,7,3,2,5,9]

for item in a:
    print(str(item) + " Position of element "+ str(a.index(item)+1))
