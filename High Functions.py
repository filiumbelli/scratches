def countLetters(words):
    if len(words)<1:
        return 0
    else:
        return len(words[0]) + countLetters(words[1:])

def altcount(words):
    count=0
    for i in range(0,len(words)):
        count +=1
    return count
import functools
count = 0
words = "I have at least 30 letters in this string"
functools.reduce(lambda x: x in range (0,len(words))count=count +1 ,words)
print(cnt)
words="I have at least 30 letters in this string"
lenNew=countLetters(words)
print(lenNew)
words=["you","are","a","great","person"]
lenNew=countLetters(words)

print(lenNew)

