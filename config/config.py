import psycopg2 as pg 

def my_connection():
    connection = pg.connect(
        database="ETL basic",
        host="localhost",
        port="5432",
        user="postgres",
        password="123"
    )
    return connection

conn = my_connection()

print(conn.info)
print(conn.status)

conn.close()

