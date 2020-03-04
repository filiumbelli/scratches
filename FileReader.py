#fileOpen = open("ForLoops.txt","w+")
#inputter = "55\n" +"87\n" +"45\n"
#writer =fileOpen.write(inputter )
sum = 0
count = 0
for x in open("ForLoops.txt"):
    sum += int(x)
    count += 1

print(sum/count)