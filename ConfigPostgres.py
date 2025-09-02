import psycopg2
import pandas as pd

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, Table, Column, Integer, Float, String, MetaData

# -----------------------------
# 1. Conexão
# -----------------------------
db_user = "postgres"
db_password = "sua_senha"
db_host = "localhost"
db_port = "5432"
db_name = "iot"


# 1️⃣ Conectar no banco default (postgres)
conn = psycopg2.connect(user=db_user, password=db_password, host=db_host, port=db_port, dbname="postgres")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

# 2️⃣ Criar banco se não existir
cur.execute(f"SELECT 1 FROM pg_database WHERE datname='{db_name}'")
exists = cur.fetchone()
if not exists:
    cur.execute(f"CREATE DATABASE {db_name}")
    print(f"Banco '{db_name}' criado!")
else:
    print(f"Banco '{db_name}' já existe.")

cur.close()
conn.close()

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
metadata = MetaData()

# 2. Create Table
temperature_readings = Table(
    'temperature_readings', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('device_id', String),
    Column('temperature', Float)
)

metadata.create_all(engine)

# 3. Ler CSV
df = pd.read_csv('IOT-temp.csv')

df = df[['id', 'temp']] 

df.columns = ['device_id', 'temperature']


# 3. Commit
df.to_sql('temperature_readings', engine, if_exists='append', index=False)

print("Dados inseridos com sucesso!")
