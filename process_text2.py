from process_text_file_3com import process_text_file_3com
from process_text_file_dlink import process_text_file_dlink
from process_text_file_intelbras import process_text_file_intelbras
from process_text_file_tplink import process_text_file_tplink
import os
import pandas as pd
from datetime import datetime


def process_files_in_directory(directory_path):
    if not os.path.isdir(directory_path):
        print(f"The provided path {directory_path} is not a valid directory.")
        return None
    
    all_dataframes = []
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        print(file_path)
        df = None
        if os.path.isfile(file_path):
            df = process_text_file_intelbras(file_path)
           
        if df is not None and isinstance(df, pd.DataFrame):
            all_dataframes.append(df)
    
    if all_dataframes:
        return pd.concat(all_dataframes, ignore_index=True)
    else:
        return None


def concat_df(all_dataframes):
    if all_dataframes:
        combined_df = pd.concat(all_dataframes, ignore_index=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"combined_data_{timestamp}.csv"
        combined_df.to_csv(output_file, index=False)
        print(f"Combined data saved to {output_file}")
    else:
        print("No dataframes to concatenate.")
          

if __name__ == "__main__":
    all_data_frames = []
    df_3com = process_files_in_directory('./valor')
    if df_3com is not None:
        all_data_frames.append(df_3com)
    
    print(df_3com)