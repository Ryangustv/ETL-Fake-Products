FROM python:3.13  

WORKDIR /app 

COPY requirements.txt .   
COPY main.py . 
COPY cron.yaml .
COPY scheduler.py .    
COPY ETL/ . 
COPY data/ .
COPY config/ .

RUN pip install -r requirements.txt

CMD ["python", "scheduler.py"]


