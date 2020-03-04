sent="I am the only person that who loves the cats in this world.I love them sooo much!!!"
words= sent.split(" ")
print(words)
words= sorted(words)
print("Sentence in sorted order:\n")
print(len(words))
numWords= {}
for i in range(0,len(words)):
    if words[i] in numWords:
        numWords[words[i]] +=1
    else:
        numWords[words[i]] = 1
print("Word list and count: \n")
for key in numWords.keys():
    print(key,numWords[key])