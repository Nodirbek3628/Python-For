n = int(input("enter :"))      # 1 dan boshlab "N" gacha bo'lgan sonlarning kvadratlari yig'indisini  topish.

b = 0

for a in range(1,n+1):
    b += a**2
    print(b)