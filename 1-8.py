x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"( {x1} , {y1} )")
print(f"( {x2} , {y2} )")
print(f"Distance = {distance:.4f}")