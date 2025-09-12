import services as con 
import pandas as pd 

df = pd.DataFrame(con.dados)

df['category'] = df['category'].replace({
    "women's clothing": "Roupas Femininas",
    "jewelery": "Joias",
    "men's clothing": "Roupas Masculinas",
    "electronics": "Eletrônicos"
})

df = df.drop_duplicates(subset=['category'])

for _, row in df.iterrows():
    con.cur.execute("""
        INSERT INTO categoria (descricao)
        VALUES (%s)
    """,(
        (row['category'],))
)


df['preco_promocional']  = df['price'] - (df['price'] * 0.1)

con.cur.execute(" ALTER TABLE promo ADD COLUMN IF NOT EXISTS preco_promocional NUMERIC(10,2);")

for _, row in df.iterrows():
    con.cur.execute("""
    INSERT INTO promo (produto, preco, preco_promocional, descricao, image_url, link_promo, fonte_api)
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

con.conn.commit()
con.cur.close()
con.conn.close()