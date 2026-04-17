# 轉16進制

num = eval(input())

if num >= 10:
    print(chr(ord('A')+num-10))
else:
    print(num)