class Yemek:

    def pisirme(self, yemekturu):

        print(yemekturu + " pişirildi.")

class Pizza(Yemek):
    adi = ""
    def __init__(self,adi):
        self.adi=adi

    def pişir(self):
        self.pisirme(self.adi)

class Lahmacun(Yemek):
    adi = ""
    def __init__(self,adi):
        self.adi =adi
    def pişir(self):
        self.pisirme(self.adi)

lahm = Lahmacun("Lahmacun")
pizza = Pizza("pizza")
lahm.pişir()

pizza.pişir()
pizza.pisirme(pizza.adi)
print(pizza.adi)
print(lahm.adi)


