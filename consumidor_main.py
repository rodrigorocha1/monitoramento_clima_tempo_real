import os
from src.consumidor.kafka_consumidor_clima import KafkaConsumidorClima


def limpar_terminal():

    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    kafka_consumer = KafkaConsumidorClima(
        bootstrap_servers='localhost:9092',
        group_id='weather_grupo',
        topico='topico_teste'
    )

    for dados in kafka_consumer.consumidor_mensagens():

        if dados['particao'] == 0:
            limpar_terminal()
        print('=' * 20)
        print(f'Partição: {dados["particao"]}')
        print(f"Cidade: {dados['cidade']}")
        print(f"Temperatura: {dados['temperatura']}°C")
        print(f"Data/Hora_api: {dados['data_hora_api']}")
        print(f"Data/Hora: {dados['data_hora_atual']}")

        print('=' * 20)


if __name__ == '__main__':
    main()
