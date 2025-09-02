import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import plotly.express as px

# Conexão PostgreSQL
db_user = "postgres"
db_password = "sua_senha"
db_host = "localhost"
db_port = "5432"
db_name = "iot"

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

st.title('Dashboard de Temperaturas IoT')

# Gráfico 1: Média de temperatura por dispositivo
st.header('Média de Temperatura por Dispositivo')
df_avg_temp = load_data('avg_temp_por_dispositivo')
fig1 = px.bar(df_avg_temp, x='device_id', y='avg_temp')
st.plotly_chart(fig1)

# Gráfico 2: Temperatura máxima por dispositivo
st.header('Temperatura Máxima por Dispositivo')
df_max_temp = load_data('max_temp_por_dispositivo')
fig2 = px.bar(df_max_temp, x='device_id', y='max_temp')
st.plotly_chart(fig2)

# Gráfico 3: Temperatura mínima por dispositivo
st.header('Temperatura Mínima por Dispositivo')
df_min_temp = load_data('min_temp_por_dispositivo')
fig3 = px.bar(df_min_temp, x='device_id', y='min_temp')
st.plotly_chart(fig3)
