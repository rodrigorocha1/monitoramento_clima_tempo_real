import json
import datetime
from kafka import KafkaConsumer


class KafkaConsumidorClima:
    def __init__(self, bootstrap_servers: str, group_id: str, topico: str) -> None:
        self.__consumer = KafkaConsumer(
            topico,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True
        )

    def consumidor_mensagens(self):
        for mensagem in self.__consumer:

            cidade = mensagem.value["name"]
            data_hora = datetime.datetime.fromtimestamp(
                mensagem.value["dt"]).strftime('%Y-%m-%d %H:%M:%S')
            temperatura = mensagem.value["main"]["temp"]
            data_hora_atual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            chave = mensagem.key
            particao = mensagem.partition
            offset = mensagem.offset
            print(
                f'Cidade: {cidade}, Data e Hora: {data_hora}, Temperatura: {temperatura}°C, data_hora_atual: {data_hora_atual}, chave: {chave}, particao: {particao} , offset: {offset} ')
