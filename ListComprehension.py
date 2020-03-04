grades = [25,55,66,73]

class KucuktenBuyuge():
    list =[]
    def __init__(self):
        pass

class BuyukBulucu(KucuktenBuyuge):

    def __init__(self,list):
        self.list = list


    def bigFinder(self):
        x= 0
        for i in range(0,len(self.list)):
            if self.list[i] >= self.list[x]:
                x = i
                newMax = self.list[x]
        print(newMax)


 class CanEgrisi():
     grade= 0
     def canEgrisi(self,grade,grades):
         self.grade=grade
         for grade in grades:
             grade = 100-grade
             newList= [grades+grade]
         print(newList)
a = BuyukBulucu(grades)
a.bigFinder()


