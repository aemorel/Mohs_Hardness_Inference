import joblib
import os

def save_model(model, file_path):
    """
    Guarda el modelo entrenado en un archivo.
    """
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Guardar el modelo
    joblib.dump(model, file_path)
    print(f"Modelo guardado en: {file_path}")