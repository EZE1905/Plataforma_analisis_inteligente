import pandas as pd

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

def division_categoria(df):
    # Filtrar ingresos y gastos
    df_gastos = df[df['operacion'] == 'gasto']
    df_ingresos = df[df['operacion'] == 'ingreso']
    
    # Calcular totales x categorias
    gastos_x_categoria = df_gastos.groupby('categoria')['monto'].sum()
    ingresos_x_categoria = df_ingresos.groupby('categoria')['monto'].sum()

    # Agarrar los 5 mayores
    gastos_x_categoria = gastos_x_categoria.sort_values(ascending=False).head(5)
    ingresos_x_categoria = ingresos_x_categoria.sort_values(ascending=False).head(5)

    # Pasar a diccionario
    gastos_x_categoria = gastos_x_categoria.to_dict()
    ingresos_x_categoria = ingresos_x_categoria.to_dict()

    return gastos_x_categoria, ingresos_x_categoria

def movimientos_fecha(df):
    # Filtrar ingresos y gastos
    df_gastos = df[df['operacion'] == 'gasto']
    df_ingresos = df[df['operacion'] == 'ingreso']

    # Convertir fecha a datetime
    df_gastos['fecha'] = pd.to_datetime(df_gastos['fecha'])
    df_ingresos['fecha'] = pd.to_datetime(df_ingresos['fecha'])

    # Agrupar por mes
    df_gastos['Mes'] = df_gastos['fecha'].dt.to_period('M')
    df_ingresos['Mes'] = df_ingresos['fecha'].dt.to_period('M')

    #filtrar movimientos por mes y sumar
    df_fecha_gasto = df_gastos.groupby('Mes')['monto'].sum()
    df_fecha_ingreso = df_ingresos.groupby('Mes')['monto'].sum()

    # Convertir a string
    df_fecha_gasto.index = df_fecha_gasto.index.astype(str)
    df_fecha_ingreso.index = df_fecha_ingreso.index.astype(str)

    #pasar a diccionario
    df_fecha_gasto = df_fecha_gasto.to_dict()
    df_fecha_ingreso = df_fecha_ingreso.to_dict()

    return df_fecha_gasto, df_fecha_ingreso