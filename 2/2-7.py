# 折扣方案

price = eval(input())
discount = price
if price >=38000:
    discount = price * 0.7
elif price >= 28000:
    discount = price * 0.8
elif price >= 18000:
    discount = price * 0.9
elif price >= 8000:
    discount = price * 0.95
print(f"{discount}")