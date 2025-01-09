from xgboost import XGBRegressor

def train_model(X_train, y_train, params=None):
    """
    Entrena un modelo de XGBoost con parámetros predeterminados o personalizados.
    """
    # Parámetros
    if params is None:
        params = {
            "n_estimators": 100,  # Número de árboles
            "max_depth": 6,       # Profundidad máxima de los árboles
            "learning_rate": 0.1, # Tasa de aprendizaje
            "random_state": 42    # Semilla para reproducibilidad
        }
    
    # Instanciar el modelo XGBoost con los parámetros dados
    model = XGBRegressor(**params)
    
    # Entrenar el modelo
    print("\nEntrenando el modelo...")
    model.fit(X_train, y_train)
    print("Entrenamiento completado.")
    
    return model
