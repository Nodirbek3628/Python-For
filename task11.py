n = int(input("nechta son kiritasiz(n) :"))   # Foydalanivchi kiritilgan sondan eng kichik va eng katta sonlarni o'rtachasi topildi

number = float(input("1-sonni kiriting: "))
max = number
min = number

for i in range(2, n+1):
     
    numbers = float(input(f"{i}-sonni kiriting: "))

    if numbers > max:
        max = numbers
    elif numbers < min:
        min = numbers

resalt = (max + min) / 2

print(resalt)
