from analisis.metricas import analizar_kpis, movimientos_fecha
# Calcular la categoria que mas gasta/ingresa 

def insights(df):
    # Filtrar ingresos y gastos
    df_gastos = df[df['operacion'] == 'gasto']
    df_ingresos = df[df['operacion'] == 'ingreso']
    
    # Calcular totales x categorias
    gastos_x_categoria = df_gastos.groupby('categoria')['monto'].sum()
    ingresos_x_categoria = df_ingresos.groupby('categoria')['monto'].sum()

    # Agarrar los maximos de gasto y ingreso
    max_gasto = gastos_x_categoria.sort_values(ascending=False).head(1)
    max_ingreso = ingresos_x_categoria.sort_values(ascending=False).head(1)

    # Pasar a escritura
    max_gasto = max_gasto.index[0].capitalize() + " : $" + max_gasto.values[0].astype(str)
    max_ingreso = max_ingreso.index[0].capitalize() + " : $" + max_ingreso.values[0].astype(str)

    return max_gasto, max_ingreso

def alerta_gastos(df):
    kpis = analizar_kpis(df)
    total_gastos = int(kpis['total_gastos_raw'])
    total_ingresos = int(kpis['total_ingresos_raw'])
    porcentaje = total_gastos / total_ingresos * 100
    porcentaje = round(porcentaje, 2)

    return porcentaje

def balance(df):
    df_gastos_mes, df_ingresos_mes = movimientos_fecha(df)
    balance = 0

    for mes in df_gastos_mes.keys():
        gasto_mes = df_gastos_mes[mes]
        ingreso_mes = df_ingresos_mes[mes]
        balance += ingreso_mes - gasto_mes
    
    cantidad_meses = len(df_gastos_mes)
    promedio_balance = balance / cantidad_meses
    promedio_balance = f"{ promedio_balance:,}".replace(',', '.')
    return promedio_balance
        

