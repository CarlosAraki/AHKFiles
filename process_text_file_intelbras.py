import pandas as pd

# Função para ler o arquivo de texto e extrair as informações desejadas
def process_text_file_intelbras(file_path):
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
    output_broadcasts = []
    output_multicasts = []
    output_pauses = []

    # Dividindo o arquivo em blocos por porta
    blocks = data.split('Port')
    
    for block in blocks:
        if "Received" in block:
            lines = block.strip().split('\n')
            port = lines[0].strip()

            # Inicialização com valores padrão
            input_broadcast = input_multicast = input_pause = '0'
            output_broadcast = output_multicast = output_pause = '0'
            
            for line in lines:
                if "Broadcast" in line and "Received" not in line and "Sent" not in line:
                    parts = line.split('\t')
                    input_broadcast = parts[1].strip().replace(',', '')
                    output_broadcast = parts[4].strip().replace(',', '')
                elif "Multicast" in line:
                    parts = line.split('\t')
                    input_multicast = parts[1].strip().replace(',', '')
                    output_multicast = parts[4].strip().replace(',', '')
                elif "Alignment Errors" in line:
                    parts = line.split('\t')
                    input_pause = parts[1].strip().replace(',', '')
                elif "Collisions" in line:
                    parts = line.split('\t')
                    output_pause = parts[1].strip().replace(',', '')
            
            ports.append(port)
            input_broadcasts.append(input_broadcast)
            input_multicasts.append(input_multicast)
            input_pauses.append(input_pause)
            output_broadcasts.append(output_broadcast)
            output_multicasts.append(output_multicast)
            output_pauses.append(output_pause)
    
    # Criando um DataFrame com os dados coletados
    df = pd.DataFrame({
        'Port': ports,
        'Input Broadcasts': input_broadcasts,
        'Input Percent': input_multicasts,
        'Input Total': input_pauses,
        'Output Broadcasts': output_broadcasts,
        'Output Percent': output_multicasts,
        'Output Total': output_pauses,
        'file':file_path
    })

    
    return df
