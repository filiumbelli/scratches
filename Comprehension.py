# words =["NOW","IS","THE","TIME"]
# print(words)
# words = [word.lower () for word in words]
# print(words)
# liste =[]
# for i in words:
#     liste += [i]
# print(liste)
# saygac=[1,2,5,6,7,8,9]
# print(liste)
# x=0
# sayiToplar=[x +i for i in saygac]
# for i in sayiToplar:
#     x += i
#
# print(x)
#
# print(sayiToplar)
# fileOpener = open("gradex.txt","w+")
# fileOpener.write("85\n73\n44\n")
# fileOpener.close()
# fileReader = open("gradex.txt","r")
# a=fileReader.readlines()
# print(a)
# x=[]
# for i in range(len(a)):
#     x+=[a[i].rstrip()]
# print(x)
#
# grades =[grade.rstrip() for grade in open("gradex.txt")]
# print(grades)
# N = range(1,101)
# EN = [x for x in N if x % 2 == 0]
# ON = [x for x in N if x % 2 == 1]
# print(EN, "\n" ,ON)
sent = "now is the time for all good people"
sent += " of their party"
words = sent.split(" ")
wlen =[(word,len(word)) for word in words]
print(wlen)