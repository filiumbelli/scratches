# def fact(number):
#     if number <=1:
#         return 1
#     else:
#         return number*fact(number-1)
#
# def explode(word):
#     if len(word) <= 1:
#         return word
#     else:
#         return word[0] + " " + explode(word[1:])
# a = explode("ahmedinecat")
# print(a)
# newWord="aaabbbccdeffffgg"
# def removeDups(newWord):
#     if len(newWord) <= 1:
#         return newWord
#     elif newWord[0] == newWord[1]:
#         return removeDups(newWord[1:])
#     else:
#         return newWord[0] + removeDups(newWord[1:])
#
# x= removeDups(newWord)
# print(x)