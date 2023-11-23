"""# Assignment: instance method :Solve 1-1 example with positional,keyword,default & Var. leng. args
#1. instance method : positional args
# EX.1
class positional_args:
    def __init__(self, account, number):
        print(account)
        print(number)

positional_args('ICICI', 2352345)

#EX.2

class Car:
    def __init__(self,brand):
        self.brand= brand

    def display_info(self, model, year):
        print('Brand: ', self.brand, 'Model:', model, 'Year:', year)

car = Car("Mercedes")
car.display_info('M2023', 2023)

#2. instance method : keyword args
#Ex.1

class school:
    def __init__(self, name= 'IIT', year='2023'):
        print('Name: ', name)
        print('Year: ', year)

school()

#Ex. 2
class Person:
    def __init__(self, name):
        self.name=name

    def great(self, time='Morning,', message='Hello'):
        print('Good',time, message,'!','I am ', self.name)

#Creating an instance of person

person= Person('Johnson')

# Calling the greet method with keyword arguments
person.great()

#3.  instance method : default args

class computer:
    def __init__(self, model, ram='8GB', memory='250GB'):
        print('Constructor called')
        print('Computer model is', model)
        print('Computer RAM is', ram)
        print('Computer Memory is', memory)

computer('AB2023')

  def dispay_info(self):
        print('Name:'self.name)
        print('Courses: ' self.courses)
        print('Grades :'self.grades)


"""

#4.  instance method : Var. leng. args


#1. variable length positional argument

"""class Student:
    def __init__(self,name,*courses):
        self.name =name
        self.courses = list(courses)
        print('Constructor called')
        print('name', self.name)
        print('courses: ',self.courses  )

Student('Bob','Maths','Science')"""

#2. Variable length keyword argument
class Teacher:
    def __init__(self,name,**lectures):
        self.name = name
        self.lectures = dict(lectures)
        print('Constructor called...')
        print('name', self.name)
        print('courses: ',self.lectures  )

Teacher('Bobby',Maths=3,Science=4)