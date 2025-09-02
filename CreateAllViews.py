from sqlalchemy import text
from sqlalchemy import create_engine

# -----------------------------
# 1. Conexão
# -----------------------------
db_user = "postgres"
db_password = "sua_senha"
db_host = "localhost"
db_port = "5432"
db_name = "iot"

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")


views = [
    """
    CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
    SELECT device_id, AVG(temperature) AS avg_temp
    FROM temperature_readings
    GROUP BY device_id;
    """,
    """
    CREATE OR REPLACE VIEW max_temp_por_dispositivo AS
    SELECT device_id, MAX(temperature) AS max_temp
    FROM temperature_readings
    GROUP BY device_id;
    """,
    """
    CREATE OR REPLACE VIEW min_temp_por_dispositivo AS
    SELECT device_id, MIN(temperature) AS min_temp
    FROM temperature_readings
    GROUP BY device_id;
    """
]

with engine.begin() as conn:  # begin() faz commit automático
    for view in views:
        conn.execute(text(view))