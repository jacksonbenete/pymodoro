# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:31:09 2015

@author: Jackson
"""

import sys
from dicionarioFuncoes import *

argumentos = len(sys.argv) - 1

if argumentos == 0:
    print("Passe os argumentos representando as variaveis da funcao.")
elif argumentos == 1:
    """ Função Constante """
    funcao_constante(sys.argv[1])
elif argumentos == 2:
    """ Função Linear """
    funcao_linear(sys.argv[1], sys.argv[2])
elif argumentos == 3:
    """ Função Linear Afim """
    funcao_linear_afim()
elif argumentos == 4:
    """ Função Quadrática """
    funcao_quadratica()
elif argumentos == 5:
    """ Função Quadrática """
    funcao_quadratica()
else:
    print("ERRO: Muitos Argumentos.")
    
