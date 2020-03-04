words = ("now", "is", "the", "time")
max = 0
for i in range(0, len(words)):
    for j in range(0,len(words)):
        if len(words[max]) >= len(words[j]):
            newLongest = words[max]
        else:
            max += 1

print(newLongest)

for i in range(0,len(words)):
    if len(words[i]) >= len(words[max]):
        max=i

print("The longest word is " + "* * "+ words[max])
