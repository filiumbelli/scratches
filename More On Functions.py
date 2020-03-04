def square(number):
    return number * number

sq=square
print(sq(2))
liste=[2,4,5,6,7,8,9]
newList =[sq(i)for i in liste]
print(newList)
numberssq = list(map(square,liste))
print(numberssq)
def fact(number):
    if number <=1:
        return 1
    else:
        return number*fact(number-1)

numberfact = list(map(fact,liste))
print(numberfact)