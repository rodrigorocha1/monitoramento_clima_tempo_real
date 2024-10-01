import streamlit as st
import time
from datetime import datetime
from src.consumidor.kafka_consumidor_clima import KafkaConsumidorClima
st.set_page_config(
    layout='wide',
    page_title='Dashboard Tempo Real'
)
st.title('Dashboard Tempo Real para Monitoramento das Condições Climáticas para a Região de Ribeirão Preto')

kafka_consumer = KafkaConsumidorClima(
    bootstrap_servers='localhost:9092',
    group_id='weather_grupo',
    topico='topico_app_tempo_real'
)


placeholder = st.empty()

dados_municipios = []

municipios_por_atualizacao = 5


for dados in kafka_consumer.consumidor_mensagens():
    dados_municipios.append(dados)

    if len(dados_municipios) >= municipios_por_atualizacao:

        placeholder.empty()

        with placeholder.container():
            for chave, municipio in enumerate(dados_municipios):
                st.write(f'Chave: {chave}')
                st.write(f'Partição: {municipio["particao"]}')
                st.write(f"Cidade: {municipio['cidade']}")
                st.write(f"Temperatura: {municipio['temperatura']}°C")
                st.write(f"Data/Hora_api: {municipio['data_hora_api']}")
                st.write(f"Data/Hora: {municipio['data_hora_atual']}")
                st.write('-' * 20)

        dados_municipios.clear()

    time.sleep(1)
