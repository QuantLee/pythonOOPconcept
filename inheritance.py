# Inheritance, syntax, super().__init__(first, last, pay)
class Employee:

    raiseRate = 0.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(self.pay * (1 + self.raiseRate))


class Developer(Employee):

    raiseRate = 0.1

    def __init__(self, first, last, pay, progLang):
        super().__init__(first, last, pay)
        self.progLang = progLang


class Manager(Employee):

    raiseRate = 0.2

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def removeEmp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printEmp(self):
        for emp in self.employees:
            print('--->', emp.fullName())


# test functions
dev1 = Developer('Mark', 'Zackberg', 10000, 'Java')
dev2 = Developer('Will', 'Simon', 20000, 'C++')
emp1 = Employee('Dongxu', 'Li', 60000)

print(dev1.email)
print(emp1.fullName())

manager = Manager('James', 'Simon', 10000, [dev1, dev2, emp1])
manager.printEmp()
