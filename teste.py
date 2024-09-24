import os
from kafka import KafkaAdminClient
from dotenv import load_dotenv

load_dotenv()


def criar_topico(topico: str, num_particoes: int, fator_replicacao: int):
    # Conecta ao servidor Kafka
    admin_client = KafkaAdminClient(
        bootstrap_servers=os.environ['URL_KAFKA'],
        client_id='meu_cliente_admin'
    )

    # Verifica se o tópico já existe
    if topico in admin_client.list_topics():
        print(f"O tópico '{topico}' já existe.")
        return

    # Cria o novo tópico
    try:
        admin_client.create_topics(
            new_topics=[
                {
                    'topic': topico,
                    'num_partitions': num_particoes,
                    'replication_factor': fator_replicacao,
                }
            ],
            validate_only=False  # Se False, cria o tópico; se True, apenas valida
        )
        print(
            f"Tópico '{topico}' criado com {num_particoes} partições e fator de replicação {fator_replicacao}.")
    except Exception as e:
        print(f"Erro ao criar o tópico: {e}")


if __name__ == '__main__':
    criar_topico('novotopico', 3, 1)
