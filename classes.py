class Employee:
    def __init__(self, name, last, email, pay):
        self.name = name
        self.last = last
        self.email = email
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.name, self.last) 


emp_1 = Employee('Sarah' , 'Smith', 'sarahsmith.com', 200000)
emp_2 =Employee('Jessica', 'Parker', 'jparker.com',12000) 

print(emp_1.__dict__)
print(emp_2.__dict__)