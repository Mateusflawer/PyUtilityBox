def extrat_pattern_content(string, string_padrao, inicio_padrao='[', fim_padrao=']', up=False) -> str:
    """
    Busca um padrão específico dentro de uma string e retorna o conteúdo encontrado entre os delimitadores definidos.
    
    Parameters:
        string (str): A string onde a busca será realizada.
        string_padrao (str): O padrão que precede o conteúdo desejado.
        inicio_padrao (str): O caractere que marca o início do conteúdo desejado. Padrão é '['.
        fim_padrao (str): O caractere que marca o fim do conteúdo desejado. Padrão é ']'.
        up (bool): Se True, retorna o conteúdo em maiúsculas. Padrão é True.
    
    Returns:
        str: O conteúdo encontrado entre os delimitadores, ou None se não for encontrado.
    """
    # Verifica se os parâmetros são válidos
    if not string or not string_padrao:
        return None

    # Busca a posição do padrão na string
    start_idx = string.find(string_padrao)
    if start_idx == -1:
        return None

    start_idx += len(string_padrao)
    start_delim_idx = string.find(inicio_padrao, start_idx)

    if start_delim_idx == -1:
        return None

    end_delim_idx = string.find(fim_padrao, start_delim_idx + 1)

    if end_delim_idx == -1:
        return None

    conteudo = string[start_delim_idx + 1:end_delim_idx].strip()

    if up:
        return conteudo.upper()

    return conteudo
