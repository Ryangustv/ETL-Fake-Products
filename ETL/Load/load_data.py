import config.config as cc
import psycopg2 as pg 
import pandas as pd

conn = cc.my_connection()

processed_path = 'data/processed/weather_data_transformed.json'

df = pd.read_json(processed_path)

def load_data(df, conn):
    try:    
        with conn.cursor() as cur:
            for _, row in df.iterrows():
                cur.execute("""
                    INSERT INTO promo(produto, preco, preco_promocional, descricao, image_url, link_promo, fonte_api)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,(
                        row["title"],
                        row["price"],
                        row['preco_promocional'],
                        row["description"],
                        row["image"],
                        row["permalink"],
                        "API-PROMO"
                        )
                )
            conn.commit()
            print("Dados inseridos com Sucesso")
    except Exception as e:
        conn.rollback()
        print(f"Erro ao inserir dados: {e}")
    finally:
        conn.close()
        print("Conexao fechada.")
load_data(df, conn)