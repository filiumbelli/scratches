fileOpen = open("Online.txt","a")
print("what do you want to do with your life? ")
x=input("")
while (x != "die" or x != "DIE"):
    print("Anything Else")
    fileOpen.write("Online")
    x=input(" ")
    if x == "die" or x=="DIE":
        break
print("good luck with your life")
