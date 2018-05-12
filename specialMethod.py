# magic and dunder method


class Employee:

    raiseRate = 0.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(self.pay * (1 + self.raiseRate))

    def __repr__(self):
        '''
            usually the string it returns enables user to recreate the object.
            normally this is used by developer.
        '''
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        '''
            usually, this special method is used by end user
        '''
        return self.fullName() + ' --> ' + self.email

    def __add__(self, other):
        # this is kind like the operation overload, if you will.
        # return the sum of two salary
        return self.pay + other.pay

    def __len__(self):
        # return the length of the fullname
        return len(self.fullName())


emp1 = Employee('Dongxu', 'Li', 60000)
emp2 = Employee('Mark', 'Zakberg', 50000)

print(str(emp1))
print(repr(emp1))
print()
# these are identical
print(emp1.__str__())
print(emp1.__repr__())
print()
# more special method, int is also an object
print(1 + 2)
print(int.__add__(1, 2))
print()

print('a' + 'b')
print(str.__add__('a', 'b'))
print()

print(emp1 + emp2)
print()

print(len('leodongxu'))
print('leodongxu'.__len__())
print()

print(len(emp1))
print()
