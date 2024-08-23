import time

def countdown_timer(wait_seconds: int, msg_wait=""):
    """Countdown by seconds"""
    for i in range(wait_seconds, 0, -1):
        print(f"{msg_wait} {i} second(s) ...", end='\r')
        time.sleep(1)  # Waits for 1 second
        

def execute_with_retries(max_retries: int, function, *args, **kwargs):
    """
    Executes a function with a specified number of retries in case of failure.
    
    Parameters:
        max_retries (int): Maximum number of retry attempts.
        function (callable): Function to be executed.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.
    
    Returns:
        The result of the function if successful, None otherwise.
    """
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
