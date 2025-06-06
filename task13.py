n = int(input("nechta son kiritasiz(n) :"))       #Telefon do'konidagi telfonlarning narxlaridan eng yuqorisi va eng past narxlarini toing..

number = int(input("1-sonni kiriting: "))
max = number
min = number

for i in range(2, n+1):
     
    num = int(input(f"{i}-sonni kiriting: "))

    if num > max:
        max = num
    elif num < min:
        min = num

resalt = (max + min)/2

print("Eng yuqori narx",max)
print("End past narx",min)
print(resalt)