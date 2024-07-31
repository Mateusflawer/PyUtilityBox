import datetime

def dividir_dias_em_periodos(dias: int, delta_dias_periodo=30) -> list:
    """Divide períodos em partes retornando uma lista com os períodos."""
    periodos = []

    datahora_agora = datetime.datetime.now()

    if dias < delta_dias_periodo:
        datahora_agora_menos_dias = datahora_agora - datetime.timedelta(days=dias)
        return [(datahora_agora_menos_dias, datahora_agora, 0)]
    
    while dias > 0:
        datahora_menor = datahora_agora - datetime.timedelta(days=dias)
        if dias > delta_dias_periodo:
            datahora_maior = datahora_menor + datetime.timedelta(days=delta_dias_periodo)
        else:
            datahora_maior = datahora_agora
        dias_para_tras = abs(datahora_agora - datahora_maior).days
        periodos.append((datahora_menor, datahora_maior, dias_para_tras))
        dias -= delta_dias_periodo
