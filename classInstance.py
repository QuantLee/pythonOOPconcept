# python object programming, regular method, static method and class method


class Employee:

    numOfEmployee = 0
    raiseRate = 0.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
        Employee.numOfEmployee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def printInfo(self):
        print("{}'s email address is: {}, and {}'s pay is: {}.".format(self.fullname(), self.email,
                                                                       self.fullname(), self.pay))

    def applyRaise(self):
        # In order to get access to the raiseRate, get it through instance or classes, if the
        # instance do not have the attribute, it would try to find the attribute from the class
        # which it inheritate from. self.raiseRate could be changed to Employee.raiseRate. But if
        # you assign a value to the instance, example: instance.raiseRate = 1.05, then raiseRate for
        # this instance will refer to this value instead of searching for the class.
        self.pay = int(self.pay * (1 + self.raiseRate))

    # Regular methods, static methods and class methods difference, regular methods automatically
    # take in self as the input parameter. Here we can see the difference between classmethods and
    # staticmethods.
    @classmethod
    def setRaiseRate(cls, rate):
        # So for class method, the first input of the member function is the class instead of self.
        cls.raiseRate = rate

    @classmethod
    def printNumEmployee(cls):
        print(cls.numOfEmployee)

    @classmethod
    def fromStr(cls, string):
        # This is a very important usage of the classmethod, to use it as an alternative constructor
        first, last, pay = string.split('-')
        # Here we have to return an instance, to pass into an object container
        return cls(first, last, pay)

    # For static method, there is no automatic input, it's like the regular function, we include
    # them inside the class because it has some logic connection with the class.
    @staticmethod
    def isWorkDay(day):
        # In python, .weekday return a number, where [0, 1, 2, 3, 4, 5, 6] indicate Monday to Sunday
        if day.weekday() not in [5, 6]:
            return True
        return False


# test class implementation
import datetime
myDate = datetime.date(2016, 7, 11)
print(Employee.isWorkDay(myDate))

# construct instances

e1 = Employee.fromStr('Jack-Douson-7000')
e2 = Employee.fromStr('Emily-Woodly-6000')
e3 = Employee.fromStr('Will-Simon-10000')

e1.printInfo()
e2.printInfo()
e3.printInfo()

print(Employee.numOfEmployee)
print()
print(Employee.raiseRate)
Employee.setRaiseRate(0.05)
print(Employee.raiseRate)
