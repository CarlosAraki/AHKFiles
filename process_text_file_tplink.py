import pandas as pd

# Função para ler o arquivo de texto e extrair as informações desejadas
def process_text_file_tplink(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()

    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as file:
            data = file.read()
    
    # Inicializando listas para armazenar os dados
    ports = []
    input_broadcasts = []
    input_packets = []
    input_pauses = []
    output_broadcasts = []
    output_packets = []
    output_pauses = []
    input_percents = []
    output_percents = []
    output_packets = []

    # Dividindo o arquivo em blocos de portas
    port_blocks = data.strip().split("Port")
    
    for block in port_blocks[1:]:  # Ignorando o primeiro bloco vazio
        lines = block.strip().split('\n')
        
        port = lines[0].strip()

        in_broadcast = lines[3].strip().replace(',', '')
        in_packet = lines[11].strip().replace(',', '')
        
        in_percent = 0
        if int(in_packet) >0:
            in_percent = float(in_broadcast)/float(in_packet)
        
       
        
        out_broadcast = lines[20].strip().replace(',', '')
        out_packet = lines[28].strip().replace(',', '')

        out_percent = 0
        if int(out_packet) >0:
            out_percent = float(out_broadcast)/float(out_packet)

        ports.append(port)
        input_broadcasts.append(in_broadcast)
        input_packets.append(in_packet)
        input_percents.append(in_percent)
        output_broadcasts.append(out_broadcast)
        output_packets.append(out_packet)
        output_percents.append(out_percent)
    

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

