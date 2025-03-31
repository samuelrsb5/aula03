nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
salario = float(input("Informe seu salario: "))
porcentagemAcrescimo = float(input("Informe uma porcetangem de acrescimo: "))

valorAcrescimo = (salario * porcentagemAcrescimo) / 100

salarioAtualizado = salario + valorAcrescimo

# print(f"Seu nome é {nome}, tem {idade} anos e ganha R${salario}")

print(f"Nome: {nome}\nIdade: {idade}\nRecebeu um acrescimo de {porcentagemAcrescimo}% que equivalem a R${valorAcrescimo}.\nSeu salário atualmente é de R${salarioAtualizado}.")



