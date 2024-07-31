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

    return periods

def divide_hours_into_periods(hours: int, period_hours_delta=24) -> list:
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