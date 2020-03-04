class Person:
    name = ''
    surname = ''

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def getWholeName(self):
        return self.name + " " + self.surname


class Employee(Person):

    def printName(self):
        print(person.name)

person = Employee("ali", "kağan")

person.printName()