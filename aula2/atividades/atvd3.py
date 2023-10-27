sex = str(input("""
Digite seu sexo: 
F - Feminimo
M - Masculino
""")).upper().strip()

if sex =="F" or sex == "FEMININO":
    print(f"seu sexo é {sex}")

elif sex == "M" or sex == "Masculino":
    print(f"seu sexo é {sex}")

else: 
    print("seu sexo é invalido")    