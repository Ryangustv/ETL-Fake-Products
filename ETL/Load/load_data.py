import psycopg2 as pg 
import pandas as pd
from config.db_connection import my_connection
from config.db_connection import DB_PARAM

processed_path = 'data/processed/weather_data_transformed.json'

#Tentando ler o DataFrame
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
                    #Inserindo dados na tabela 'Categoria'
                    cur.execute("""
                    INSERT INTO categoria(nome)
                    VALUES (%s) ON CONFLICT (nome) DO UPDATE SET nome = EXCLUDED.nome
                    RETURNING id;            
                                """, (row['categoria'],)
                                )
                    id_categoria = cur.fetchone()[0] 

                    #Inserindo dados na tabela 'Produto'
                    cur.execute("""
                    INSERT INTO produto(codigo, nome_produto, descricao, preco_base, preco_promocional, id_categoria)
                    VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (codigo) DO UPDATE SET codigo = EXCLUDED.codigo
                    returning id;
                                """, (row['codigo'],
                                      row['nome'],
                                      row['descricao'],
                                      row['preco'],
                                      row['preco_promocional'],
                                      id_categoria)
                                )
                    id_produto = cur.fetchone()[0]

                    #Inserindo dados na tabela 'Classificacao'
                    cur.execute("""
                    INSERT INTO classificacao(produto_id, quantidade_classificacao, nota_media)
                    VALUES (%s, %s, %s)  ON CONFLICT (produto_id) DO UPDATE SET produto_id = EXCLUDED.produto_id
                    returning id;
                                """, (id_produto,
                                      row['quantidade_de_classificacao'],
                                      row['classificacao'])
                                      )

                    #Inserindo dados na tabela 'Promocao'
                    cur.execute("""
                    INSERT INTO promocao(produto_id, tipo_promocao, fonte_api)
                    VALUES (%s, %s, %s)
                                """,(
                                    id_produto,
                                    row['tipo_promo'],
                                    "API-FAKE-PRODUCTS"
                                ))
            conn.commit()
            print("Dados carregados com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        print("finalizado")
if __name__ == '__main__':
    load_data(df, DB_PARAM)


        