num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))

if num1 > num2 and num1 > num3:
    print(f"O número {num1} é maior")

elif num2 > num1 and num2 > num3:
    print(f"O número {num2} é maior")

elif num3> num1 and num3 > num2:
    print(f"O número {num3} é maior")

else:
    print(f"O número {num1,num2,num3} sao iguais")

