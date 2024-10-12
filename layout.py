import streamlit as st
from src.utils.faixas_climaticas import obter_escala_vento
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

# Instância do consumidor Kafka
kafka_consumer = KafkaConsumidorClima(
    bootstrap_servers='localhost:9092',
    group_id='weather_grupo',
    topico='topico_tempo_dashboard'
)

# Função para gerar layout


def gerar_layout(dados: Dict):
    col1, col2, col3 = st.columns(3)
    print(dados['velocidade_vento'])

    with col1:
        st.write(f'Partição: {dados["particao"]}')
        st.write(f'**Cidade: {dados["cidade"]}**')
        st.write(f"Data hora API: {dados['data_hora_api']}")
        st.write(f"Temperatura: {dados['temperatura']}°C")
    with col2:
        st.write(f'Data/hora Atual: {dados["data_hora_atual"]}')
        st.write(f'Clima: {dados["clima"]}')
        st.image(f'https://openweathermap.org/img/wn/{dados["icone"]}.png')
        st.write(f'Umidade: {dados["umidade"]}%')
    with col3:
        st.write(
            f"Velocidade do Vento: {dados['velocidade_vento']} m/s - Condição vento: {obter_escala_vento(dados['velocidade_vento'])}"
        )
        st.write(f"Ângulo do Vento: {dados['angulo_vento']}°")
        st.write(f"Probabilidade de Chuva: {dados['probabilidade_chuva']}%")
    st.write('-' * 20)


numero_particoes = 14


container_tela = {
    particao: st.empty() for particao in range(numero_particoes)
}

while True:
    for particao in range(numero_particoes):
        print('Primeiro loop', particao)
        container_tela[particao].empty()
    for dados in kafka_consumer.consumidor_mensagens():
        particao = dados['particao']
        if particao in container_tela:
            with container_tela[particao].container():
                gerar_layout(dados=dados)
