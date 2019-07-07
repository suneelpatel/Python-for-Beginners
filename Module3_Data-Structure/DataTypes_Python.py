# -*- coding: utf-8 -*-
"""

There are eight native datatypes in Python.

Boolean
Numbers
Strings
Bytes & Byte Arrays
Lists
Tuples
Sets
Dictionaries

Let us look at how to implement these data types in Python.
"""

#Boolean
number = [1,2,3,4,5]
boolean = 3 in number
print(boolean)
 
#Numbers
num1 = 5**3
num2 = 32//3
num3 = 32/3
print('num1 is',num1)
print('num2 is',num2)
print('num3 is',num3)
 
#Strings
str1 = "Welcome"
str2 = " to Edureka's Python Programming Blog"
str3 = str1 + str2
print('str3 is',str3)
print(str3[0:10])
print(str3[-5:])
print(str3[:-5])
 
#Lists
countries = ['India', 'Australia', 'United States', 'Canada', 'Singapore']
print(len(countries))
print(countries)
countries.append('Brazil')
print(countries)
countries.insert(2, 'United Kingdom')
print(countries)
 
#Tuples
sports_tuple = ('Cricket', 'Basketball', 'Football')
sports_list = list(sports_tuple)
sports_list.append('Baseball')
print(sports_list)
print(sports_tuple)
 
#Dictionary
#Indian Government
Government = {'Legislature':'Parliament', 'Executive':'PM & Cabinet', 'Judiciary':'Supreme Court'}
print('Indian Government has ',Government)
#Modifying for USA
Government['Legislature']='Congress'
Government['Executive']='President & Cabinet'
print('USA Government has ',Government)