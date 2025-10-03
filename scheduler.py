import schedule
import time
import yaml
from ETL.Extract.extract_data import extract 
from ETL.Transform.transform_data import transform 
from config.db_connection import my_connection as conn
from ETL.Load.load_data import load_data 


with open("cron.yaml", "r", encoding="utf-8") as f:
    cron = yaml.safe_load(f)

def run_etl():
    if not conn:
        print("Conexão inválida. Encerrando processo de carga.")
        return

    print("Iniciando extração dos dados")
    raw_df = extract()

    if raw_df is None:
        print("Nenhum dado encontrado. Encerrando processo")
        return

    if len(raw_df) == 0:
        print("Nenhum dado a ser extraido no momento.")
        return
    
    print("Iniciando transformação dos dados")
    transformed = transform(raw_df)

    print("Iniciando carga dos dados")
    load_data(transformed, conn)


for jobs in cron["cron"]:
    if jobs["description"] == "carregar dados":
        getattr(schedule.every(jobs["interval"]), jobs["unit"]).do(run_etl)
        print(f"Cron job agendado: {jobs['description']} a cada {jobs['interval']} {jobs['unit']}")

while True:
    schedule.run_pending()
    time.sleep(1)
