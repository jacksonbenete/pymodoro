#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from pprint import pprint
from sys import argv
from datetime import datetime

def cli_interface():
    massa = 0

    for arg in argv:
        
        if (arg == "massas" or arg == "massas.py"):
                continue
        if (arg[0] == "C" or arg[0] == "c"):
            if ( len(arg[1:]) > 0 ):
                massa = massa + ( 12 * int(arg[1:]))
            else:
                massa = massa + 12
        if (arg[0] == "O" or arg[0] == "o"):
            if ( len(arg[1:]) > 0 ):
                massa = massa + ( 16 * int(arg[1:]))
            else:
                massa = massa + 16
        if (arg[0] == "H" or arg[0] == "h"):
            if ( len(arg[1:]) > 0 ):
                massa = massa + ( 1 * int(arg[1:]))
            else:
                massa = massa + 1

    print("Massa total: ", str(massa))

def main():
    #print("\nLuna Assistant\n")

    # Se tem argumentos, então trata os argumentos
    if (len(argv) > 1):
        cli_interface()
        return True

if __name__ == '__main__':
    main()

