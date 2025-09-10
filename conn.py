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