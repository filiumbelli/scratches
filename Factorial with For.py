sum = ""
for i in open("ForLoops.txt"):
    for j in range(1,int(i)):
        if j % 10 == 0:
            sum = sum + "*"
    print(sum +"  "+ i)
    sum = ""

