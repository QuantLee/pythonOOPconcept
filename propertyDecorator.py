# property decorator, treat the member function as an attribute of the class
# setter(property decorator), setter, deleter


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'
        # here is a problem, cus once the first name changes: emp.first = othernames
        # email still remains the same, so we have to define a email method like fullName()

    @property
    def email(self):
        return self.first + '.' + self.last + '@email.com'

    @property
    def fullName(self):
        return self.first + ' ' + self.last

    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        self.first = ''
        self.last = ''
        print('Name Delete!')


emp = Employee('Dongxu', 'Li')
emp.last = 'Lee'
print(emp.first)
print(emp.fullName)
print(emp.email)
print()

emp.fullName = 'Mark Zackburg'
print(emp.first)
print(emp.fullName)
print(emp.email)
print()

del emp.fullName
print(emp.first)
print(emp.fullName)
print(emp.email)
