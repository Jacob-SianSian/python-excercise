minute = eval(input())
second = eval(input())
kilometer = eval(input())
mile = kilometer / 1.6
speed = mile / (minute / 60 + second / 3600)
print(f"Speed = {speed:.1f}")