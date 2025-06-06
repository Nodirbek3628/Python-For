num = int(input("Sinfdagi  talabalarning yoshini kiriting:"))    #sinifdagi 5 ta talabalarning yoshini kiritib.
                                                                # ularni o'rtacha yoshini toping....
total = 0
for a in range(1,num+1):
    student = int(input(f"{a}-student age "))
    total +=student
    result = total/num
    print(result)