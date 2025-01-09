import pandas as pd
from joblib import load
from data.data_processor import preprocess_data

def run_inference(dataset_path, model_path, output_path):
    """
    Ejecuta el proceso de inferencia dado un dataset, un modelo entrenado y la ruta de salida.
    """
    # 1. Cargar los datos
    print("Cargando datos de inferencia...")
    data = pd.read_csv(dataset_path)
    print("Datos cargados correctamente.")

    # 2. Preprocesar los datos
    print("Preprocesando datos de inferencia...")
    X_scaled = preprocess_data(data)
    print("Datos preprocesados correctamente.")

    # 3. Cargar el modelo
    print(f"Cargando modelo desde {model_path}...")
    model = load(model_path)
    print("Modelo cargado correctamente.")

    # 4. Realizar predicciones
    print("Realizando predicciones...")
    predictions = model.predict(X_scaled)
    print("Predicciones completadas.")

    # 5. Guardar resultados
    data['Predictions'] = predictions
    data.to_csv(output_path, index=False)
    print(f"Resultados guardados en: {output_path}")
