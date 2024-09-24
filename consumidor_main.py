from src.consumidor.kafka_consumidor_clima import KafkaConsumidorClima


def main():
    kafka_consumer = KafkaConsumidorClima(
        bootstrap_servers='localhost:9092',
        group_id='weather_grupo',
        topico='topico_app_tempo_real'
    )

    kafka_consumer.consumidor_mensagens()


if __name__ == '__main__':
    main()
