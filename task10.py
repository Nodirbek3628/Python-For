max_son = int(input("1-sonni kiriting: "))     # Foydalanavchi tominidan kiritilgan 7 sondan maximium  qiymat topildi.

for i in range(2, 8):
    son = int(input(f"{i}-son kiriting: "))
    if son  > max_son:
        max_son = son
        
print(max_son)
