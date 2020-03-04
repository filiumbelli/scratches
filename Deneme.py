class Araba:
    vites = False
    yakit = ""
    garanti = 0
    def __init__(self):
       pass


class Audi(Araba):
    model= ""
    def __init__(self,model,vites,yakit,garanti):
        self.model=model
        self.vites=vites
        self.garanti=garanti
        self.yakit=yakit

    def printGaranti(self):
        strVites =""
        if self.vites:
            strVites="otomatik"
        else:
            strVites="manual"
        print(self.model + " " +self.yakit+ " " + strVites + " Audi arabanın garanti süresi "+str(self.garanti)+" yıldır.")


audi = Audi("94",True,"dizel",0)
audi.printGaranti()