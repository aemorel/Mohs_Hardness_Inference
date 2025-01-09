from sklearn.model_selection import train_test_split

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Divide los datos en conjuntos de entrenamiento y prueba.
    """
    # Dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # Imprimir tamaños de los conjuntos
    print(f"Conjunto de entrenamiento: X_train={X_train.shape}, y_train={y_train.shape}")
    print(f"Conjunto de prueba: X_test={X_test.shape}, y_test={y_test.shape}")
    
    return X_train, X_test, y_train, y_test