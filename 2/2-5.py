# §PÂ_¦r¤¸
char = input("")
if (char >= "A" and char <= "Z") or (char >= "a" and char <= "z"):
    print(f"{char} is an alphabet.")
elif char >= "0" and char <= "9":
    print(f"{char} is a number.")
else:
    print(f"{char} is a symbol.") 