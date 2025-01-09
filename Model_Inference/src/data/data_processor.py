from sklearn.preprocessing import StandardScaler

def preprocess_data(data):
    """
    Preprocesa el dataset:
    - Elimina columnas irrelevantes.
    - Escala características numéricas.
    """
    # 1. Eliminar columnas irrelevantes si existen
    if 'Unnamed: 0' in data.columns:
        data = data.drop(columns=['Unnamed: 0','Formula', 'Crystal structure', 'Hardness (Mohs)'])
        print("Columnas")
    
    # 2. Seleccionar características numéricas para escalar
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    print(f"Columnas numéricas seleccionadas para escalar: {list(numeric_columns)}")
    
    # 3. Escalar características numéricas
    scaler = StandardScaler()
    data_scaled = data.copy()
    data_scaled[numeric_columns] = scaler.fit_transform(data[numeric_columns])
    print("Datos escalados correctamente.")
    
    return data_scaled