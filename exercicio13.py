numero = int(input("Digite um número: "))
multiplicacao = 0
for x in range(1, 11, 1):
    multiplicacao = numero * x

    print(f"{numero} x {x} = {multiplicacao}")