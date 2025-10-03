import psycopg2 as pg 

DB_PARAM = {
        'database':"ETL_Products",
        'host':"localhost",
        'port':"5432",
        'user':"postgres",
        'password':"123"
    }

def my_connection(db_params):
    try:   
        conn = pg.connect(**DB_PARAM)
        print("Conexão com banco de dados realizada com sucesso!")
        return conn
    except pg.Error as e:
        print(f"Erro ao conectar com banco de dados: {e}")
        return None

