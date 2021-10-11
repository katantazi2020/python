class Employee:
    def __init__(self, first, last, pay):
        self.first = first  # instance variables
        self.last = last
        self.pay = pay
        self.email =first +'.' + 'last' + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    
emp_1 = Employee('Corey','Schafer',50000) 
emp_2 = Employee('Test','User',60000)


#print(emp_1.fullname()) Anotther way  to print values
emp_1.fullname()
print(Employee.fullname(emp_1))

