letra = str(input("Digite uma letra:"))

if len(letra) == 1:

   if letra in "aeiou":
     print(f"A letra {letra} é uma vogal")

   elif letra in "bcdfghjklmnpqrstvwxyz":
    print(f"A letra {letra} é uma consoante")
    
   else:
     print("caracter invalido,digite uma letra do alfabeto")