#!/usr/bin/env python3

import sys

# Inicializa as variáveis principais
seq_dict = {}            # Dicionário para armazenar as sequências com seus IDs e descrições
sequence = ''            # Variável temporária para armazenar a sequência atual
sequence_desc = ''       # Variável para armazenar a descrição da sequência
sequence_ID = ''         # Variável para armazenar o ID da sequência
file = ''                # Variável para o nome do arquivo

# Tenta obter o arquivo de entrada como argumento de linha de comando
try:
    file = sys.argv[1]
except IndexError:
    # Exibe uma mensagem e encerra o programa caso o arquivo não seja fornecido
    print('Please provide a file')
    sys.exit(1)  # Encerra o programa com um código de erro

# Abre o arquivo para leitura
with open(file, 'r') as myFile:

    # Processa cada linha do arquivo
    for line in myFile:
        line = line.s
