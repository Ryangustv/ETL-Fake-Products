import psycopg2 as pg 
import pandas as pd
from config.db_connection import my_connection
from config.db_connection import DB_PARAM

processed_path = 'data/processed/weather_data_transformed.json'

try: 
    df = pd.read_json(processed_path)
except Exception as e:
    print("Erro ao ler dataframe.")
    df = pd.DataFrame()

def load_data(df, db_params):
    try:    
        with my_connection(db_params) as conn:

            with conn.cursor() as cur:

                for _, row in df.iterrows():
                    cur.execute("""
                    INSERT INTO categoria(nome)
                    VALUES (%s) ON CONFLICT (nome) DO UPDATE SET nome = EXCLUDED.nome
                    RETURNING id;            
                                """, (row['categoria'],)
                                )
                    id_categoria = cur.fetchone()[0] 

                    cur.execute("""
                    INSERT INTO promo(produto, preco, preco_promocional, descricao, categoria_id, fonte_api)
                    VALUES (%s, %s, %s, %s, %s, %s)
                                """,(
                                    row['nome'],
                                    row['preco'],
                                    row['preco_promocional'],
                                    row['descricao'],
                                    id_categoria,
                                    "API-FAKE-PRODUCTS"
                                ))
            conn.commit()
            print("Dados inseridos com Sucesso")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        print("finalizado")
if __name__ == '__main__':
    load_data(df, DB_PARAM)


        