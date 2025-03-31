nome_aluno = input("Informe seu nome: ")
nota_1 = float(input("informe a nota 1: "))
nota_2 = float(input("informe a nota 2: "))
nota_3 = float(input("informe a nota 3: "))

media = (nota_1 + nota_2 + nota_3) / 3

# :.2f para formatar o número
if media >= 7:
    print(f"{nome_aluno}, sua média é {media:.2f} e você está aprovado")
if media < 4:
    print(f"{nome_aluno}, sua média é {media:.2f} e você está reprovado")
else:
    print((f"{nome_aluno}, sua média é {media:.2f} e você irá para a recuperação"))