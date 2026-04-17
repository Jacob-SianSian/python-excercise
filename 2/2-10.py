sideLength1 = eval(input())
sideLength2 = eval(input())
sideLength3 = eval(input())
if sideLength1 >= sideLength2 and sideLength1 >= sideLength3:
    if sideLength1 < sideLength2 + sideLength3:
        print(sideLength1 + sideLength2 + sideLength3)
    else:        print("Invalid")
elif sideLength2 >= sideLength1 and sideLength2 >= sideLength3:
    if sideLength2 < sideLength1 + sideLength3:
        print(sideLength1 + sideLength2 + sideLength3)
    else:        print("Invalid")
elif sideLength3 >= sideLength1 and sideLength3 >= sideLength2:
    if sideLength3 < sideLength1 + sideLength2:
        print(sideLength1 + sideLength2 + sideLength3)
    else:        print("Invalid")