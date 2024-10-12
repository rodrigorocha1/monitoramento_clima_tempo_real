import streamlit as st
import time
from datetime import datetime
from src.consumidor.kafka_consumidor_clima import KafkaConsumidorClima
from typing import Dict


# Configuração da página
st.set_page_config(
    layout='wide',
    page_title='Dashboard Tempo Real'
)

# Título da página
st.title('Dashboard Tempo Real para Monitoramento das Condições Climáticas para a Região de Ribeirão Preto')

st.image('https://openweathermap.org/img/wn/04d.png')
