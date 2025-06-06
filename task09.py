min_son = int(input("1-sonni kiriting: "))    # Foydalanavchi tominidan kiritilgan 7 sondan minimum  qiymat topildi.

for i in range(2, 8):
    son = int(input(f"{i}-son kiriting: "))
    if son  < min_son:
        min_son = son
        
print(min_son)
