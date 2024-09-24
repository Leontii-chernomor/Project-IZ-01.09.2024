result_1 = input("Tipe some number")
number_1 = int(result_1)//10**4
number_2 = (int(result_1)%10**4)//10**3
number_3 = (int(result_1)%10**3)//10**2
number_4 = (int(result_1)%10**2)//10
number_5 = (int(result_1)%10**1)//1
number_6 = (number_5*10**4) + (number_4*10**3) + (number_3*10**2) + (number_2*10) +number_1
print(number_5,number_4,number_3,number_2,number_1)

print(number_6)