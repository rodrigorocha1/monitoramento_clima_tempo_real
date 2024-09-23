import json
from typing import Dict
from kafka import KafkaProducer


class KafkaProdutorClima:
    def __init__(self, bootstrap_servers: str) -> None:
        self.__produtor = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=lambda k: k.encode('utf-8')
        )

    def enviar_dados_clima(self, topico: str, municipio: str, dados_climaticos: Dict, particao: int):
        self.__produtor.send(
            topic=topico,
            value=dados_climaticos,
            key=municipio,
            partition=particao
        )
        self.__produtor.flush()
