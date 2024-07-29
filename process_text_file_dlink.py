import pandas as pd

# Função para ler o arquivo de texto e extrair as informações desejadas
def process_text_file_dlink(file_path):
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
    input_packets = []
    input_percents = []
    input_pauses = []
    output_broadcasts = []
    output_multicasts = []
    output_pauses = []
    output_packets = []
    output_percents = []

    # Dividindo o arquivo em linhas
    lines = data.strip().split('\n')
    for line in lines:
        if line.startswith("eth"):
            parts = line.split()
            port = parts[0]
            in_octets = parts[1]
            in_ucast_pkts = parts[2]
            in_mcast_pkts = parts[3]
            in_bcast_pkts = parts[4]
            out_octets = parts[5]
            out_ucast_pkts = parts[6]
            out_mcast_pkts = parts[7]
            out_bcast_pkts = parts[8]
            in_pkts_total = int(in_ucast_pkts) + int(in_mcast_pkts) +int(in_bcast_pkts)
            out_pkts_total = int(out_ucast_pkts) + int(out_mcast_pkts) +int(out_bcast_pkts)

            input_percent = 0
            output_percent = 0

            ports.append(port)
            if in_pkts_total > 0:
                input_percent = float(in_bcast_pkts)/float(in_pkts_total)

            if out_pkts_total > 0:
                output_percent = float(out_bcast_pkts)/float(out_pkts_total)

            input_percents.append(input_percent)
            output_percents.append(output_percent)
            input_packets.append(str(in_pkts_total))
            output_packets.append(str(out_pkts_total))
            input_broadcasts.append(in_bcast_pkts)
            input_multicasts.append(in_mcast_pkts)
            input_pauses.append(in_octets)
            output_broadcasts.append(out_bcast_pkts)
            output_multicasts.append(out_mcast_pkts)
            output_pauses.append(out_octets)
    
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

