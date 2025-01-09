from sklearn.preprocessing import StandardScaler

def preprocess_data(data, target_column):
    """
    Preprocesa el dataset:
    - Elimina columnas irrelevantes.
    - Escala características numéricas.
    
    """
    # 1. Eliminar columnas irrelevantes
    if 'Unnamed: 0' in data.columns:
        data = data.drop(columns=['Unnamed: 0'])
    
    # 2. Separar características y objetivo
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    # 3. Escalar características numéricas
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y