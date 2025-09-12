from src.extract import fetch_api
from src.transform import transform_data 
from src.load import load_data

API_URL = "https://fakestoreapi.com/products"
RAW_PATH = "data/raw/products_raw.json"
PROCESSED_PATH = "data/processed/products_processed.csv"
CONN_PARAMS={
    "db_name": "",
    "user": "",
    "password": "",
    "host": "",
    "port": ""
}

df_raw = fetch_api(API_URL, RAW_PATH)
df_processed = transform_data(df_raw, PROCESSED_PATH)
df_loaded = load_data(df_processed, CONN_PARAMS)
