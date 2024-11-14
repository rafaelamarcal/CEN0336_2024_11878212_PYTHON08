#!/usr/bin/env python3

import sys

# Variáveis para armazenar informações de sequência e controlar a entrada de nucleotídeos válidos
seq_dict = {}           # Dicionário para armazenar as sequências com ID e descrição
sequence = ''           # Variável para armazenar a sequência atual
sequence_desc = ''      # Variável para a descrição da sequência atual
sequence_ID = ''        # Variável para o ID da sequência atual
valid_nt = set('ACTGN') # Conjunto com os nucleotídeos válidos (A, C, T, G e N)
file = ''               # Variável para armazenar o nome do arquivo de entrada

# Tenta obter o nome do arquivo de entrada
try:
    file = sys.argv[1]  # Obtém o argumento da linha de comando

    # Verifica se o arquivo possui uma extensão válida (.fa, .fasta, .nt)
    if not (file.endswith('.fa') or file.endswith('.fasta') or file.endswith('.nt')):
        raise ValueError('Not a valid FASTA file')

    # Abre o arquivo para leitura
    with open(file, 'r') as myFile:
        for line in myFile:
            # Verifica se a linha é um cabeçalho de sequência (começa com '>')
            if line.startswith('>'):
                # Se houver uma sequência já lida, armazena-a no dicionário
                if len(sequence) > 0:
                    seq_dict[sequence_ID] = {'sequence': sequence, 'description': sequence_desc}
                    sequence = ''  # Reinicia a sequência para a próxima entrada

                # Remove o '>' inicial, divide em ID e descrição e remove espaços
                line = line.lstrip('>').rstrip()
                sequence_ID, sequence_desc = line.split(maxsplit=1)
            else:
                # Processa linhas de sequência (nucleotídeos)
                line = line.rstrip().upper()  # Remove espaços e converte para maiúsculas
                # Valida cada nucleotídeo na linha para garantir que é válido
                for nt in line:
                    if nt not in valid_nt:
                        raise Exception('Invalid nucleotide characters')
                
                sequence += line  # Adiciona a linha à sequência atual

        # Armazena a última sequência processada
        if len(sequence) > 0:
            seq_dict[sequence_ID] = {'sequence': sequence, 'description': sequence_desc}

    # Abre o arquivo de saída para salvar as sequências formatadas em códons no frame 1
    with open('Python_08.codons-frame-1.nt', 'w') as wFile:
        for key in seq_dict:
            split_seq = ''  # String para armazenar a sequência formatada em códons
            seq_to_split = seq_dict[key]['sequence']  # Obtém a sequência completa

            # Divide a sequência em códons de 3 nucleotídeos no frame 1
            for i in range(0, len(seq_to_split), 3):
                split_seq += seq_to_split[i:i+3] + ' '  # Adiciona códon com espaço

            # Escreve o ID e a sequência de códons no frame 1 no arquivo de saída
            wFile.write(f"{key}-frame 1 codons\n{split_seq.strip()}\n")

    # Abre o arquivo de saída para salvar os frames 1, 2 e 3 dos códons
    with open('Python_08.codons-frame-3.nt', 'w') as wFile:
        for key in seq_dict:
            seq_to_split = seq_dict[key]['sequence']  # Obtém a sequência completa
            
            # Loop para processar cada um dos três frames
            for j in [0, 1, 2]:  # Frame 0 (posição inicial), 1 e 2
                split_seq = ''  # String para armazenar os códons do frame atual

                # Cria códons a partir do frame atual
                for i in range(j, len(seq_to_split), 3):
                    split_seq += seq_to_split[i:i+3] + ' '  # Adiciona códon com espaço

                # Escreve o ID e a sequência de códons para o frame atual no arquivo
                wFile.write(f"{key}-frame {j+1} codons\n{split_seq.strip()}\n")

# Tratamento de exceção para o caso de nenhum arquivo ser fornecido como argumento
except IndexError:
    print('Please provide a file')

# Tratamento de exceção para caso o arquivo não tenha uma extensão de FASTA válida
except ValueError as e:
    print(e)
