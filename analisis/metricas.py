def analizar_kpis(df):
    # Filtrar ingresos y gastos
    df_ingresos = df[df['operacion'] == 'ingreso']
    df_gastos = df[df['operacion'] == 'gasto']

    # Calcular totales
    total_ingresos = df_ingresos['monto'].sum()
    total_gastos = df_gastos['monto'].sum()
    balance = total_ingresos - total_gastos

    #Calcular totales de operaciones
    operaciones_ingresos = len(df_ingresos)
    operaciones_gastos = len(df_gastos)
    operaciones_totales = operaciones_ingresos + operaciones_gastos

    # Guardar totales sin formato para cálculos futuros
    total_ingresos_raw = df_ingresos['monto'].sum()
    total_gastos_raw = df_gastos['monto'].sum()
    balance_raw = total_ingresos_raw - total_gastos_raw

    # Formatear totales a formato de moneda
    total_ingresos = f"${total_ingresos:,}".replace(',', '.')
    total_gastos = f"${total_gastos:,}".replace(',', '.')
    balance = f"${balance:,}".replace(',', '.')

    # Crear diccionario de KPIs
    kpis = {
        'total_ingresos': total_ingresos,
        'total_gastos': total_gastos,
        'balance': balance,
        'total_ingresos_raw': total_ingresos_raw,
        'total_gastos_raw': total_gastos_raw,
        'balance_raw': balance_raw,
        'operaciones_totales': operaciones_totales,
        'operaciones_ingresos': operaciones_ingresos,
        'operaciones_gastos': operaciones_gastos
    }
    return kpis

def crear_visual(df_limpio):
    df_visual = df_limpio[['fecha','operacion','categoria','descripcion','monto']].copy()
    df_visual['monto'] = df_visual['monto'].apply(lambda x: f"${x:,}".replace(',', '.'))
    return df_visual.to_html(classes='table', index=False)