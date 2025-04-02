
quantidadeLitros = float(input("Informe quantos litros irá abastecer: "))
tipoCombustivel = input("Informe o tipo de combustível: ")

gasolina = 5.80
etanol = 4.90



if tipoCombustivel == "G" or tipoCombustivel == "g":
    abastecimentoGasolina = quantidadeLitros * gasolina
    print(f"O valor do abastecimento é de R${abastecimentoGasolina:.2f}")
elif tipoCombustivel == "E" or tipoCombustivel == "e":
    abastecimentoEtanol = quantidadeLitros * etanol
    print(f"O valor do abastecimento é de R${abastecimentoEtanol:.2f}")
else:
    print("Tipo inválido, informe apenas G(gasolina) ou E(etanol)")
