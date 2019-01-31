# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:31:09 2015

@author: Jackson
"""

import matplotlib.pyplot as plot

def funcao_constante(k):
    print("Funcao Constante do tipo y = k")
    x_vet = []
    y_vet = []    
    for x in range(-10,10):
        x_vet.append(x)
        y_vet.append(k)
    plot.plot(x_vet, y_vet, linestyle='-')
    plot.ylabel("Eixo y")
    plot.xlabel("Eixo x")
    plot.title("Função Constante")
    plot.show()

def funcao_linear(A,x):
    print("Funcao Linear do tipo y = Ax")
    x_vet = []
    y_vet = []    
    for contador in range(-10,10):
        x_vet.append(contador)
        y_vet.append(int(A) * int(contador))
    plot.plot(x_vet, y_vet, linestyle='-')
    plot.ylabel("Eixo y")
    plot.xlabel("Eixo x")
    plot.title("Função Constante")
    plot.show()

def funcao_linear_afim():
    return print("FOO")

def funcao_quadratica():
    return print("FOO")
