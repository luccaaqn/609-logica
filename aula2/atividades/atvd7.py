num1 = int(input("Digite um numero(1):"))
num2 = int(input("Digite um numero(2):"))
num3 = int(input("Digite um numero(3):"))

if num1 and num2 > num3 and num1 > num2:
  print(f"O numero {num1} e maior, e o numero {num3} e o menor ")
elif num1 and num3 > num2 and num3 > num2:
  print(f"O numero {num1} e maior, e o numero {num2} e o menor ")  
elif num2 and num3 > num1 and num2 > num3:
  print(f"O numero {num2} e maior, e o numero {num1} e o menor ") 
elif num2 and num1 > num3 and num2 > num1:
  print(f"O numero {num2} e maior, e o numero {num3} e o menor ")   
elif num3 and num2 > num1 and num3 > num2:
  print(f"O numero {num3} e maior, e o numero {num2} e o menor ")
elif num3 and num2 > num1 and num2 > num3:
  print(f"O numero {num3} e maior, e o numero {num1} e o menor ")      
else 
  print(f"os numeros {num1,num2,num3} sao iguais")
