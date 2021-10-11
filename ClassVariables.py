class Employee:
    raise_amount = 1.04 # class variable
    num_of_emps = 0

    def __init__(self,first, last, pay):
        self.first = first # instance variables
        self.last = last
        self.pay = pay
        self.email = first + '.' + 'last' + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amt(cls, amount): #class method
       cls.raise_amount = amount
       

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

            

#Employee.raise_amount = 1.04

#print(Employee.num_of_emps)
emp_1 = Employee('Corey','Schafer',50000) 
emp_2 = Employee('Test','User',60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
#emp_1.raise_amount = 1.05



new_emp_1 = Employee.from_string(emp_str_1)

#print(Employee.num_of_emps)
print(new_emp_1.email)
print(new_emp_1.pay)
print(new_emp_1.first)
print(new_emp_1.last)

#print(Employee.raise_amount)
print(emp_1.raise_amount)
#print(emp_2.raise_amount)

