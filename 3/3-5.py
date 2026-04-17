num = eval(input())

while num >= 10:
    print(num % 10, end="")
    num //= 10
print(num)