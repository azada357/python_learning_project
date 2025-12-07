# ctrl + b ----->close the side bar
# ctrl + shift +  M-----> show the error and warning
# ctrl + shift + p------> step 2--> format docment----> organize codes/ another way ----> ctrl + s
# ctrl + backtick(`) -----> open the terminal
# ctrl + alt + n -----> run the code
# python implenetation---> python code----> compiler{cpython , pypy , ironpython, jython}-----> PVM, JVM....etc ----> machine code (010101)
# variable---> def: a container to store data, value, information[int, float, str, bool]
# variable naming rules:
# 1. should start with a letter (a-z, A-Z) or underscore(_)
# 2. can contain letters, digits(0-9) or underscores(_)
# 3. case sensitive
# 4. should not be a reserved keyword (if, else, for, while, def, return, import, etc..)
# string---> triple quote """ """----> long sentenses
# function def. codes already made for a espesific task ex. print(), Len(), input()...etc
# Len()---> a fnction to find the length of a string
# arugment---> the value passed to a function when calling it
# print(argument[0:n])---> to print the value of the argument passed to it
# escape notation---> a special charater used to represent certain whitespace or non-printable characters---> \n, \t, \', \", \\
# escape sequence---> \n (new line), \t (tab space), \\ (backslash), \' (single quote), \" (double quote)
# formatting strings---> 1. f" " , .format() 2.add string with + operator
# methods---> a function that is associated with an object
# string methods---> lower(), upper(), strip()/lstrip or rstrip for one side [delete space], replace(), split(), find(), count()
# numbers
# operators---> arithmetic(+,-,*,/,//,%,**), assignment(=,+=,-=,*=,/=,//=,%=,**=), comparison(==,!=,>,<,>=,<=), logical(and, or, not)
# operators precedence---> 1. parentheses() 2. exponentiation** 3. multiplication*, division/, floor division//)(No decimal), modulus%--->reminder 4. addition+, subtraction- 5. comparison(==, !=, >, <, >=, <=) 6. logical(not) 7. logical(and) 8. logical(or)
# operator in ex. print("py" in "python")---> True
# augmented assignment operators ex. x += 1 ---> x = x + 1
# funtion round()---> to round a float number to the nearest integer
# function abs()---> to get the absolute value of a number
# data types---> int, float, str, bool
# modules---> a file containing python code (functions, variables, classes) that can be imported and used in other python files
# import math---> to import the math module
# import math.sqrt()---> to import only the sqrt function from the math module
# import math.ceil()---> to import only the ceil function from the math module
# change type---> int(), float(), str(), bool()
# change type for bool()---> 0, 0.0, "", [], (), {} ----> False ; other than these ----> True
# comprison operators---> ==, !=, >, <, >=, <=
# function ord()---> to get the unicode code point of a character
# conditiional statements---> if, elif, else
# if statment : indentation (4 spaces or 1 tab)
# elif stentment: to check multiple conditions, it comes after if statment, and before else statment, Many elif can be used, INDEATATION
# else: to execute a block of code when all previous conditions are false, it comes at the end of if-elif statments, INDEATATION
# ternary operator---> value_if_true if condition else value_if_false
# short circuiting---> when the second oper and is not evaluated because the first operand determines the result of the expression
# between conditions---> and, or, not
# for loop---> to iterate over a sequence (list, tuple, string) or other iterable objects
# type complex-----> range is acomplex type, in contrast to int, float ..etc it is iterable
# list---> a collection which is ordered and changeable, allows duplicate members, defined by square brackets [] [iterable]
# while loop---> to execute a block of code as long as a condition is true
# while condition:----> indentation (4 spaces or 1 tab)
# comamand = " "   while command != "exit":----> to run the loop until the user types exit print(input("..."))   print
# def a function---> def function_name(parameters):----> indentation (4 spaces or 1 tab)
# we have two types of functions: 1. doing a task (print()) 2. returning a value (return) ex.round(), abs()
# def greet(first_name):----> function def.
#     print(f"hello {first_name}")----> function body
# greet("aza")----> function call
# return keyword---> to return a value from a function
# def greet(first_name):
#     return f"hello {first_name}"
# message = greet("aza")
# print(message)
# key word arguments---> arguments that are passed to a function by explicitly specifying the parameter name
# ex. def increment(number, by=1):----> by is a key word argument with default value 1
#     return number + by
# print(increment(5))----> output 6
# defoult parameter value---> a value that is assigned to a parameter if no argument is passed for that parameter when the function is called
# ex. def increment(number, by=1):----> by is a key word argument with default value 1
#     return number + by
# print(increment(5))----> output 6
# """def multilpy(*numbers):
#  total =1
# for number in numbers:
#       total *= number
#   return total
# print(( multilpy(2,3,4)))"""
# *args---> a special syntax in function definitions to allow the function to accept a variable number of positional arguments
# **args---> a special syntax in function definitions to allow the function to accept a variable number of keyword arguments
# tuple---> a collection which is ordered and unchangeable, allows duplicate members, defined by parentheses () [iterable]
# @dictionary---> a collection which is unordered, changeable and indexed, no duplicate members, defined by curly braces {} [key:value pairs]
# escope global vs local variable


student = "aza"
age = 19
height = 165.5
is_student = True
print(student)
print(len(student))
print(student[0:1])
print(
    f"student name is {student}, age is {age}, height is {height}, is student: {is_student}")
print(
    f"student name is {student}, age is {age}, height is {height}, is student: {is_student}.")
# x = input("x: ")
# y= int(x) +1
# print(y)
# x = input("x: ")
# y = int(x) **2
# print(y)
x = print(ord("A"))
y = ("ali" == "Aza")
print(y)
tempreture = 35
if tempreture > 30:
    print("It is hot today")
elif tempreture > 30:
    print("it is cool today")
else:
    print("it is cold today")
letters = ["a", "b", "c"]
while True:
    print(letters)
    break



          
