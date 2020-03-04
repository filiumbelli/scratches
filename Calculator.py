num1= 0.0
num2= 0.0
operator = " "
while (num1 != "q"):
    print("enter first number (q to quit)")
    num1 = input()
    if num1 == "q":
        break
    num1 = float(num1)
    print("Enter operator")
    operator=input()
    print("Enter second number")
    num2 = int(input())
    if (operator == "+"):
        print(num1+num2)
    elif (operator =="-"):
        print(num1-num2)
    elif (operator == "*"):
        print(num1*num2)
    elif (operator == "/"):
        print(num1/num2)
    else:
        print("wrong value")



