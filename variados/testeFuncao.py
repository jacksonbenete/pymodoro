# Teste de funcoes

def funcao(x):
    result = pow(((1/2)*x + (1/4)), 2)
    print("Expressão Original: " + repr(result))
    return True

def duvida(x):
    result = (16*(pow(x,2)) + 4) / 24
    print("Minha Dúvida: " + repr(result))
    return True

def produtoNotavel(x):
    "Expressão final através de produto notável"
    result = (pow(x,2)/4) + (x/4) + (1/16)
    print("Produto Notável: " + repr(result))
    return True

for x in range(-100, 100, 1):
    print("-------------//-------------")
    print("X = " + repr(x))
    print()
    funcao(x)
    duvida(x)
    produtoNotavel(x)
    print("-------------//-------------")
