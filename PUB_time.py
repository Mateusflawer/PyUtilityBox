import time

def countdown_timer(wait_seconds: int, msg_wait=""):
    """Countdown by seconds"""
    for i in range(wait_seconds, 0, -1):
        print(f"{msg_wait} {i} second(s) ...", end='\r')
        time.sleep(1)  # Waits for 1 second
        

def retry_on_failure(max_retries: int):
    """
    Decorator that retries the execution of a function in case of failure.
    
    Parameters:
        max_retries (int): Maximum number of retry attempts.
    
    Returns:
        The decorated function which will be executed with retries.
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return function(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts}/{max_retries} failed with error: {e}")
                    if attempts < max_retries:
                        time.sleep(5 * attempts)  # Exponential backoff
                    else:
                        print("All retry attempts failed.")
                        return None
        return wrapper
    return decorator
