#Python Function
''' Function is a block of code which only runs when it is called. You can pass data, known as
parameter, into a function. A function can return data as a result.
Syntax:
def fnction_name():
    statement(s) to be executed
'''
def print_statement():
    print("Hello world")
    print("Good Morning")

print_statement()

print(len("Hello Abhinav"))
print(sum({1,2,3,4}))

def sum(num1, num2):
    result=num1+num2
    print("The sum of two number is", result)
sum(10,20)

def sum(x,y):
    result=x+y
    return result
print(sum(25,25))

def sum():
    number1=int(input("Enter your number1 :"))
    number2=int(input("Enter your number2 :"))
    result=number1+number2
    print("The sum of two number is :", result)
sum()

def check_even_odd():
    number=int(input("Enter your number :"))
    if number%2==0:
        print("The number is even")
    else:
        print("The number is odd")
check_even_odd()
check_even_odd()      
