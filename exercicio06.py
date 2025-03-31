nome_time1 = input("Qual o nome do time 1? ")
nome_time2 = input("Qual o nome do time 2? ")

gols_time1 = float(input("Quantos gols o time 1 fez? "))
gols_time2 = float(input("Quantos gols o time 2 fez? "))

if gols_time1 > gols_time2:
    print(f"{nome_time1} ganhou com {gols_time1} gols")
else:
    if gols_time2 > gols_time1:
        print(f"{nome_time2} ganhou com {gols_time2} gols")
    else:
        print(f"{nome_time1} e {nome_time2} empataram")