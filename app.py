from flask import Flask, render_template,redirect,request
import pandas as pd

#importando modulos
from limpieza.limpiar import limpiar_dataset
from analisis.metricas import analizar_kpis, crear_visual

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Obtener el archivo cargado
    archivo = request.files['file']
    
    try:
        # Leer el archivo CSV y limpiar los datos 
        df_crudo = pd.read_csv(archivo)
        df_limpio = limpiar_dataset(df_crudo)

        # Crear df visual para el frontend
        df_visual = crear_visual(df_limpio)

        # Calcular los KPIs
        kpis = analizar_kpis(df_limpio)
        return render_template('index.html', kpis=kpis, df_visual=df_visual)
    
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

