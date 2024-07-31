def input_period_int(msg_desc: str, msg_info: str = None, msg_error: str = None) -> list:
    while True:
        try:
            if msg_info is not None:
                print(f"INFO - {msg_info}")
            dias = input(msg_desc)
            dias_int = int(dias.strip())
            if dias_int == 0:
                break
        except Exception as e:
            if msg_error is not None:
                print(msg_error)
        else:
            return dias_int
