import pandas as pd

def extrair_numeros(string):
    return ''.join([char for char in string if char.isdigit()])\
    
def remover_strings_repetidas_preservar_ordem(lista):
    seen = set()
    result = []
    for item in lista:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Função para ler o arquivo de texto e extrair as informações desejadas
def process_text_file_3com(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()

    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as file:
            data = file.read()

    
    # Inicializando listas para armazenar os dados
    ports = []
    input_broadcasts = []
    input_multicasts = []
    input_pauses = []
    input_packets = []
    input_percents = []
    output_broadcasts = []
    output_multicasts = []
    output_pauses = []
    output_packets = []  
    output_percents = []

    # Dividindo o arquivo em blocos por porta
    blocks = data.split('----------------------------------------------------------')
    for block in blocks:
        if "port:" in block:
            lines = block.strip().split('\n')
            port = lines[0].split()[-1]
            input_percent = input_packet = input_broadcast = input_multicast = input_pause = '0'
            output_percent = output_packet = output_broadcast = output_multicast = output_pause = '0'
            inputFlag = 0; 
            outputFlag = 0; 

            for line in lines:
                if "Input(normal)" in line:
                    inputFlag = 0; 
                    outputFlag = 0; 
                    continue

                if "Output(normal)" in line:
                    inputFlag = 0; 
                    outputFlag = 0; 
                    continue

                if "Input: " in line :
                    inputFlag = 0; 
                    outputFlag = 0; 
                    continue

                if "Output: " in line :
                    inputFlag = 0; 
                    outputFlag = 0; 
                    continue

                if "Input(total)" in line :
                    input_packet = extrair_numeros(line.split(',')[0])
                    inputFlag+=1
                    continue
                    
                elif inputFlag>0:
                    parts = line.split(',')
                    if len(parts) > 1:
                        input_broadcast = parts[0].strip().split()[0]
                    if len(parts) > 2:
                        input_multicast = parts[1].strip().split()[0]
                    if len(parts) > 3:
                        input_pause = parts[2].strip().split()[0]
                    inputFlag -= 0

                elif "Output(total)" in line and outputFlag != 1 :
                    output_packet = extrair_numeros(line.split(',')[0])
                    outputFlag += 1; 
                    continue
                   
                elif outputFlag > 0 :
                    parts = line.split(',')
                    if len(parts) > 1:
                        output_broadcast = parts[0].strip().split()[0]
                    if len(parts) > 2:
                        output_multicast = parts[1].strip().split()[0]
                    if len(parts) > 3:
                        output_pause = parts[2].strip().split()[0]
                    outputFlag -= 1; 

            if float(input_packet) > 0:
               input_percent = float(input_broadcast)/float(input_packet)
            if float(output_packet) > 0:
               output_percent = float(output_broadcast)/float(output_packet)    

            input_percents.append(input_percent)
            output_percents.append(output_percent)
            ports.append(port)
            input_packets.append(input_packet)
            output_packets.append(output_packet)
            input_broadcasts.append(input_broadcast)
            input_multicasts.append(input_multicast)
            input_pauses.append(input_pause)
            output_broadcasts.append(output_broadcast)
            output_multicasts.append(output_multicast)
            output_pauses.append(output_pause)
            output_packets.append(output_packet)

    output_packets = remover_strings_repetidas_preservar_ordem(output_packets)
    
    # Criando um DataFrame com os dados coletados
    df = pd.DataFrame({
        'Port': ports,
        'Input Broadcasts': input_broadcasts,
        'Input Percent': input_percents,
        'Input Total': input_packets,
        'Output Broadcasts': output_broadcasts,
        'Output Percent': output_percents,
        'Output Total': output_packets,
        'file':file_path
    })
    
    return df

