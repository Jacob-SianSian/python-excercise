# ºâ³N¹Bºâ

num1 = eval(input(""))
num2 = eval(input(""))
operator = input("")
if operator == "+":
    print(f"{num1 + num2}")
elif operator == "-":
    print(f"{num1 - num2}")
elif operator == "*":
    print(f"{num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"{num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
elif operator == "%":
    if num2 != 0:
        print(f"{num1 % num2}")
    else:
        print("Error: Modulo by zero is not allowed.")
elif operator == "//":
    if num2 != 0:
        print(f"{num1 // num2}")
    else:
        print("Error: Floor division by zero is not allowed.")