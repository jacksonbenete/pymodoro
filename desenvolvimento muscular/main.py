# Programa de Desenvolvimento Muscular
from funcoes import *

print("==================== Desenvolvimento Muscular ====================")

while True:
    opcao = selecionar_funcao()
    if opcao == '1':
        tabela = selecionar_tabela()
        if tabela != "sair":
            visualizar_desenvolvimento(tabela)
    elif opcao == '0':
        tabela = selecionar_tabela()
        if tabela != "sair":
            inserir_dados(tabela)
    elif opcao == '2':
        visualizar_tudo()
    elif opcao == '3':
        diferenca_simetria()
    elif opcao == 'q':
        break
