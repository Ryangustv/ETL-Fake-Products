#import ETL.Extract.extract_data as ext
import pandas as pd
import os 
import json 

def main():
    processed_dir = os.path.dirname(os.path.abspath(__file__))
    processed_data_dir = os.path.join(processed_dir, '../../data/processed')
    os.makedirs(processed_data_dir, exist_ok=True)

    raw_data_dir = os.path.join(processed_dir, '../../data/raw')

    try:
        raw_files = [f for f in os.listdir(raw_data_dir) if f.endswith('.json')]
        if not raw_files:
            raise FileNotFoundError("Nenhum arquivo JSON encontrado na pasta data/raw")
        
        latest_file = max(raw_files, key=lambda f: os.path.getmtime(os.path.join(raw_data_dir, f)))
        input_filepath = os.path.join(raw_data_dir, latest_file)

        print("Iniciando transformação de {latest_file} ...")

        with open(input_filepath, 'r') as file:
            weather_data_raw = file.read()
           
        raw_data = json.loads(weather_data_raw)

        df_transformed = pd.DataFrame(raw_data)

        df_transformed['category'] = df_transformed['category'].replace({
            "women's clothing": "Roupas Femininas",
            "jewelery": "Joias",
            "men's clothing": "Roupas Masculinas",
            "electronics": "Eletrônicos"
        })

        df_transformed = df_transformed.drop_duplicates(subset=['category'])

        output_filepath = os.path.join(processed_data_dir, 'weather_data_transformed.json')
        df_transformed.to_json(output_filepath,
                              index=False,
                              orient='records',
                              indent=4
                              )

        print(f"Transformação concluída. Dados salvos em {output_filepath}")

    except Exception as e:
        print(f"Erro inesperado: {e}")
    except KeyError  as e:
        print(f"Erro a Chave não foi localizada no JSON, verifique sua estrutuda do arquivo BRUTO: {e}")   
    except FileNotFoundError  as e:
        print(f"Erro: {e}" )
    
if __name__ == '__main__':
    main()

    