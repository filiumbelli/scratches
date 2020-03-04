fileOpen = open("life.txt","a")
print("Input ")
life= input("")
while life.lower() != "die":
    fileOpen.write(life +'\n')
    print("Anything else")
    life = input()
print("Goodbye")

