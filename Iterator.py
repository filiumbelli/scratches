import os
#numbers = [1,2,3,4,5]
#x= iter(numbers)
#for i in range(0,len(numbers)):
#    print(next(x))

#fileRead = open("ForLoops.txt")
#for i in open("ForLoops.txt"):
#    print(next(fileRead))



# grades = {"ali":45,"veli":14,"kemal":85}
# for key in grades.keys():
#     print(key+":"+str(grades[key]))
#
# it=iter(grades.keys())
# it2=iter(grades.values())
# for i in range(0,len(grades.keys())):
#     print(next(it)+":"+str(next(it2)))

# files = os.popen('dir *.py')
# fileit = iter(files)
# for file in files:
#     print(file , end = " ")
square = ( (10,5),(5,25),(6,29),(12,10))
for points in square:
    print(points)
sqit = iter(square)
for i in  range(0,len(square)):
    print(next(sqit))