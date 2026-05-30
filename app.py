from flask import Flask, render_template,redirect,request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Aquí puedes agregar la lógica para manejar el archivo subido y realizar el análisis
    archivo = request.files['file']
    try: 
        df = pd.read_csv(archivo)
        print(df.info())
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")

    return render_template('/cargando.html')

if __name__ == '__main__':
    app.run(debug=True)

