import json
from typing import Dict
from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic


class KafkaProdutorClima:
    def __init__(self, bootstrap_servers: str) -> None:
        self.__produtor = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=lambda k: k.encode('utf-8')
        )
        self.__admin_cliente = KafkaAdminClient(
            bootstrap_servers=bootstrap_servers)
        print(self.__admin_cliente)

    def criar_topico(self, topico: str, numero_particoes: int) -> None:
        novo_topico = NewTopic(
            name=topico, num_partitions=numero_particoes, replication_factor=1)
        self.__admin_cliente.create_topics([novo_topico])

    def verificar_particoes(self, topico: str) -> int:
        particoes = self.__admin_cliente.describe_topics([topico])
        print(particoes[0])
        print(particoes[0]['partitions'])
        return len(particoes[0]['partitions'])

    def enviar_dados_clima(self, topico: str, municipio: str, dados_climaticos: Dict, particao: int):
        self.__produtor.send(
            topic=topico,
            value=dados_climaticos,
            key=municipio,
            partition=particao
        )
        self.__produtor.flush()
