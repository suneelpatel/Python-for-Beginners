# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 16:33:59 2019

@author: HP
"""

# Defining a function to reverse a string
 
def reverse_a_string():
    # Reading input from console
    a_string = input("Enter a string")
    new_strings = []
 
    # Storing length of input string
    index = len(a_string)
 
    # Reversing the string using while loop
    while index:
        index -= 1
        new_strings.append(a_string[index])
 
    #Printing the reversed string
    print(''.join(new_strings))
 
reverse_a_string()