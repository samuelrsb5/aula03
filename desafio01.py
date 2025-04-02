hora1 = int(input("Informe a hora 1: "))
minuto1 = int(input("Informe o minuto 1: "))
hora2 = int(input("Informe a hora 2: "))
minuto2 = int(input("Informe o minuto 2: "))

saidaHora = hora1 + hora2
saidaMinuto = minuto1 + minuto2

if saidaHora > 24:
    saidaHora = saidaHora - 24

if saidaHora > 12:
    saidaHora = saidaHora - 12

if saidaMinuto >= 60:
    saidaHora = saidaHora - 12
    saidaHora = saidaHora + 1
    saidaMinuto = saidaMinuto - 60



print(f"{saidaHora}:{saidaMinuto}")