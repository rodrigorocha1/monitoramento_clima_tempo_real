class EstatisticaClimatica:
    @classmethod
    def obter_escala_vento(cls, velocidade: float) -> str:
        if 0 <= velocidade < 0.3:
            return 'Calmo'
        elif 0.3 <= velocidade < 1.5:
            return 'Aragem'
        elif 1.5 <= velocidade < 3.3:
            return 'Brisa leve'
        elif 3.3 <= velocidade < 5.4:
            return 'Brisa fraca'
        elif 5.4 <= velocidade < 7.9:
            return 'Brisa moderada'
        elif 8.0 <= velocidade < 10.7:
            return 'Brisa forte'
        elif 10.7 <= velocidade < 13.8:
            return 'Vento Fresco'
        elif 13.8 <= velocidade < 17.1:
            return 'Vento forte'
        elif 17.1 <= velocidade < 20.7:
            return 'Ventania'
        elif 20.7 <= velocidade < 24.4:
            return 'Ventania forte'
        elif 24.4 <= velocidade < 28.4:
            return 'Tempestade'
        elif 28.4 <= velocidade < 32.6:
            return 'Tempestade Violenta'
        else:
            return 'Furação'
