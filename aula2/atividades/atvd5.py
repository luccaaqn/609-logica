av1 = int (input("Digite sua AV1:"))
av2 = int (input("Digite sua AV2:"))


if (av1 + av2) / 2 >= 7 and (av1 + av2) / 2 < 10:
    print("APROVADO")
elif (av1 + av2) / 2 < 7:
    print("REPROVADO")
elif (av1 + av2) / 2 == 10:
    print("APROVADO COM DISTINÇÂO")
else:
    print("SUA NOTA ESTA ERRADA")