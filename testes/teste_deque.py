import random
from datetime import datetime
from collections import deque
from time import sleep, time


ultimo_tempo = time()
print(f'Último tempo: {ultimo_tempo} segundos')

sleep(2)

tempo_decorrido = time() - ultimo_tempo
print(f'Tempo decorrido: {tempo_decorrido} segundos')


def gerar_temperatura():
    return {
        'temperatura': random.randint(0, 55),
        'data_hora': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }


d = deque()

for i in range(1, 6):
    d.append(gerar_temperatura())
    sleep(5)


tempo_decorrido = time() - ultimo_tempo
print(f'Tempo decorrido: {tempo_decorrido} segundos')

if tempo_decorrido > 15:
