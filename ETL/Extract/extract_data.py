import requests as req
import json
import pandas as pd 
import os
import datetime

def extract():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_dir = os.path.join(base_dir, '../../data/raw')

    os.makedirs(raw_data_dir, exist_ok=True)

    url = "https://fakestoreapi.com/products"

    print("Iniciando extracao de dados da API...")

    try:
        #Realizando uma requisição do método GET para a API
        response = req.get(url, headers={'Accept': 'Application/json'})

        #Exceção para erros HTTP
        response.raise_for_status() 

        #Convertendo a resposta para JSON
        weather_data = response.json() 

        #Formata a data e hora atual
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") 

         #Nome do arquivo com timestamp
        filename = f"weather_data_{timestamp}.json"

        #Caminho do arquivo
        file_path = os.path.join(raw_data_dir, filename) 

        # Salvando os dados extraídos em um arquivo JSON na pasta data/raw
        with open(file_path, 'w') as json_file:
            json.dump(weather_data, json_file, indent=4)
        print(f"Dados extraidos e salvos em {file_path}")

        return raw_data_dir
    #Lançando exceções
    except req.exceptions.RequestException as e:
        print(f"Erro ao extrair dados da API: {e}")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
if __name__ == "__main__":
    extract()
