def format_duration(seconds):
    if seconds == 0:
        return "now"

    # Definir as unidades de tempo em segundos
    units = [
        ("year", 365 * 24 * 3600),
        ("day", 24 * 3600),
        ("hour", 3600),
        ("minute", 60),
        ("second", 1),
    ]
    
    # Lista para armazenar os componentes de tempo
    components = []

    # Calcular cada unidade de tempo e armazenar os resultados
    for name, unit_seconds in units:
        if seconds >= unit_seconds:
            quantity = seconds // unit_seconds
            seconds %= unit_seconds
            # Adiciona a unidade ao texto, usando plural se necessário
            components.append(f"{quantity} {name}{'s' if quantity > 1 else ''}")

    # Combinar os componentes em uma string legível
    if len(components) > 1:
        return ", ".join(components[:-1]) + " and " + components[-1]
    else:
        return components[0]
    
    print(format_duration(62))  # Saída: "1 minute and 2 seconds"
    t(format_duration(3662))  # Saída: "1 hour, 1 minute and 2 seconds"
    
