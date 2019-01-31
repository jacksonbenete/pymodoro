# Calcula o Rendimento de um Investimento

# Menos de mil reais não dá por causa da corretagem
saldo_inicial = 2000

# Alimentar Saldo significa depositar mensalmente um valor adicional
ALIMENTAR_SALDO = False
alimentoDeSaldo = 500 # Valor Minimo
alimentoDeSaldo = 1000 # Ideal

DAY_TRADE = True

# Corretagem
corretagem = 5.00 # Cinco reais em Day trade

# Juros referente ao rendimento MENSAL
juros = 0.6 # Poupança Bradesco
juros = 2.0 # Tesouro Direto
juros = 5.0 # Máxima
juros = 3.0 # Máxima Day trade
juros = 1.5 # Sorte Day trade

saldo = [saldo_inicial]
lucro = []
contador = 0
contador_dia = 0

print("Saldo Inicial: " + repr(saldo_inicial))
print("Juros: " + repr(juros) + "% ao mês")
if (ALIMENTAR_SALDO == True):
    print("Depósitos adicionais ao mês: " + repr(alimentoDeSaldo))

for anos in range(1):
    print()
    print("###############################")
    print("Ano " + repr(anos + 1))
    print("###############################")
    
    for meses in range(1):                
        if (DAY_TRADE == False):
            contador += 1
            saldo.append((saldo[contador - 1] + (saldo[contador - 1] * juros / 100)) - corretagem)
            print("Saldo do mês " + repr(meses + 1) + " : " + repr(saldo[contador]))
            lucro.append(saldo[contador] - saldo[contador - 1])
            
        if (ALIMENTAR_SALDO == True):
            saldo[contador] += alimentoDeSaldo

        if (DAY_TRADE == True):                        
            for dias in range(22):
                contador_dia += 1
                saldo.append((saldo[contador_dia - 1] + (saldo[contador_dia - 1] * juros / 100)) - corretagem)
                print("Dia " + repr(contador_dia) + " : " + repr(saldo[contador_dia]))
                lucro.append(saldo[contador_dia] - saldo[contador_dia - 1])
                

    print()

    print("Rendimento Mensal Inicial: " + repr(lucro[0]))
    print("Rendimento Mensal Final: " + repr(lucro[len(lucro) - 1]))
    print("Rendimento Final: " + repr(saldo[len(saldo) - 1] - saldo[0]))    
    print()

    if (ALIMENTAR_SALDO == True):
        saldoFinalSemInvestimento = saldo_inicial + (alimentoDeSaldo * (anos + 1) * (meses + 1))
        print("Saldo Final Sem Investimento: " + repr(saldoFinalSemInvestimento))
        print("Ganho: " + repr(saldoFinalSemInvestimento - saldo[len(saldo) - 1]))
    #else:
        #print("Ganho: " + repr((saldo[len(saldo) - 1] - saldo[0]) / 100))

    if (DAY_TRADE == True):
        print("Ganho mensal: " + repr((dias + 1) * juros * (meses + 1)) + "%")
        
    print()
    print("Saldo Final: " + repr(saldo[len(saldo) - 1]))

print()
input("Pressione ENTER...")
