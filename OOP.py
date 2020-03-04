# class Name:
#     #construction method - instantiation
#     def __init__(self,first,middle,last):
#         self.first = first
#         self.middle = middle
#         self.last = last
#     def __str__(self):
#         return self.first + " " + self.middle + " " + self.last
#
#     def LastFirst(self):
#         return self.last+" " +self.first
#
#     def initials(self):
#         return self.first[0] +" "+self.middle[0]+" "+self.last[0]
# aName = Name("MARY","LIZ","SMITH")
# yourName = Name("ali","veli","kemal")
#
# print(aName)
# print(aName.LastFirst())
# print(yourName.initials())
#
# class Student:
#     #fields - name ,  id , grades(list)
#     grades=[]
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#     def addGrade(self,grade):
#         self.grades.append(grade)
#
#     def showGrades(self):
#         grds = " "
#         for grade in self.grades:
#             grds += str(grade) +" "
#         return grds
#     def averageNotes(self):
#         grds=0
#         count=0
#         for grade in self.grades:
#             grds += grade
#             count +=1
#         return str(grds/count)
#
# james= Student("James","15290263")
# james.addGrade(55)
# james.addGrade(98)
# james.addGrade(75)
# JamesNotes=james.showGrades()
# print(JamesNotes)
# JamesAverage= james.averageNotes()
# print(JamesAverage)

# class Workers:
#     def __init__(self, name, surname, age, title):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.title = title
#
#     def __str__(self):
#         return self.name + " " + self.surname + " " + str(self.age)+ " " + self.title
#
#     def changeWorkers(self, name, surname,age,title):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.title = title
#
#     def registerNew(self,name, surname,age,title):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.title = title
#         fileOpen = open("Workers.txt","a")
#         fileOpen.write("{}, {}, {}, {} \n".format(self.name,self.surname,self.age,self.title))
#         fileOpen.close()
#
#
# x = Workers("ahmet","can",14,"kalem")
# x.registerNew("ali","can",14,"öğrenci")
# x.changeWorkers("Ali","kaan",16,"öğrenci")
# print

class Employee:
    def __init__(self, name, title, age,payRate,hoursWorked):
        self.name = name
        self.title = title
        self.age = age
        self.payRate = payRate
        self.hoursWorked= hoursWorked

    def __str__(self):
        return self.name + ", " + self.title + ", " + str(self.age)+", "+str(self.payRate*self.hoursWorked)



# class Manager(Employee):
#     def __init__(self, name, title, age, Salary):
#         Employee.__init__(self, name, title, age)
#         self.Salary = Salary
#
#     def __str__(self):
#         retStr = Employee.__str__(self)
#         retStr += " Salaried: " + str(self.Salary)
#         return retStr

class File:
    def __init__(self,filename,textfile):
        self.filename=filename
        self.textfile=textfile

    def fileWriteOnIt(self):
        fileOpener = open("{}".format(self.filename),"w+")
        fileOpener.write(self.textfile)
        fileOpener.close()
    def fileAddName(self):
        fileOpener = open("{}".format(self.filename),"a")
        fileOpener.write(self.textfile)
        fileOpener.close()


x=1
while x == True:
    x=int(input("1 to add a registration of an Employee, 0 for closing program: "))
    if x==0:
       break
    else:
        inf1 = input("Name of the employee: ")
        inf2 = input("Title of the employee: ")
        inf3 = int(input("Age of the employee: "))
        inf4=int(input("Hours payed for employee: "))
        inf5 = int(input("Hours employee has worked: "))

        e1 =Employee(inf1,inf2,inf3,inf4,inf5)

        fils = File("amer.txt","Name: {} ,Title: {} ,Age: {} ,Payment Rate: {} ,Work Hours: {} \n".format(inf1,inf2,inf3,inf4,inf5))
        fils.fileAddName()



