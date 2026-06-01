def analizar_kpis(df):
    # Filtrar ingresos y gastos
    df_ingresos = df[df['operacion'] == 'ingreso']
    df_gastos = df[df['operacion'] == 'gasto']

    # Calcular totales
    total_ingresos = df_ingresos['monto'].sum()
    total_gastos = df_gastos['monto'].sum()
    balance = total_ingresos - total_gastos
    
    # Formatear totales a formato de moneda
    total_ingresos = f"${total_ingresos:,}".replace(',', '.')
    total_gastos = f"${total_gastos:,}".replace(',', '.')
    balance = f"${balance:,}".replace(',', '.')

    # Crear diccionario de KPIs
    kpis = {
        'total_ingresos': total_ingresos,
        'total_gastos': total_gastos,
        'balance': balance
    }
    return kpis