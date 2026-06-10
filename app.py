from flask import Flask, render_template,redirect,request
import pandas as pd

#importando modulos
from limpieza.limpiar import limpiar_dataset
from analisis.metricas import analizar_kpis, crear_visual, division_categoria, movimientos_fecha
from analisis.insights import insights, alerta_gastos, balance

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Obtener el archivo cargado
    archivo = request.files['file']
    
    # Guardar el archivo en la carpeta de uploads
    archivo.save('uploads/' + archivo.filename)

    try:
        # Leer el archivo
        if archivo.filename.endswith('.csv'):
            df_crudo = pd.read_csv('uploads/' + archivo.filename)
        elif archivo.filename.endswith('.xlsx') or archivo.filename.endswith('.xlsm') or archivo.filename.endswith('.xls'):
            df_crudo = pd.read_excel('uploads/' + archivo.filename) 
        else:
            error = "El archivo debe ser .csv, .xlsx, .xls o .xlsm"
            return render_template('/index.html', error=error)

        # Limpieza
        df_limpio = limpiar_dataset(df_crudo)

        # Crear df visual para el frontend
        df_visual = crear_visual(df_limpio)

        # Guardar el archivo limpio en la carpeta de uploads
        df_limpio.to_excel('uploads/limpio.xlsx', index=False)

        # Calcular los KPIs
        kpis = analizar_kpis(df_limpio)
        
        # Calcular las divisiones x categorias
        gastos_x_categoria, ingresos_x_categoria = division_categoria(df_limpio)

        # Calcular los movimientos x fecha
        df_fecha_gasto, df_fecha_ingreso = movimientos_fecha(df_limpio)

        # Calcular la categoria con mas gasto y mas ingreso
        max_gasto, max_ingreso = insights(df_limpio)

        # Calcular la alerta de gastos
        porcentaje = alerta_gastos(df_limpio)

        # Calcular el balance
        balance_mensual = balance(df_limpio)

        return render_template('index.html', kpis=kpis, df_visual=df_visual,gastos_x_categoria=gastos_x_categoria,ingresos_x_categoria=ingresos_x_categoria,df_fecha_gasto=df_fecha_gasto,df_fecha_ingreso=df_fecha_ingreso,max_gasto=max_gasto,max_ingreso=max_ingreso,porcentaje=porcentaje, balance_mensual=balance_mensual)
    
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return redirect('/')

@app.route('/exportar', methods=['POST'])
def exportar():
    # Lógica para exportar el archivo
    # Leer archivo de uploads
    df_limpio = pd.read_excel('uploads/limpio.xlsx')
    print(df_limpio.head())
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

