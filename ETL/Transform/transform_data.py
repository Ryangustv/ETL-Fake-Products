import pandas as pd
import os 
import json 

def transform(df: pd.DataFrame):
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

        print(f"Iniciando transformação de {latest_file} ...")

        with open(input_filepath, 'r') as file:
            weather_data_raw = file.read()
           
        raw_data = json.loads(weather_data_raw)
        df_transformed = pd.DataFrame(raw_data)

        #Tratando dados referente a coluna 'categoria'
        df_transformed['categoria'] = df_transformed['category'].replace({
            "women's clothing": "Roupas Femininas",
            "jewelery": "Joias",
            "men's clothing": "Roupas Masculinas",
            "electronics": "Eletronicos"
        })
        df_transformed = df_transformed.drop_duplicates(subset=['categoria'])
        

        #Removendo expressões da coluna 'descrições'
        remove_expression = r'[;/*-+:]+'
        df_transformed['descricao'] = df_transformed['description'].str.replace(remove_expression, '', regex=True)
    
        #Inserindo a coluna 'preco_promocional' a estrutura do JSON
        df_transformed['preco_promocional'] = (df_transformed['price'] * 0.09).round(2)

        #Retirando e separando as colunas do dicionário 'rating'
        df_transformed['classificacao'] = df_transformed['rating'].apply(lambda x: x["rate"])
        df_transformed['quantidade_de_classificacao'] = df_transformed['rating'].apply(lambda x: x["count"])
        df_transformed = df_transformed.drop(columns=['rating'])

        df_transformed['preco'] = df_transformed['price']
        df_transformed['nome'] = df_transformed['title']

        df_transformed = df_transformed.drop(columns=['description', 'price', 'title', 'category'])

        #Salvando modificações no JSON antes de ser salvo para LOAD.
        #df_transformed.to_json('../../data/processed/weather_data_transformed.json', orient='records', force_ascii=False)

        output_filepath = os.path.join(processed_data_dir, 'weather_data_transformed.json')
        df_transformed.to_json(output_filepath,
                              index=False,
                              orient='records',
                              indent=4
                              )

        print(f"Transformação concluída. Dados salvos em {output_filepath}")

        return df_transformed
    except Exception as e:
        print(f"Erro inesperado: {e}")
    except KeyError  as e:
        print(f"Erro a Chave não foi localizada no JSON, verifique sua estrutuda do arquivo BRUTO: {e}")   
    except FileNotFoundError  as e:
        print(f"Erro: {e}" )
    
if __name__ == '__main__':
    transform()

    