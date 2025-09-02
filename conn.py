import psycopg2 as psy 
import requests as req
import json 


conn = psy.connect(
    dbname="smartbuy",
    user="postgres",
    password="123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

url = "http://localhost:8080/produto"
response = req.get(url)
dados = response.json()

print(json.dumps(dados, indent=2))

for promo in dados:
    cur.execute("""
    INSERT INTO promo (produto, preco, descricao, categoria, image_url, link_promo, fonte_api)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""",(
    promo.get("title", ""),
    promo.get("price", 0.0),
    promo.get("description", ""),
    promo.get("category", ""),
    promo.get("image", ""),
    promo.get("permalink", ""),
    "API-PROMO"
    ) 
)

conn.commit()
cur.close()
conn.close()