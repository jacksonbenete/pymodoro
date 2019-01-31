# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 21:56:27 2016

QUEST MAGIC: The Mtg RPG!

@author: Muhammad
"""

import json
import sys
from types import *
#from pprint import pprint

#data = 0
#with open('AllCards.json') as data_file:
with open('SOI.json', encoding="utf8") as data_file:
    data = json.load(data_file)
    #data += 1

cards = data['cards']   

def inserir_carta(multiverseid, cmc, colorsIdentity, name, power, toughness, types, subtypes):
    # Testes
    
    assert type(multiverseid) is str, "multiverseid não é string: %r" % multiverseid
    assert type(cmc) is int, "cmc não é integer: %r" % cmc
    assert type(colorsIdentity) is str, "colorsIdentity não é string: %r" % colorsIdentity
    assert type(name) is str, "name não é string: %r" % name
    assert type(power) is str, "power não é integer: %r" % power
    assert type(toughness) is str, "toughness não é integer: %r" % toughness
    assert type(types) is str, "types não é string: %r" % types
    assert type(subtypes) is str, "subtypes não é string: %r" % subtypes
    
    import sqlite3
    conexao = sqlite3.connect('soi.db')
    tabela = "criaturas"
    db = conexao.cursor()
    #sys.exit("INSERT INTO " + tabela + " (multiverseid, cmc, colorsIdentity, name, power, toughness, types, subtypes) VALUES ("+ multiverseid +","+ repr(cmc) +","+ colorsIdentity +","+ name +","+ repr(power) +","+ repr(toughness) +","+ types +","+ subtypes + ")")
    try:
        query = "INSERT INTO " + tabela + " (multiverseid, cmc, colorIdentity, name, power, toughness, types, subtypes) VALUES ("+ multiverseid +","+ repr(cmc) +","+ colorsIdentity +","+ name +","+ repr(power) +","+ repr(toughness) +","+ types +","+ subtypes + ")"
        db.execute(query)
        conexao.commit()
        conexao.close()
        return True
    except sqlite3.Error as e:
        print("Um erro ocorreu: ", e.args[0])   
        sys.exit(query)
        

def procurar_criatura():
    
    for elemento in cards:
        var_tipos = []
        var_subtipos = []
        var_cores = []
        if 'cmc' not in elemento:
            continue
        else:
            if 'Creature' not in elemento['types']:
                continue
            else:
                for tipo in elemento['types']:
                    var_tipos.append(tipo)
                    for subtipo in elemento['subtypes']:
                        var_subtipos.append(subtipo)
                    if 'colorIdentity' not in elemento:
                        var_cores.append('I')
                    else:
                        for cores in elemento['colorIdentity']:
                            var_cores.append(cores)
        #sys.exit(repr(elemento['name']))
        inserir_carta(
            str(elemento['multiverseid']), 
            elemento['cmc'], 
            repr('-'.join(var_cores)), 
            repr(elemento['name']), 
            elemento['power'], 
            elemento['toughness'], 
            repr('-'.join(var_tipos)), 
            repr('-'.join(var_subtipos)))
            
procurar_criatura()


        
#for index, card in data['cards']:
#    print(index)