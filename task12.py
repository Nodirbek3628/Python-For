num = int(input("Son kiriting:"))   # 1 dan boshlab kiritilgan songacha juft va toq sonlar yig'indisi alohida bajarildi
juft_son = 0
toq_son = 0

for i in range(1,num+1):
    if i %2 == 0:
        juft_son += i
        print(juft_son)
    if i %2 == 1:
        toq_son += i
        print(toq_son)

print(juft_son,",",toq_son)




