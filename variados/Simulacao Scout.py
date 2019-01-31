import random

# Simulacao de Scout
print("========================== Simulação de Classe Scout ==========================")
print("Assumindo rolagens como a metade do valor ou como a metade do valor +1 como média, exemplo:")
print("1d20 valerá 10+1, 1d8 valera 4+1, 1d4 valerá 2")

# Flags
simular_vida = 1
simular_tiros = 0

d4 = 2
d6 = 3
d8 = 5
d10 = 5
d12 = 6
d20 = 11

print()

# Simular Vida
if simular_vida == True:
    nivel = int(input("Entre com o Nível: "))
    # Vida
    print("================================ Simular Vida ================================")

    for con in [0,1,2,3,4]:
        print("CON >> +" + repr(con))
        vida = 24 + con + (nivel * (random.randrange(1,20) + con))
        print("Hit Points: " + repr(vida))

# Simular Tiros
if simular_tiros == True:
    print("================================ Simular Tiros ================================")
    # Dificuldade
    CA = 18
    # BBA +3, DEX +3
    bonus = 6
    # Dano da arma
    dados_dano = 3

    print("Simulação utilizando arma " + repr(dados_dano) + "d6 de dano, ataque" + repr(bonus) + ", CA +" + repr(CA) + ", dez tentativas")
    rolagens_d20 = []
    for x in range(1, 10):
        rolagens_d20.append(random.randrange(1, 20))

    print("Burst Fire => -5 penalty, +2 dados de dano")
    penalty = 5
    bonus_dano = 2
    dano_final = 0
    acertos = 0
    for rolagem in rolagens_d20:
        if (rolagem + bonus - penalty) > CA:
            print("Acerto => "+repr(dados_dano + bonus_dano)+"d6 ")
            dano_final = dano_final + dados_dano + bonus_dano
            acertos = acertos + 1
        else:
            print("FALHA")
    print("================================")
    print("Acertos = " + repr(acertos))
    print("Dano final = " + repr(dano_final) + "d6")
    print("================================")

    print("Rapid Shot => -2 penalty, +1 dado de dano")
    penalty = 2
    bonus_dano = 1
    dano_final = 0
    acertos = 0
    for rolagem in rolagens_d20:
        if (rolagem+bonus-penalty) > CA:
            print("Acerto => "+repr(dados_dano + bonus_dano)+"d6 ")
            dano_final = dano_final + dados_dano + bonus_dano
            acertos = acertos + 1
        else:
            print("FALHA")
    print("================================")
    print("Acertos = " + repr(acertos))
    print("Dano final = " + repr(dano_final) + "d6")
    print("================================")

    print("Point Blank Shot => +1 bonus")
    penalty = -1
    bonus_dano = 0
    dano_final = 0
    acertos = 0
    for rolagem in rolagens_d20:
        if (rolagem+bonus-penalty) > CA:
            print("Acerto => "+repr(dados_dano + bonus_dano)+"d6 ")
            dano_final = dano_final + dados_dano + bonus_dano
            acertos = acertos + 1
        else:
            print("FALHA")
    print("================================")
    print("Acertos = " + repr(acertos))
    print("Dano final = " + repr(dano_final) + "d6")
    print("================================")
