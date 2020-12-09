#!/usr/bin/python3
import sys
import os

if len(sys.argv) < 2:
    print('Parametro não foi passado!')
    exit()
file_name = sys.argv[1]

if os.path.exists(file_name):
    print('Arquivo existe: ' + file_name)
else:
    print('Arquivo não existe: ' + file_name)
