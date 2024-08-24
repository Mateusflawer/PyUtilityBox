def input_period_int(msg_desc: str, msg_info: str = None, msg_error: str = "Entrada inválida. Tente novamente.") -> int:
    """
    Solicita a entrada de um número inteiro positivo do usuário e retorna esse valor.
    
    Parameters:
        msg_desc (str): Mensagem descritiva para solicitar a entrada.
        msg_info (str, optional): Mensagem de informação a ser exibida antes da entrada. Padrão é None.
        msg_error (str, optional): Mensagem de erro a ser exibida em caso de entrada inválida. Padrão é "Entrada inválida. Tente novamente."
    
    Returns:
        int: O número inteiro fornecido pelo usuário.
    """
    while True:
        if msg_info:
            print(f"INFO - {msg_info}")
        
        dias = input(msg_desc).strip()
        
        try:
            dias_int = int(dias)
            if dias_int == 0:
                print("INFO - Valor zero inserido. Saindo.")
                return 0
            return dias_int
        except ValueError:
            print(f"ERROR - {msg_error}")
