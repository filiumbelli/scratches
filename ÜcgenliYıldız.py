for i in range(0,11):
    for j in range(0,i+1):

        if i >1:
            if j==0 or j==i:
                print("*", end=" ")
            elif i==10:
                print("*",end=" ")
            else:
                print(" ",end=" ")

        else:
            print("*", end=" ")
    print("\n")