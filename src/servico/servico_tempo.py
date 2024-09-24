import os
from dotenv import load_dotenv
import requests
import datetime


class ServicoTempo:

    def __init__(self) -> None:
        self.__url = os.environ['URL_OPENWEATHER']
        self.__chave = os.environ['OPENWEATHER_KEY']

    def obter_tempo_atual(self, cidade: str):
        params = {
            'appid': self.__chave,
            'units': 'metric',
            'lang': 'pt_br',
            'q': cidade
        }
        response = requests.get(
            url=self.__url + 'weather',
            params=params,
            timeout=10
        )
        if response.status_code == 200:
            return response.json()
