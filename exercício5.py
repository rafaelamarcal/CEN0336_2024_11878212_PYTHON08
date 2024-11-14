#!/usr/bin/env python3

import sys
from function import *  # Aqui, a função 'rev_comp' e 'translate' são importadas de um módulo externo

# Dicionário para armazenar as sequências com seus IDs e descrições
seq_dict = {}
sequence = ''
sequence_desc = ''
sequence_ID = ''

# Definir nucleotídeos válidos
valid_nt = set('ACTGN')

# Tenta pegar o arquivo fornecido pelo usuário como argumento de linha de comando
file = ''
try:
    # Verifica se o arquivo foi fornecido como argumento
    file = sys.argv[1]
    # Verifica se a extensão do arquivo é válida (FASTA ou .nt)
    if not (file.endswith('.fa') or file.endswith('.fasta') or file.endswith('.nt')):
        raise ValueError('Not a valid FASTA file')

    # Abre o arquivo de entrada
    with open(file, 'r') as myFile:
        # Lê cada linha do arquivo
        for line in myFile:
            # Verifica se a linha é um cabeçalho de sequência (inicia com '>')
            if line.startswith('>'):
                # Se já houver uma sequência armazenada, guarda ela no dicionário
                if len(sequence) > 0:
                    seq_dict[sequence_ID] = {'sequence': sequence, 'description': sequence_desc}
                    sequence = ''  # Limpa para a próxima sequência

                # Remove o '>' do cabeçalho e divide em ID e descrição
                line = line.lstrip('>').rstrip()
                sequence_ID, sequence_desc = line.split(maxsplit=1)
            else:
                # Processa a linha de sequência (convertendo para maiúsculas e verificando nucleotídeos válidos)
                line = line.rstrip().upper()
                for nt in line:
                    if nt not in valid_nt:
                        raise Exception('Invalid nucleotide characters')

                # Adiciona a linha à sequência
                sequence += line

        # No final, armazena a última sequência no dicionário
        if len(sequence) > 0:
            seq_dict[sequence_ID] = {'sequence': sequence, 'descri
