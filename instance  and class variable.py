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
    raise_amount = 1.04 # class variable. When we access class variable, We need to either access through the class itself or an instance of a class
    num_of_emps = 0 
    def __init__(self,first,last,pay): # u can think of initialize #self is istance argument,add more argument u want except self
        self.first = first
        self.last = last
        self.pay = pay
        self.email =first + '.' + last + '@gmail.com'
        Employee.num_of_emps += 1 # us number of employees here instead of self.num_of_emps// reason: becasue its nice to have constant class value that can be overwritten per instance
    def fullname(self): #each method within a class automatically takes the instance as the first argument
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.ra


emp_1 = Employee('Haitian','Cai',100000)
emp_2 = Employee('Rabbit','Zhao',200000)

print(emp_1.fullname())# this is a method instead of the argument, thats the reason why we need to use the parentheses

# We can write print('{} {}'.format(emp_1.first, emp_1.last)) but you dont want to do it every time, 
# back and forth, so we can added it into our class function

#What if we dont add self in fullname() method, it will automatically pass the argument, so we have to make sure self is in.

emp_1.fullname() # no need to pass in self, because it already know
print(Employee.fullname(emp_1)) # When we call a method in a class, it doesnt know what instance we want to run, so we need to add

print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)
print(Employee.num_of_emps)