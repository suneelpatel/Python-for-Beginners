#Table of Content
1. Learn Basics Concept of Python
2. Downloading & Installation
3. Python Applications
4. Python Variables
5. Python Keywords
6. Python Identifiers
7. Python Literals
8. Python Operators
9. Data Structure
10. Conditional Statement
11. Flow Contorl
12. Loops in Python
13. Functions
14. File Operations
15. Eception Handling


# 1. Learn Basics Concept of Python

## What is Python?
* Created in 1991 by Guido Van Rossum
* Named after Monty Python’s Flying Circus
* Is an interpreted, Object-Oriented, High Level Programming Language with dynamic semantics.
* Gained popularity because of its clear syntax and readability

## Why Learn Python?
Python’s syntax is very easy to understand. The lines of code required for a task is less compared to other languages. Let me give you an example – If I have to print “Welcome To Edureka!”  all I have to type:

print (“Welcome To Edureka!”)

Let’s see, What experts have to say about Python:

* Simple and Easy to learn
* Free and open source
* High Level Language
* Support different programming paradigm
    - Object Oriented
    - Procedure Oriented
    - Functional Oriented
    - Imperative Oriented
* Portable

# 2. Downloading & Installation
I will be installing Python in Windows 10 OS. You can try installing Python in Linux, Mac etc. If you face any issue mention it in the comments section.

### Following are the steps to install Python
* Step1: 1. Go to www.python.org/downloads/
* Step2: Select the Operating System and also the version of Python. I am downloading 3.6.0 in my windows machine.  Open the installer and click on “Run”.
* Step3: Click on “Install Now” and check on “Add Python 3.6 to PATH”.
* Step4: Start IDLE which is a Python GUI and start scripting.


### Python IDE (Integrated Development Environment):
IDE typically provides code editor, compiler/ interpreter and debugger in one GUI (Graphical User Interface). It encapsulates the entire process of code creation, compilation and testing which increases the productivity of developers.

A developer working with an IDE starts with a model, which the IDE translates into suitable code. The IDE then debugs and tests the model-driven code, with a high level of automation. Once the build is successful and properly tested, it can be deployed for further testing through the IDE or other tools outside of the IDE.

# 3. Python Applications:
* Artificial Intelligence
* Data Science
* Desktop Application
* Automation
* Web Development
* Data Wrangling, Exploration And Visualization


# 4. Python Variables
* A Python variable is a reserved memory location to store values. In other words, a variable in a python program gives data to the computer for processing. 
* Variables are containers for storing data values. Unlike other programming languages, Python has no command for declaring a variable.

### Python Variable Name Rules
* Must begin with a letter (a - z, A - B) or underscore (_)
* Other characters can be letters, numbers or _
* Case Sensitive.
* Can be any (reasonable) length.
* There are some reserved words which you cannot use as a variable name because Python uses them for other things.

## Python Tokens
* Keyword
    - Python keywords are special reserve keywords
* Identifiers
    - Names that the programmer defines
* Literals
    - Values classified by types: e.g., numbers, truth values, text
* Operators
    - Symbols that operate on data and produce results
    
# 5. Python Tokens: Keywords
* Python keywords are special reserve keywords
* Convey a special meaning to the compiler/interpreter
* Each keywords have a special meaning and a specific operation
* Keywords CANNOT be used as variable

# 6. Python Tokens: Identifiers
* Identifiers are the name to identify a variable, function, class or an object
* RULES defined for naming an identifiers:
    - No special character except underscore (_) can be used as an identifier
    - Keywords should not be used as an identifiers
    - Python is case sensitive, i.e. Var and var are two different identifier
    - First character of an identifier can be character, underscore(_) but not digit.
    
# 7. Python Tokens: Literals
Literals are data given in a variable or constant
* String Literals
    - Formed by enclosing a text in the quotes
    - Both single and double quotes can be used
* Numeric Literals
    - Int   |   long    |   Float   |   Complex
* Boolean Literals
    - Can have only two values: 	True    |   False
* Special Literals
    - Python has one special literal: None
    - Used to specify to the field that is not created

# 8. Python Tokens: Operators
* Arithmetic Operator
* Assignment Operator
* Comparison Operator
* Logical Operator
* Bitwise Operator
* Identity Operator
* Membership Operator


# 9. Data Structure (Data Types in Python)
* Immutable Data
    - Numeric : 
    There are three numeric types in Python:
        - Int :Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
        - Float : Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
        - Complex : Complex numbers are written with a "j" as the imaginary part:
    - String :
    Combination of characters within the single or double quotes or it's a contiues series of characters surrounded by single or double quotes
    - Tuples :
    A tuple is a collection which is ordered and immutable (unchangeable). In Python tuples are written with round brackets.
 
 * Mutable Data
    - List :
    A list is a collection which is ordered and changeable. In Python lists are written with square brackets. [ ]
    - Set :
    A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets { }
    - Dictionary :
    A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets { }, and they have keys and values in each items.


# 10. Conditional Statement
Python Conditional Statement : If ... Else Statement

Python Conditional Operators (conditions) and If statements

Python supports the usual logical conditions from mathematics:

Equals: a == b Not Equals: a != b Less than: a < b Less than or equal to: a <= b Greater than: a > b Greater than or equal to: a >= b

# 11. Flow Control
Flow Control lets us define a flow in executing our programs. To mimic the real world, you need to transform real world situations into your program. For this you need to control the execution of your program statements using Flow Controls.

There are six basic flow controls used in Python programming:

* if
* for
* while
* break
* continue
* pass

#### If Statement :
The Python compound statement ’if’ lets you conditionally execute blocks of statements.

#### For Statement:
The for statement supports repeated execution of a statement or block of statements that is controlled by an iterable expression.

#### While Statement: 
The while statement in Python programming supports repeated execution of a statement or block of statements that is controlled by a conditional expression.

#### Break Statement: 
The break statement is allowed only inside a loop body. When break executes, the loop terminates. If a loop is nested inside other loops, break terminates only the innermost nested loop.

#### Continue Statement:
The continue statement is allowed only inside a loop body. When continue executes, the current iteration of the loop body terminates, and execution continues with the next iteration of the loop.

#### Pass Statement: 
The pass statement, which performs no action, can be used as a placeholder when a statement is syntactically required but you have nothing specific to do.


# 12. Loops in Python
In general, statements are executed sequentially: The first statement in a function is executed first, followed by the second, and so on. There may be a situation when you need to execute a block of code several number of times.

Programming languages provide various control structures that allow for more complicated execution paths.

A loop statement allows us to execute a statement or group of statements multiple times. 

* while loop :
Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.

* for loop :
Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.

* nested loops: 
You can use one or more loop inside any another while, for or do..while loop.

### Loop Control Statements:
* Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed

    - 1. Break Statement : Terminates the loop statement and transfer execution to the statement immediately following the loop
    - 2. Continue Statement: Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating
    - 3. Pass Statement: The pass statement in Python is used when a statement is required syntactically but you don't want any command or code to execute  

# 13. Functions

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

In other words, Functions in Python programming, is a group of related statements that performs a specific task. Functions make our program more organized and help in code re-usability.

#### Uses Of Functions:
* Functions help in code reusability
* Functions provide organization to the code
* Functions provide abstraction
* Functions help in extensibility

# 14. File Operations / File Handling

File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

### File Handling

File Handling refers to those operations that are used to read or write a file.

To perform file handling, we need to perform these steps:

* Step1: Open File
* Step2: Read / Write File
* Step3: Close File


The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

#### Opening A File:

Python has a built-in function open() to open a file
This function returns a file object, also called a handle, as it is used to read or modify the file accordingly


#### Writing To A File:

In order to write into a file we need to open it in write ‘w’, append ‘a’ or exclusive creation ‘x’ mode
We need to be careful with the ‘w’ mode as it will overwrite into the file if it already exists. All previous data are erased
Writing a string or sequence of bytes (for binary files) is done using write() method

#### Reading From A File:
To read the content of a file, we must open the file in the reading mode
We can use the read(size) method to read in size number of data
If size parameter is not specified, it reads and returns up to the end of the file

#### Closing A File:
When we are done with operations to the file, we need to properly close it.
Closing a file will free up the resources that were tied with the file and is done using the close() method.

### File Operations Using Python – CRUD Operation In Python:

What are the various file operations that you can generally perform?

We call it CRUD. CRUD stands for:

* Create
* Read
* Update
* Delete


There are four different methods (modes) for opening a file:

    - "r" - Read - Default value. Opens a file for reading, error if the file does not exist

    - "a" - Append - Opens a file for appending, creates the file if it does not exist

    - "w" - Write - Opens a file for writing, creates the file if it does not exist

    - "x" - Create - Creates the specified file, returns an error if the file exists

* In addition you can specify if the file should be handled as binary or text mode

    - "t" - Text - Default value. Text mode

    - "b" - Binary - Binary mode (e.g. images)
    

### Types Of Files Supported By Python
Can you quickly think of all of the types of files that you know? Image, audio, video, text, scripts and many more.

The dependency on the native Operating System is the most important thing to keep in mind when considering the type of files supported.

Windows supports all of the file types mentioned in the first line. But does it support every type of file? Absolutely not! There are certain limitations here as well.

Now, coming to Python – There are 2 types of files mainly:

* Binary
* Text

A binary file is any type of file that is not a text file. Because of their nature, binary files can only be processed by an application that knows or understand the file’s structure. In other words, they must be applications that can read and interpret binary.

Text files are structured as a sequence of lines, where each line includes a sequence of characters. This is what you know as code or syntax. Each line is terminated with a special character, called the EOL or End of Line character.

# 15. Exception Handling:

The "try" block lets you test a block of code for errors.

The "except" block lets you handle the error.

The "finally" block lets you execute code, regardless of the result of the try- and except blocks.
