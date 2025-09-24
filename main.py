import os 
import sys
import pandas as pd 

project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(project_root)   

from ETL.Extract.extract_data import extract as extract
from ETL.Transform.transform_data import transform as transform
from ETL.Load.load_data import load_data as load_data
from config.db_connection import my_connection as conn

def main():
    print("Iniciando pipeline de ETL completo!")

    raw_df = extract()

    if raw_df is None:
        print("Nenhum dado encontrado. Encerrando processo")
        return

    if len(raw_df) == 0:
        print("Nenhum dado a ser extraido no momento.")
        return
    
    transformed = transform(raw_df)
    load = load_data(transformed, conn)

    print("Pipeline de ETL finalizado!")

if __name__ == "__main__":
    main()


