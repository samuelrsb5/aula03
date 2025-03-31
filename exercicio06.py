time_1 = float(input("Quantos gols o time 1 fez? "))
time_2 = float(input("Quantos gols o time 2 fez? "))

if time_1 > time_2:
    print("Time 1 ganhou")
if time_2 > time_1:
    print("Time 2 ganhou")
if time_1 == time_2:
    print("Empate")