from data.inference import run_inference  # Importación directa desde el mismo nivel


def main():
    # Configurar rutas relativas
    dataset_path = r"C:\Users\Andy\Documents\Andrea_Echague_Mohs_Hardness\Model_Inference\data\Synthetic_Single_Crystals.csv"  # Ruta relativa al archivo de datos
    model_path = r'C:\Users\Andy\Documents\Andrea_Echague_Mohs_Hardness\Model_Inference\models\xgboost_model.joblib'          # Ruta relativa al modelo guardado
    output_path = r'C:\Users\Andy\Documents\Andrea_Echague_Mohs_Hardness\Model_Inference\models\Mohs_Inference.csv'           # Ruta relativa para guardar resultados

    # Ejecutar inferencia
    print("Iniciando flujo de preprocesamiento e inferencia...")
    run_inference(dataset_path, model_path, output_path)

if __name__ == "__main__":
    main()