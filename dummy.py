# # print(10==10)
# # print(10<9)
# # print(10==100)

# # x='200'
# # print(isinstance(x,int))

# # import operator
# # print(operator.add(15, 5))
# # print(operator.sub(15, 5))
# # print(operator.mul(15, 5))
# # print(operator.pow(15, 5))
# # print(operator.truediv(15, 5))
# # print(operator.truediv(15, 5))
# # print(operator.floordiv(20, 3))
# # print(operator.mod(15, 5))


# x = 5
# x += 5
# print(x)

# import operator
# x=operator.iadd(5,5)

# x=5
# x-=2
# print(x)

# x=operator.isub(5,2)

# x=5
# y=6
# print(x > 1 and y< 10 )

# x = 5
# y = 6
# if x > 6 or y < 10:
#  print ('hello')   



# User se input lena



# a = int(input("Pehla number daaliye: "))
# b = int(input("Dusra number daaliye: "))
# print(a+b)


# a = int(input("Pehla number: "))
# b = int(input("Dusra number: "))

# if a > 0 and b > 0:
#     print("Dono number positive hain.")
# else:
#     print("Koi ek ya dono number negative hain.")




#for two inputs
#input functions used using AND condition

# a = int(input("Pehla number: "))
# b = int(input("Dusra number: "))
# c = int(input("Teesra number: "))

# if a >= b and a >= c:
#     print("Badi sankhya hai:", a)
# elif b >= a and b >= c:
#     print("Badi sankhya hai:", b)
# else:
#     print("Badi sankhya hai:", c)


# x=10
# print(id(x))
# y=44
# print(id(y))


# variable id
# x = "abhishek"
# print(id(x))
# y = "mayank"
# print(id(y))
# print(x is not y)  




# List of numbers
# nums = [1, 2, 3, 4, 5]

# print(1 in nums)   
# print(10 in nums) 
# 
# print('str' in 'string')    
# print('cli' in 'string') 
# print('ng' in 'string') 


# print(6 & 3)


# Homework-
# question1
# homework = "PythonProgramming"
# homework = homework[2:6]
# print(homework)  

# question 2 # reversing the string data science = ecneics atad
# homework= "DataScience"
# reversed_homework = homework[::-1]
# print(reversed_homework) 

#question 3- skipping character-extract every third element starting from index 0.
# list[start : end : skip]
# start=0
# end= nothing
# skip=3


# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list[0::3])    

# question no 4- negative indexing
# negative_indexing = "HelloWorld"
# negative_indexing = negative_indexing[-5:]
# print(negative_indexing)




# question no 5- middle number

# Middle_number = [10, 20, 30, 40, 50, 60, 70]
# print(Middle_number[2:5])


# fruits= ["apple", "banana", "strawberry"]
# print(fruits)


# fruits= ["apple", "banana", "strawberry"]
# print(fruits[1])

# fruits= ["apple", "banana", "strawberry"]
# print(fruits[-1])


# fruits= ["apple", "banana", "strawberry","kiwi"]
# # print(fruits[:])


# name = "abhishek"
# print(name[::2])

#TOPIC list data type
# Fruits = ['apple', 'banana', 'orange']
# Fruits[1:2] = ['kiwi']
# print(Fruits)



# fruits=["apple","mango","banana","strawberry"]
# fav_fruits=fruits.copy()
# print(fav_fruits)


#insert function

# fruits=["apple","banana","cherry"]
# fruits.insert(1,"orange")
# print(fruits)

#append function

# fruits=['apple','banana', 'cherry']
# fruits.append("orange")
# print(fruits)

# #extend function

# fruits1=['apple','banana', 'cherry']
# fruits2=['mango','pineapple','papaya']
# fruits1.extend(fruits2)
# print(fruits1)


#remove fucntion


# fruits=['apple','banana', 'cherry']
# fruits.remove('banana')
# print(fruits)


#pop function

# fruits=['apple','banana', 'cherry']
# fruits.pop(1)
# print(fruits)

#del function with index given 1

# fruits=['apple','banana', 'cherry']
# del fruits[1]
# print(fruits)

# fruits=['apple','banana', 'cherry']
# del fruits


#clear function

# fruits=['apple','banana', 'cherry']
# fruits.clear()
# print(fruits)

# Fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
# print(Fruits[2:])

# 2 se chalu ki hai and : se khtm ki hai


# x=("apple","banana","cherry")
# y=list(x)
# print
# y[1]="watermelon"
# x=tuple(y)
# print(x)


# data types sets


# Fruits = {"apple", "banana", "cherry"}
# for x in Fruits:
#     print(x)

# print("banana" in Fruits)

# add fucntions

# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")
# print(fruits)


# fruits = {"apple", "banana", "cherry"}
# mylist1=["kiwi","orange"]
# fruits.update(mylist1)
# print(fruits)


# Removing item in aset using remove and discard

# fruits = {"apple", "banana", "cherry"}
# fruits.remove("apple")
# print(fruits)


# fruits = {"apple", "banana", "cherry"}
# fruits.discard("apple")
# print(fruits)


#pop()

# fruits = {"apple", "banana", "cherry"}
# fruits.clear()
# print(fruits)

# fruits = {"apple", "banana", "cherry"}
# del fruits
# print(fruits)

# fruits = {"apple", "banana", "cherry"}
# x=fruits.pop()
# print(x)
# print(fruits)

#Union function ()

# set1={"a","b","c"}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3)

# update function

# set1={"a","b","c"}
# set2={1,2,3}
# set1.update(set2)
# print(set1)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)
# print(x)



# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.intersection(y)
# print(z)


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.symmetric_difference_update(y)
# print(x)



# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.symmetric_difference(y)
# print(z)


# set1 = {"apple", 1, "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1.intersection(set2)
# print(set3)




# Frozen set



# nu = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # tuple of numbers

# fnum = frozenset(nu)             # converting tuple to frozenset

# # print("frozenset Object is :", fnum)

# print("Type of fnum is :", type(fnum))


# Dictionary data set

# Brand is key and bmw is values
#cars is the varibale
# It is  just type of JSON DATA TYPE
# cars={
#     "brand":"BMW",
#     "model":"2nd series",
#     "year":2004
# }
# print(cars)


# duplicates

# cars={
#     "brand":"BMW",
#     "model":"1nd series",
#     "model":"2nd series",
#     "year":2004
# }
# print(cars)



# cars = {
#     "brand": "BMW",
#     "model1": "2nd series",
#     "model2": "2nd series",
#     "year": 2004
# }
# print(cars)




# dictionary items are ordered

# in order to access the element use get


# x=cars.get("model")
# print(x)


# car={

#     "brand":"ford",
#     "model":"Mustang",
#     "year":1964

# }



# x=car.values()
# print(x)
# car["year"]=2020
# print(x)



# car={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }

# x=car.values()
# print(x) #befor the change
# car["colour"]="red"
# print(x)

# x=car.items()
# print(x)






# car={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }

# car["year"]=2020
# print(cars)


# cars={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }

# cars.update({"year":2022})


# cars = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# cars.pop("year") 
# print(cars)




# cars = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# cars.clear()  
# print(cars)

#copy fucntion used in dic data type

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# mydict = thisdict.copy()
# print(mydict)




# friends={

#     "child1":{
#     "name":"arun",
#     "year":2000
#     },

#     "child2":{
#         "name":"vignesh",
#         "year":2001
#     },
#         "child3":{
#             "name":"arya",
#             "year":2018
#         }

#     }

# print(friends)



# User se input lena



# Instead of taking input
# a = 1
# b = 20

# if a < b:
#     print("b is greater")
# elif a == b:
#     print("a and b both are equal")


    # Taking user input and converting to integers
# a = int(input("Enter the value of a: "))  
# b = int(input("Enter the value of b: "))   

# Comparison logic
# if a < b:
#     print("b is greater")
# elif a > b:
#     print("a is greater than b")

# else:
#     print("print any number")


# a=2
# b=400
# print(("A")if a>b else print("B"))




# a = 10
# b = 20
# c = 30

# if a > b and a > c:
#     print("a bada hai")
# elif b > a and b > c:
#     print("b bada hai")
# else:
#     print("c bada hai")


#replacing the words in the string
# abhishek="hello world"
# anand=abhishek.replace("l","o")
# print(anand)

# question- i need to change the 1st L


# text="hello world"
# new_text=text[3]
# print(new_text)


#chaning words in strings

# text = "banana"
# index = 1
# new_char = "o"

# formula below

# new_text = text[:index] + new_char + text[index + 1:]
# print(new_text)



#nested 

# both conditions are true

# x = 41

# if x > 10:
#     print("Above ten,")
#     if x > 20:
#         print("and also above 20!")
#     else:
#         print("but not above 20.")


# one condition will be true and one will be false

# x = 15

# if x > 10:
#     print("Above ten,")
#     if x < 20:
#         print("and also above 20!")
#     else:
#         print("but not above 20.")



# PASS statement

# a = 79
# b = 70

# if a > b:
#     pass



# while statement

# L=0
# while L<4:
#     L+=1
#     print(L)



# Step 1: Brand list
# brands = ["Adidas", "Reebok"]

# # Step 2: Show list to user
# print("Available brands:", brands)

# # Step 3: User se brand choose karna
# selected_brand = input("Choose a brand from the list: ")

# # Step 4: If-else logic
# if selected_brand == "Adidas":
#     print("This brand is good")
# elif selected_brand == "Reebok":
#     print("This brand is very good")
# else:
#     print("Brand not recognized")

#i meaning is name of the variable name for example abhishek or you can write i

# s="ipcs global"
#implementing for loop
#meaning of for loop is usage is toh get the data- meaning without range

# for i in s:


    # s bhi variable hai and i bhi varibale hai and for loop

    # before for loop we add variable 
    # print(i)

# for loop i pehle jaake print karega i ko fir p ko print karega fir c ko print karega and s ko print karega

#print 1 to 10- use range i in range esa likjna hai

# for i in range(1, 11,2):
#     print(i)


# using slicing concept using for loop



# for i in range(11):
#     print("Hello World")


#using range

# for i in range(1, 12):
#     print(i, "Hello World")



# Old style using %s %d
# print("\nDictionary Iteration")

# d = dict()
# d['xyz'] = 123
# d['abc'] = 345

# for i in d:
#     print("%s %d" % (i, d[i]))



# for x in 'python developer':
#     if x == 'e' or x == 'o':
#         continue
#     print('Current Letter:', x)

#range function
# for i in range (1,22):
#  print(i)


# show range() basics
# printing a number

# output horizantal ho gya
# for i in range(10):
#     print(i, end=" ")
# print()




# l = [10, 20, 30]
# for i in range(len(l)):
#     print(l[i], end=" ")


    #end ="" ese karke likhunga toh bhi horizontally hi print karega


# simple project using if else conditions, taking user input


# #taking input from user
# state=input(" state ka naam dijiye   ?       "   )

# #using equal operator ie state==MP

# if state=="madhya pradesh":
#     print("MOHAN YADAV")

# elif state=="UTTAR PRADESH":
#     print("ADITYANATH YOGI")
    
# elif state=="Delhi":
#     print("EX CM ARVIND KEJIRWAL")

# elif state=="punjab":
#      print("BHAGWANT MANN")

# else:
#     print("mjhe nhi pta state ka cm kaun hai")  




# if insert_number=="1":
#  print("result:", a+b)

# elif insert_number=="2":
#  print("result:", a-b)

# elif insert_number=="3":
#  print("result:", a*b)

# elif insert_number=="4":
#  print("result:", a/b)

# else:
#  print("wrong number")



# functions


# def hello():
#      print("Hello")

#      writing without paramater

#      calling functions with the name of the fucntions

# def hello():         # Define a function named 'hello'
#     print("hello")   # It prints the word 'hello'

# hello()              # You are calling (using) the function



# A simple Python function to check
# whether x is even or odd

# def evenOrOdd(x):
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")

# # Driver code to call the function
# evenOrOdd(7)
# evenOrOdd(7)



# Python program to demonstrate default arguments

# def myFun(x, y=50):
#     print("x:", x)
#     print("y:", y)

# # Driver code (function ko sirf ek argument ke saath call kiya gaya hai)
# myFun(5)


# def student(firstname, lastname):
#     print(firstname, lastname)

# # pehli baar call 
# student(firstname='python', lastname='functions')

# # 2nd time call
# student(firstname='data', lastname='science')

# # 3rd time call
# student(firstname='hello', lastname='world')



# using double star **



# def myfunction(*argv):
  
#         print(*argv)

# myfunction('Hello','welcome','welcome','to','ipcs')        

# what is arguments


# def introduce(name, age, city):
#     print(f"My name is {name}, I am {age} years old, and I live in {city}.")

# introduce("Abhishek", 25, "Lucknow")


# single arguments *  


# def my_function(*kids):
#     print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")



# using for 

# def myfunction(*argv):
#     for x in argv:
#         print(x)

# myfunction('Hello', 'Welcome', 'to', 'ipcs')


# double arguments double **
# it works on keys and values

# def my_function(**student):
#     print("His first name is " + student["fname"])

# my_function(fname="vignesh", lname="$")



# my fucntions call kuya toh uske andar ka run hoga




# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))

# myFun(first='welcome', mid='for', last='course')


# default parameter

# my fucntion() jismai keys and value nhi hai usmai norway aagya hai
# def my_function(country = "Norway"):
#     print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")



# def my_function(xyz):
#     for x in xyz:
#         print(x)

# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)



# return value

# #without return
# def man(n):
#     print(n)

# man(2)

# now using return where print is written write return

#functions without using return value 

# def check_even_odd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# def check_even_odd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# # Function call
# print(check_even_odd(17))   # Output: Odd
# print(check_even_odd(10))  # Output: Even




# using return Value


# def check_even_odd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# # Function call with return value stored
# result1 = check_even_odd(7)
# result2 = check_even_odd(12)

# # Print kr diya returned values kol
# print("7 is", result1)
# print("12 is", result2)




# now taking user input





# def check_even_odd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# num1= int(input("enter the first number: "))
# num2= int(input("enter the second number: "))

# result1= check_even_odd(num1)
# result2= check_even_odd(num2)
    

# print(num1, "is", result1)   
# print(num2, "is", result2 )




# creating a factorial function

# def fact(n):
#     f=1
#     for i in range(1, n+1):
#         f=f*i
#     return f   


# # user se input

# num = int (input("enter the number: "))
# print("factorial is:", fact (num))



# function once created and then can be call again and again you dont have to write code again and again


# using def function to define 2 table 3 table etc


# def table(n):

#     for i in range(1,11):
#         print(n, "x", i, "=", n*i)


# # first number

# a= int(input("enter the first number: "))
# table(a)

# # second number

# b= int(input("enter the second number: "))
# table(b)


# update kr diya 30 ko
# def myfunction(x):
#     x[0] = 30   # list ke first element ko 30 bana diya

# # Driver Code
# lst = [9, 11, 13, 14, 15]
# myfunction(lst)
# print(lst)



# nested function


# def f1():
#     s = 'I love python'   # outer function ka variable
#     def f2():
#         print(s)          # inner function outer function ka variable use kar raha hai
#     f2()  # inner function ko yahin call kiya gaya hai

# # Driver code
# f1()




# lamda fucntion


# x = "hello python"

# # lambda function gets passed to print
# (lambda x: print(x))(x)


# def student_details(name, age, course):
#     print("Name:", name)
#     print("Age:", age)
#     print("Course:", course)

# # Function call with 3 arguments
# student_details("Abhishek", 22, "Python")





# # Normal function
# def cube(y):
#     return y * y * y






# # Lambda function
# g = lambda x: x * x * x

# print(g(7))      # Using lambda → 343
# print(cube(5))   # Using normal function → 125






# def power(n):
#     return lambda a : a ** n

# Create two separate base objects
# base_square = power(2)  # For squaring
# base_fifth = power(5)   # For fifth power

# print("Square operations:")
# print("5 squared =", base_square(5))  # 25
# print("7 squared =", base_square(7))  # 49

# print("\nFifth power operations:")
# print("2^5 =", base_fifth(2))  # 32
# print("3^5 =", base_fifth(3))  # 243






# # Original list of numbers
# a = [100.7, 8, 60, 5, 4, 3, 31, 10, 11]

# # 1. Using filter() with lambda to get even numbers
# filtered_result = filter(lambda x: x % 2 == 0, a)
# print("Filtered even numbers:", list(filtered_result))

# # 2. Using map() with lambda to check even/odd
# mapped_result = map(lambda x: x % 2 == 0, a)
# print("Even check results:", list(mapped_result))

# # 3. Additional example: Using map() to square all numbers
# squared_numbers = map(lambda x: x**2, a)
# print





# with global variable included


# x = "aw"  # Global variable defined outside the function

# def mufun():
#     print(x)  # Accesses the global variable 'x'

# mufun()  # Calls the function which prints the global 'x'
    








# without global

# output mai error

# def mun():
#     x = "python"  # This 'x' is LOCAL (not global)
# mun ()
# print(x)  




# def mun():
#     x = "python"  # Local variable
#     return x  # Return the value

# x = mun()  # Store returned value in global x
# print(x)  # Output: python




# a = 1

# def f():
#     print('Inside f() :', a)

# def g():
#     a = 2
#     print('Inside g() :', a)

# def h():
#     global a
#     a = 3
#     print('Inside h() :', a)

# print('global :', a)
# f()
# print('global :', a)
# g()
# print('global :', a)
# h()
# print('global :', a)




# def shout(text):
#     return text.upper()

# def whisper(text):
#     return text.lower()

# def greet(func):
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     print(greeting)

# greet(shout)
# greet(whisper)



# def create_adder(x):
#     def adder(y):
#         return x + y
#     return adder

# add_15 = create_adder(15)
# print(add_15(10))



# def prepare_dish(base_flavor, ingredient_count):
#     final_flavor = base_flavor + (ingredient_count * 2)
#     return "final flavor: " + str(final_flavor)

# print(prepare_dish(5, 4))





# def calc_factorial(x):
    
#     if x == 0:
#         return 2.86
#     else:
#         return x * calc_factorial(x - 1)

# num = 4
# print("The factorial of", num, "is", calc_factorial(num))


# def factorial(n):
#     if n==1:
#         return 1
#     return n * factorial(n-1)



# inbuilt module



# import platform
# x = platform.system()
# print(x)
# x = dir(platform)
# print(x)

# import datetime
# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))



#file handling

# # Open the file in read mode
file = open('python.txt', 'r')


for line in file:
     print(line)

# # Close the file after reading
file.close()




































































































