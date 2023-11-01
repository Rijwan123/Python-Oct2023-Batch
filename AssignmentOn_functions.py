"""# Even or odd number

def check_even_odd(num):
    if num%2==0:
        print(num, 'is even')
    else:
        print(num, 'is odd')
num= int(input('Enter the number: '))
check_even_odd(num)
#--------------------------------------------
# Pass or fail

def result(marks):
    if marks> 35:
        print('Pass')
    else:
        print('Fail')
marks= int(input('Enter the marks: '))
result(marks)

#---------------------------------------------
#Positive or negative

def pon(num2):
    if num2>0:
        print(num2,'is positive')
    else:
        print(num2, 'is Negative')

num2= int(input('Enter the num: '))
pon(num2)

-------------------------------------------------------

# Check Seasons
def check_seasons(month):
    if month == 'January' or month == 'February' or month == 'December' or month == 'November':
        print("It's Winter season")
    elif month == 'March' or month == 'April' or month == 'May' or month == 'June':
        print("It's Summer season")
    else:
        print("It's rainy season")

check_seasons('July')
-------------------------------------------------------------------------------------------

# Functions with Return
#1
def add(a, b):
    result= a+b
    return result

sum= add(3,4)
print(sum)

#2

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

factorial = fact(5)
print('Factorial is ', factorial)
#3
def cube(num3):
    return num3*num3*num3

res2= cube(3)
print(res2)
"""
#4Check Fiscal Quarters
def Fiscal_Quarter(month):
    if month == 'January' or month == 'February' or month == 'March' or month == 'April':
        return 'first_quarter'
    elif month == 'July' or month == 'August' or month == 'May' or month == 'June':
        return 'second_quarter'
    elif month == 'September' or month == 'Octomber' or month == 'November' or month == 'December':
        return 'third_quarter'
    else:
        return 'Invalid month'

month= str(input('Enter a month : '))
print(Fiscal_Quarter(month))

















