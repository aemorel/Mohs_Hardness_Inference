from data.data_loader import load_data
from data.data_processor import preprocess_data
from data.data_splitter import split_data
from model.trainer import train_model
from model.evaluator import evaluate_model
from model.saver import save_model
import os

def main():
    # Ruta al dataset
    dataset_path = "data/Naturally_Occurring_Minerals.csv"
    model_save_path = "models/xgboost_model.joblib"
    
    # 1. Cargar los datos
    data = load_data(dataset_path)
    
    # 2. Preprocesar los datos
    target_column = "Hardness"
    X_scaled, y = preprocess_data(data, target_column)
    
    # 3. Dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = split_data(X_scaled, y)
    
    # 4. Entrenar modelo XGBoost
    model = train_model(X_train, y_train)
    
    # 5. Guardar el modelo entrenado
    save_model(model, model_save_path)
    
    # 6. Verificar que el modelo se guardó
    if os.path.exists(model_save_path):
        print(f"Modelo guardado exitosamente en: {model_save_path}")
    else:
        print("Error: El modelo no se guardó correctamente.")
    
    # 7. Evaluar el modelo
    metrics = evaluate_model(model, X_test, y_test)

    # 8. Mostrar métricas finales
    print("\n===== Métricas Finales =====")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")

if __name__ == "__main__":
    main()
