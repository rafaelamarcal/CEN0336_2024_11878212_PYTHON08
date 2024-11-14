#!/usr/bin/env python3

import sys
from function import *  # Importa funções externas como 'rev_comp' e 'translate'

# Dicionário para armazenar as sequências e suas descrições
seq_dict = {}
sequence = ''
sequence_desc = ''
sequence_ID = ''

# Nucleotídeos válidos
valid_nt = set('ACTGN')

# Tenta obter o arquivo passado como argumento
try:
    # Pega o arquivo fornecido como argumento
    file = sys.argv[1]
    
    # Verifica se o arquivo é do tipo correto (FASTA ou NT)
    if not (file.endswith('.fa') or file.endswith('.fasta') or file.endswith('.nt')):
        print("Arquivo não válido. Deve ser .fa, .fasta ou .nt")
        exit()

    # Abre o arquivo para leitura
    with open(file, 'r') as myFile:
        # Lê o arquivo linha por linha
        for line in myFile:
            if line.startswith('>'):  # Linha de cabeçalho
                # Se houver uma sequência armazenada, salva no dicionário
                if len(sequence) > 0:
                    seq_dict[sequence_ID] = {'sequence': sequence, 'description': sequence_desc}
                    sequence = ''  # Limpa para próxima sequência

                # Limpa o '>' e divide o cabeçalho em ID e descrição
                line = line.lstrip('>').rstrip()
                sequence_ID, sequence_desc = line.split(maxsplit=1)

            else:
                # Processa a sequência, convertendo para maiúsculas
                line = line.rstrip().upper()

                # Valida se todos os nucleotídeos são válidos
                for nt in line:
                    if nt not in valid_nt:
                        raise ValueError(f'Caractere inválido: {nt}')
                
                sequence += line  # Adiciona à sequência

        # No final, guarda a última sequência
        if len(sequence) > 0:
            seq_dict[sequence_ID] = {'sequence': sequence, 'description': sequence_desc}

    # Criando um dicionário para armazenar as sequências de códons
    total_nt_dict = {}

    # Abre o arquivo para escrever as sequências divididas em códons
    with open('Python_08.codons-frame-6.nt', 'w') as wFile:
        for key in seq_dict:
            seq_to_split = seq_dict[key]['sequence']
            # Gera a sequência complementar reversa
            rc_seq_to_split = rev_comp(seq_to_split)
            codon_dict = {}
            total_nt_dict[key] = codon_dict

            # Para cada um dos 3 frames (inicia em 0, 1 ou 2)
            for j in [0, 1, 2]:
                split_seq = ''
                rc_split_seq = ''

                # Divide a sequência em códons de 3 nucleotídeos
                for i in range(j, len(seq_to_split), 3):
                    split_seq += seq_to_split[i:i + 3] + ' '
                    rc_split_seq += rc_seq_to_split[i:i + 3] + ' '

                # Salva os códons para cada frame
                codon_frame_key = f'frame {1 + j} codons'
                rc_codon_frame_key = f'RC frame {1 + j} codons'
                total_nt_dict[key][codon_frame_key] = split_seq
                total_nt_dict[key][rc_cod
