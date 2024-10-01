import json
import datetime
from kafka import KafkaConsumer
from collections import deque


class KafkaConsumidorClima:
    def __init__(self, bootstrap_servers: str, group_id: str, topico: str) -> None:
        self.__consumer = KafkaConsumer(
            topico,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            auto_offset_reset='latest',
            enable_auto_commit=True
        )
        self.temperaturas = deque()  # Armazena (timestamp, temperatura)

    def consumidor_mensagens(self):
        intervalo_minutos = 5
        intervalo_segundos = intervalo_minutos * 60

        for mensagem in self.__consumer:
            # Extrai os dados da mensagem
            cidade = mensagem.value["name"]
            data_hora = datetime.datetime.fromtimestamp(
                mensagem.value["dt"]).strftime('%Y-%m-%d %H:%M:%S')
            temperatura = mensagem.value["main"]["temp"]
            timestamp_mensagem = datetime.datetime.now()

            # Armazena a temperatura com o timestamp
            self.temperaturas.append((timestamp_mensagem, temperatura))

            # Remove as temperaturas fora do intervalo de 5 minutos
            while self.temperaturas and (timestamp_mensagem - self.temperaturas[0][0]).total_seconds() > intervalo_segundos:
                self.temperaturas.popleft()

            # Calcula a média das temperaturas no intervalo de 5 minutos
            if self.temperaturas:
                temperaturas_intervalo = [temp[1]
                                          for temp in self.temperaturas]
                media_temperatura = sum(
                    temperaturas_intervalo) / len(temperaturas_intervalo)
            else:
                media_temperatura = 0

            # Dados extras da mensagem
            data_hora_atual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            chave = mensagem.key
            particao = mensagem.partition
            offset = mensagem.offset

            # Exibe os dados e a média
            print(
                f'Cidade: {cidade}, Data e Hora: {data_hora}, Temperatura: {temperatura}°C, '
                f'Data e Hora Atual: {data_hora_atual}, Chave: {chave}, Partição: {particao}, Offset: {offset}, '
                f'Média das temperaturas nos últimos 5 minutos: {media_temperatura:.2f}°C'
            )
