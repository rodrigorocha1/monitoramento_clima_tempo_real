import os
from src.consumidor.kafka_consumidor_clima import KafkaConsumidorClima


def limpar_terminal():

    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    kafka_consumer = KafkaConsumidorClima(
        bootstrap_servers='localhost:9092',
        group_id='weather_grupo',
        topico='topico_app_tempo_real'
    )

    for dados in kafka_consumer.consumidor_mensagens():

        if dados['particao'] == 0:
            limpar_terminal()
        print(dados)


if __name__ == '__main__':
    main()
