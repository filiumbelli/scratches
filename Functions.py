# def square(number):
#     return number * number
#
# def numVowels(string):
#     string = string.lower()
#     count = 0
#     for i in range(len(string)):
#         if string[i] == "a" or string[i] == "e" or \
#             string[i] == "i" or string[i] == "o" or \
#             string[i] == "u":
#             count += 1
#     return count
# num = int(input("Enter a number"))
# sqr = square(num)
# print(sqr)
# string = input("Bir string giriniz")
# star = numVowels(string)
# print(star)

def ftoc(temp):
    return (temp - 32.0) * (5 / 9)


def ctof(temp):
    return temp * (9.0 / 5.0) + 32.0


# def conver(temp, toScale):
#     if toScale.lower() == "c":
#         return ftoc(temp)
#     elif toScale.lower() == "f":
#         return ctof(temp)
#     else:
#         return ValueError
#
# print("Enter a temperature: ")
# temp = int(input())
# scale = input("If scale is Celcius insert c,otherwise you can input F")
# a=conver(temp,scale)
# print(a)
# def tax(value):
#     if value <240:
#         return 0
#     elif value >=240 and value <480:
#         return value*0.15
#     else:
#         return value*0.28
# def netPay(value):
#     return value-taxer
# print("Enter the amount of the value you earn")
# value=int(input())
# taxer= tax(value)
# print("the tax you need to pay is = " + str(taxer))
# netpay = netPay(value)
# print("the original money after taxes is = " +str(netpay))
# def fact(number):
#     product = 1
#     for i in range(1, number + 1):
#         product *= i
#     return product
#
# a=fact(5)
# print(a)
