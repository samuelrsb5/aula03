nome_aluno = input("Informe seu nome: ")
nota_1 = int(input("informe a nota 1: "))
nota_2 = int(input("informe a nota 2: "))

media = (nota_1 + nota_2) / 2

if media >= 7:
    print(f"{nome_aluno}, sua média é {media} e você está aprovado")
else:
    print(f"{nome_aluno}, sua média é {media} e você está reprovado")