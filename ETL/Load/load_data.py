import psycopg2 as pg 

def load_data(df, conn_params):
    conn = pg.connect(**conn_params)
    cur = conn.cursor()

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
                "API-PROMO")
        )