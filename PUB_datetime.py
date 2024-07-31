import datetime

def divide_days_into_periods(days: int, period_days_delta=30) -> list:
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

