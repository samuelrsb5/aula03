quantidadeLitros = float(input("Informe quantos litros irá abastecer: "))
tipoCombustivel = input("Informe o tipo de combustível: ")

gasolina = 5.80
etanol = 4.90

abastecimentoGasolina = quantidadeLitros*gasolina
abastecimentoEtanol = quantidadeLitros*etanol


if tipoCombustivel == "G":
    print(f"O valor do abastecimento é de R${abastecimentoGasolina:.2f}")
elif tipoCombustivel == "E":
    print(f"O valor do abastecimento é de R${abastecimentoEtanol:.2f}")
else:
    print("Tipo inválido, informe apenas G(gasolina) ou E(etanol)")
