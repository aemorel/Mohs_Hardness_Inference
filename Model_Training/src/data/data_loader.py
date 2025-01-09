import pandas as pd
import os

def load_data(filepath):
    
    # Carga el dataset desde un archivo CSV y realiza una inspección básica.
    
    # Verificar si el archivo existe en el path proporcionado
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"El archivo no existe en la ruta especificada: {filepath}")
    
    # Cargar los datos en un DataFrame
    data = pd.read_csv(filepath)
    
    # Mostrar información básica sobre el dataset cargado
    print("Cargando datos desde:", filepath)
    print("Primeras 5 filas del dataset:")
    print(data.head())
    print("\nResumen del dataset:")
    print(data.info())
    
    return data


# Ejemplo de uso
if __name__ == "__main__":
    # Ruta del archivo
    dataset_path = "data/Naturally_Occurring_Minerals.csv"
    
    # Cargar los datos
    minerals_data = load_data(dataset_path)
