
database = 'medidas.db'

def selecionar_tabela():
    "Escolhe a tabela desejada"
    opcoes = {"1": "peso", "2": "peito", "3": "braco", "4": "quadril", "5": "perna", "q": "sair"}
    print("Digite o numero da tabela a seguir:")
    print("[1] peso")
    print("[2] peito")
    print("[3] braco")
    print("[4] quadril")
    print("[5] perna")
    print("[q] sair")  
    print()
    opcao_tabela = input(">> ")
    
    return opcoes[opcao_tabela]

def selecionar_funcao():
    "Escolhe a funcao desejada"
    print("Digite o numero da opcao desejada:")
    print("[1] Visualizar Desenvolvimento")
    print("[2] Visualizar Tudo")
    print("[3] Diferenca entre a Simetria Perfeita")
    print("[0] Inserir Dados")
    print("[q] Sair")
    print()
    opcao_funcao = input(">> ")

    return opcao_funcao

def inserir_dados(tabela):
    import sqlite3
    conexao = sqlite3.connect(database)
    db = conexao.cursor()

    while True:
        print("Entre com a Data no formato 'dd/mm/yy'")
        print("Caso deseje sair, digite 'q'")
        data = input(">> ")
        if data == "q":
              conexao.close()
              break
              
        print("Entre com a Medida em cm, apenas numeros, exemplo '4.9'")
        print("Caso deseje sair, digite 'q'")
        medida = input(">> ")
        if medida == "q":
              conexao.close()
              break   
        try:
            db.execute("INSERT INTO " + tabela + " (data, medida) VALUES ('"+ data +"', " + repr(medida) + ")")
            conexao.commit()
            conexao.close()
            return True
        except sqlite3.Error as e:
            print("Um erro ocorreu: ", e.args[0])       

def visualizar_desenvolvimento(tabela):
    import matplotlib.pyplot as plot
    import datetime as DT
    import sqlite3
    conexao = sqlite3.connect(database)
    db = conexao.cursor()

    x = []
    y = []
    
    for row in db.execute("SELECT * FROM " + repr(tabela)):
        x.append(DT.datetime.strptime(row[0], "%d/%m/%Y"))
        y.append(row[1])    
    plot.plot_date(x, y, linestyle='-', marker=None)
    ymin, ymax = plot.ylim()
    plot.ylim(ymin, ymax + 0.01)
    plot.gcf().autofmt_xdate()
    plot.title("Desenvolvimento " + tabela + " (" + repr(y[-1]) + " cm/kg)")
    plot.xlabel("Data")
    plot.ylabel("Medida (cm ou kg)")
    plot.show()
    return True

def diferenca_simetria():
    import matplotlib.pyplot as plot
    import sqlite3
    conexao = sqlite3.connect(database)
    db = conexao.cursor()

    print("==================== Simetria Perfeita ====================")

    # Simetria ideal Arnold (para 180 cm)
    #simetria = {'braco': 53.6, 'peito': 138.78, 'quadril': 100.1,
    #            'perna': 69.318, 'peso': 101.95}
    
    # Simetria ideal segundo tabela (no coeficiente)
    simetria = {'braco': 40, 'pescoco': 42.5, 'antebraco': 33.4,
                'peito': 110.9, 'cintura': 83.1, 'quadril': 99.9,
                'perna': 59.9, 'panturrilha': 40, 'coeficiente': 0.478,
                'peso': 86.1}
    tabelas = []
    for tabela in db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"):
        tabelas.append(tabela[0])
    for tabela in tabelas:
        for row in db.execute("SELECT medida FROM " + tabela + " ORDER BY id DESC LIMIT 1"):
            diferenca = simetria[tabela] - row[0]
            print("Diferenca de medida " + tabela + ": {:03.2f} cm \t(Atual: {:03.2f} cm, Ideal: {:03.2f} cm)".format(diferenca, row[0], simetria[tabela]))
    print("============================================================")
    print()
    return True

def visualizar_tudo():
    import sqlite3
    import matplotlib.pyplot as plot
    import datetime as DT
    
    conexao = sqlite3.connect(database)
    db = conexao.cursor()

    x = []
    y = []
    plots = []
    tabelas = []
    
    fig = plot.figure()
    fig.subplots_adjust(left=0.2, wspace=1)
    
    plot_number = 230
    k = 0
    for tabela in db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"):
        tabelas.append(tabela[0])
    for tabela in tabelas:
        for row in db.execute("SELECT * FROM " + tabela):
            x.append(DT.datetime.strptime(row[0], "%d/%m/%Y"))
            y.append(row[1])
        plot_number = plot_number + 1
        p = fig.add_subplot(plot_number)
        p.plot(x, y)
        ymin, ymax = plot.ylim()
        plot.ylim(ymin, ymax + 0.01)
        plot.gcf().autofmt_xdate()
        if (tabela == "peso"):
            plot.title(tabela + " (" + repr(y[-1]) + " kg)")
        else:
            plot.title(tabela + " (" + repr(y[-1]) + " cm)")
        plot.xlabel("Data")
        plot.ylabel("Medida (cm ou kg)")
        x = []
        y = []
        k = k + 1
    plot.show()
    
# TEST ZONE
#print(selecionar_tabela())
#visualizar_desenvolvimento("peso")
#visualizar_tudo()
#diferenca_simetria()
