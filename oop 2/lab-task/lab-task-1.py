#python basics excercies

#print("hello world!!")

#Data types in python
# intiger = 10 #intiger
# float_type = 20.20 #float
# complexType = 20j #complex
# string = "String" #string
# boolean = True #boolean (True or False)
#print(intiger," is ",type(intiger),float_type," is ",type(float_type),complexType," ",string," is ", type(string))

#python input output operation

#string input
# stringInput = input("What's your name?: ")
# print("Hey ",stringInput)
# #intiger input
# value1 = int(input("Enter value 1: "))
# value2 = int(input("Enter value 2: "))
# #adding these two value and printing the sum
# total = value1+value2
# print(total)


# #Arithmatics Operations
# num1  = 10
# num2 = 5
# #addition (+)
# add = num1+num2
# #substraction(-)
# sub = num1-num2
# #multiplication(*)
# mul = num1*num2
# #division(/)
# div = num1/num2
# #mod
# mod = num1%num2
# #power
# power = num1 ** num2
# #printing these value
# print(add,sub,mul,div,mod,power)

#logical Operators
# condition1 = True
# condition2 = False
# #Logical AND operator(&&)
# print(condition2 and condition1)
# #Logical OR 
# print(condition1 or condition2)
# #Logical NOT
# print(not condition2)

#Bitwise Operations

# a = 4
# b = 4

# #bitwise AND
# print(a & b)
# #bitwise OR
# print(a | b)
# #bitwise NOT
# print(~a)
# #bitwise XOR
# print(a ^ b)
# #Bitwise Left Shift
# print(a << b)
# #Bitwise right shift
# print(a>>b)

#Assignment operations
# a = 10 
# b  = a
# print(b)
# b += a
# print(b)
# b -= a
# print(b)
# b *= a
# print(b)
# b /= a
# print(b)
# b %= 2
# # print(b)
# # b >>= a
# print(b)

#pythons conditionals 

#if,if-else,else,ladder

# a = 10
# b = 10
# if(a == b): #is equal
#     print("a and b is equl")
# else:
#     print("a and b is not equal!!")

#ladder
# one = 10
# two = 5
# if(one>two):
#     print(one," is greater than ",two)
# elif(one == two):
#     print("Both are equal")
# else:
#     print(two," is greater than ",one)

#Basic looping in python

#for loop using range
# for i in range(2,100,2):#range(start,end,increment)
#     if(i == 10):
#         break
#     print(i)

#python while loop
# i = 0
# while(i <= 10):
#     print(i)
#     i+=1

#Basics Function in python

def sum(a,b):
    return a+b
result = sum(10,20)
print(result)

