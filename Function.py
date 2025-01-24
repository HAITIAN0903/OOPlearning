def hello_fun(greeting,name='You'):
    return '{},{}'.format(greeting, name)

#positional keyword arguments must come before keyword arguments
#args tuples, kwargs dictionaries

print(hello_fun('Hi'))


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

courses = ['Math','Art']
info = {'name':'John','age':22}

student_info(*courses,**info)

##for loop study
#
# For loops iterated through a certain number of values
nums = [1,2,3,4,5]

for num in nums:
    if num ==3:
        print('Found')
        break#end
    print(num)

for num in nums:
    if num ==3:
        print('Found')
        continue#skip to next iteration
    print(num)

for num in nums:
    for letters in 'abc':
        print(num,letters)

for i in range(1,10):
    print (i)

#While loop will just keep going unitl a certain condition is met or until we hit a break

x = 0
while x < 10:
    if x == 5:
        break # just break condition
    print(x)
    x+=1

#import modules and explore

import random,math,os

courses =['History','Math','Physics','Compsci']

rads = math.radians(90)

print(os.getcwd())


#sort list
li =[9,1,8,2,7,3,6,4,5]
s_li = sorted(li)# if I want to reverse, just add reverse=true after li
print('Sorted Variable:\t',s_li)

li.sort()
print('original variable:',li)

li2 = [-6,-5,-4,1,2,3]
s_li2 = sorted(li2,key=abs) #key argument, the function will sort it as the way u use in key element, 
print(s_li2)

#example: emp_1 = Employee();emp_2 = Employee() each of the these are going to 

# be their own unique instances of the employee class

emp_1 = Employee()
emp_2 = Employee()
print(emp_1)
print(emp_2)

emp_1.first = 'Haitian'
emp_1.last = 'Cai'
emp_1.email = 'Haitian0903@gmail.com'
emp_1.pay = 80000

#instance variable, we just dont want to do it back and forth because it will have mistakes

#our init method, takes the instance which we called self
class Employee:
    def __init__(self,first,last,pay): # u can think of initialize #self is istance argument,add more argument u want except self
        self.first = first
        self.last = last
        self.pay = pay
        self.email =first + '.' + last + '@gmail.com'
    def fullname(self): #each method within a class automatically takes the instance as the first argument
        return '{} {}'.format(self.first,self.last)


emp_1 = Employee('Haitian','Cai',100000)
emp_2 = Employee('Rabbit','Zhao',200000)

print(emp_1.fullname())# this is a method instead of the argument, thats the reason why we need to use the parentheses

# We can write print('{} {}'.format(emp_1.first, emp_1.last)) but you dont want to do it every time, 
# back and forth, so we can added it into our class function

#What if we dont add self in fullname() method, it will automatically pass the argument, so we have to make sure self is in.

emp_1.fullname() # no need to pass in self, because it already know
print(Employee.fullname(emp_1)) # When we call a method in a class, it doesnt know what instance we want to run, so we need to add
