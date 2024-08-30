import datetime


def divide_days_into_periods(days: int, period_days_delta=30) -> list[tuple[datetime.datetime, datetime.datetime, int]]:
    """Divides a number of days into periods of length `period_days_delta`, returning a list of tuples containing 
    the start date, end date, and number of days in the period."""
    
    if days <= 0:
        raise ValueError("The number of days must be greater than zero.")
    
    periods = []
    current_datetime = datetime.datetime.now()

    while days > 0:
        if days <= period_days_delta:
            smaller_datetime = current_datetime - datetime.timedelta(days=days)
            larger_datetime = current_datetime
        else:
            smaller_datetime = current_datetime - datetime.timedelta(days=days)
            larger_datetime = smaller_datetime + datetime.timedelta(days=period_days_delta)

        days_back = (larger_datetime - smaller_datetime).days
        periods.append((smaller_datetime, larger_datetime, days_back))
        days -= period_days_delta

    return periods


def divide_hours_into_periods(hours: int, period_hours_delta=24) -> list[tuple[datetime.datetime, datetime.datetime, int]]:
    """Divides a number of hours into periods of length `period_hours_delta`, returning a list of tuples containing 
    the start date, end date, and number of hours in the period."""
    
    if hours <= 0:
        raise ValueError("The number of hours must be greater than zero.")
    
    periods = []
    current_datetime = datetime.datetime.now()

    while hours > 0:
        if hours <= period_hours_delta:
            smaller_datetime = current_datetime - datetime.timedelta(hours=hours)
            larger_datetime = current_datetime
        else:
            smaller_datetime = current_datetime - datetime.timedelta(hours=hours)
            larger_datetime = smaller_datetime + datetime.timedelta(hours=period_hours_delta)

        hours_back = (larger_datetime - smaller_datetime).seconds // 3600
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


def convert_to_seconds(time_str: str) -> int:
    """
    Converte um horário no formato HH:MM:SS para o total em segundos.

    Parameters:
    time_str (str): String representando o horário no formato HH:MM:SS.

    Returns:
    int: O total de segundos representado pelo horário. Retorna 0 se o input for inválido ou None.
    """
    if time_str:
        try:
            # Dividir a string em horas, minutos e segundos
            hours, minutes, seconds = map(int, time_str.split(':'))

            # Calcular o total de segundos
            return (hours * 3600) + (minutes * 60) + seconds
        except ValueError:
            # Retornar 0 se a string não estiver no formato correto
            return 0
    return 0


def convert_to_time(seconds: int) -> str:
    """
    Converts a value in seconds to HH:MM:SS format.

    Parameters:
    seconds (int or str): The total number of seconds to be converted.

    Returns:
    str: A string representing the time in HH:MM:SS format.
    """
    if seconds:
        if isinstance(seconds, str):
            if not seconds.isnumeric():
                return '00:00:00'
            seconds = int(seconds)
        
        # Ensure seconds is not negative and is an integer
        seconds = max(0, int(seconds))

        # Calculate hours, minutes, and seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Format the output in the desired format
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    return '00:00:00'


def convert_hours_to_time(hours: float) -> str:
    """
    Converts a value in hours to HH:MM:SS format.

    Parameters:
    hours (int, float, or str): The total number of hours to be converted.

    Returns:
    str: A string representing the time in HH:MM:SS format.
    """
    if hours:
        if isinstance(hours, str):
            try:
                hours = float(hours)
            except ValueError:
                return '00:00:00'
        
        # Ensure hours is not negative
        hours = max(0, float(hours))

        # Calculate total seconds
        total_seconds = int(hours * 3600)

        # Calculate hours, minutes, and seconds
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Format the output in the desired format
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

    return '00:00:00'

