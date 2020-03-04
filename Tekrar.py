class Analyzer:
    name = ""
    surname = ""
    age = ""
    title = ""

    def __init__(self):
        pass


class CalisanAdi(Analyzer):
    print("calisanin adini yazınız: ")
    def __init__(self,name,surname,age,title):
        self.name = name
        self.surname = surname
        self.age = age
        self.title = title

    def fileOpener(self):
        fileWriter= open("Calisanlar.txt","a")
        fileWriter.write(self.name + " " + self.surname + " " + self.age + " " + self.title + "\n")
        fileWriter.close()
Log = CalisanAdi("Kalan","yörü","101","yatır").fileOpener()
print(CalisanAdi.name,CalisanAdi.surname)

