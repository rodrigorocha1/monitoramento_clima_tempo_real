import os
import time
from dotenv import load_dotenv
from src.produtor.kafka_produtor_clima import KafkaProdutorClima
from src.servico.servico_tempo import ServicoTempo
load_dotenv()


def principal():
    kafka_produtor = KafkaProdutorClima(
        bootstrap_servers=os.environ['URL_KAFKA']

    )
    topico = 'topico_app_tempo_real'
    servico_tempo = ServicoTempo()
    cidades = ['Ribeirão Preto', 'Sertãozinho']

    kafka_produtor.criar_topico(topico=topico, numero_particoes=len(cidades))
    numero_particoes = kafka_produtor.verificar_particoes(topico=topico)
    print(
        f'Número de partições para o tópico {topico}: {numero_particoes}'
    )

    while True:
        for particao, cidade in enumerate(cidades):

            dados_tempo = servico_tempo.obter_tempo_atual(cidade=cidade)
            kafka_produtor.enviar_dados_clima(
                topico=topico,
                dados_climaticos=dados_tempo,
                municipio=cidade,
                particao=particao)
            time.sleep(2)


if __name__ == '__main__':
    principal()
