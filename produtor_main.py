import os
import time
from dotenv import load_dotenv
from src.produtor.kafka_produtor_clima import KafkaProdutorClima
from src.servico.servico_tempo import ServicoTempo
load_dotenv()


class ProdutorMain():
    def __init__(self):
        self.__kafka_produtor = KafkaProdutorClima(
            bootstrap_servers=os.environ['URL_KAFKA'])
        self.__cidades = [
            "Barrinha",
            "Brodowski",
            "Cravinhos",
            "Dumont",
            "Guatapará",
            "Jardinópolis",
            "Pontal",
            "Pradópolis",
            "Ribeirão Preto",
            "Santa Rita do Passa Quatro",
            "São Simão",
            "Serrana",
            "Serra Azul",
            "Sertãozinho"
        ]
        self.__topico = 'topico_tempo_dashboard'
        self.__servico_tempo = ServicoTempo()

    def rodar_produtor(self):

        self.__kafka_produtor.criar_topico(
            topico=self.__topico, numero_particoes=len(self.__cidades))
        numero_particoes = self.__kafka_produtor.verificar_particoes(
            topico=self.__topico)

        while True:
            for particao, cidade in enumerate(self.__cidades):
                dados_tempo = self.__servico_tempo.obter_tempo_atual(
                    cidade=cidade)
                self.__kafka_produtor.enviar_dados_clima(
                    topico=self.__topico,
                    dados_climaticos=dados_tempo,
                    municipio=cidade,
                    particao=particao)
            time.sleep(5)


if __name__ == '__main__':
    pm = ProdutorMain()
    pm.rodar_produtor()
