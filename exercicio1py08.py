#!/usr/bin/env python3

import sys

file_path = sys.argv[1]
sequences = {}

with open(file_path, 'r') as file:
    sequence_id, sequence_desc, sequence = '', '', ''

    for line in file:
        line = line.strip()
        if line.startswith('>'):
            # Armazena a sequência anterior no dicionário antes de processar uma nova
            if sequence:
                sequences[sequence_id] = {'sequence': sequence, 'description': sequence_desc}
            sequence_id, sequence_desc = line[1:].split(maxsplit=1)
            sequence = ''  # Redefine a sequência para a nova entrada
        else:
            sequence += line

    # Adiciona a última sequência processada ao dicionário
    if sequence:
        sequences[sequence_id] = {'sequence': sequence, 'description': sequence_desc}

# Conta e exibe a composição de bases
for seq_id, info in sequences.items():
    seq = info['sequence']
    base_counts = {base: seq.count(base) for base in 'ATCG'}
    sequences[seq_id] = {'sequence_composition': base_counts}
    
    print(f"{seq_id}\t{base_counts['A']}\t{base_counts['T']}\t{base_counts['G']}\t{base_counts['C']}")
