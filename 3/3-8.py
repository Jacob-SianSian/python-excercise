times = eval(input())
for i in range(times):
    num = eval(input())
    temp = num
    sum = 0
    while temp > 0:
        sum += temp % 10
        temp //= 10
    print(f"Sum of all digits of {num} is {sum}")
