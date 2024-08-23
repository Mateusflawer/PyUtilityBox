import datetime

def divide_days_into_periods(days: int, period_days_delta=30) -> list[tuple[datetime.datetime, datetime.datetime, int]]:
    """Divides days into periods, returning a list of the periods."""
    periods = []

    current_datetime = datetime.datetime.now()

    if days < period_days_delta:
        datetime_minus_days = current_datetime - datetime.timedelta(days=days)
        return [(datetime_minus_days, current_datetime, 0)]
    
    while days > 0:
        smaller_datetime = current_datetime - datetime.timedelta(days=days)
        if days > period_days_delta:
            larger_datetime = smaller_datetime + datetime.timedelta(days=period_days_delta)
        else:
            larger_datetime = current_datetime
        days_back = abs(current_datetime - larger_datetime).days
        periods.append((smaller_datetime, larger_datetime, days_back))
        days -= period_days_delta

    return periods

def divide_hours_into_periods(hours: int, period_hours_delta=24) -> list[tuple[datetime.datetime, datetime.datetime, int]]:
    """Divides hours into periods, returning a list of the periods."""
    periods = []

    current_datetime = datetime.datetime.now()

    if hours < period_hours_delta:
        datetime_minus_hours = current_datetime - datetime.timedelta(hours=hours)
        return [(datetime_minus_hours, current_datetime, 0)]
    
    while hours > 0:
        smaller_datetime = current_datetime - datetime.timedelta(hours=hours)
        if hours > period_hours_delta:
            larger_datetime = smaller_datetime + datetime.timedelta(hours=period_hours_delta)
        else:
            larger_datetime = current_datetime
        hours_back = abs(current_datetime - larger_datetime).seconds // 3600
        periods.append((smaller_datetime, larger_datetime, hours_back))
        hours -= period_hours_delta
    
    return periods

def generate_logs(days=1, days_ago=0, prefix="log_historico_") -> list:
    """
    Retorna uma lista de nomes de tabelas para consultar no banco de dados, baseando-se em uma faixa de dias.

    Parameters:
    days (int): Número de dias para gerar logs, incluindo o dia inicial. Valor padrão é 1.
    days_ago (int): Quantos dias atrás deve começar a contagem. Valor padrão é 0 (hoje).
    prefix (str): Prefixo para o nome das tabelas. Valor padrão é 'log_historico_'.

    Returns:
    list: Lista de nomes de tabelas com o prefixo e a data formatada.
    """
    logs = []
    now = datetime.date.today()
    end_date = now - datetime.timedelta(days=days_ago)
    start_date = end_date - datetime.timedelta(days=(days-1))

    while start_date <= end_date:
        log_name = f"{prefix}{start_date.strftime('%d%m%Y')}"
        logs.append(log_name)
        start_date += datetime.timedelta(days=1)

    return logs
