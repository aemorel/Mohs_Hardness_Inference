# **Determinación de la dureza de Minerales Sintéticos**

Este proyecto implementa un pipeline de Machine Learning para predecir la dureza de cristales sintéticos, utilizando modelos basados en características numéricas extraídas de un dataset de minerales naturales.

El dataset contiene información sobre minerales y sus propiedades químicas, físicas y atómicas. 
El objetivo principal es **predecir la dureza Mohs** (`Hardness`) de los minerales en función de sus características. 

Este análisis se enfoca en entender la estructura, calidad y posibles desafíos del dataset, sirviendo como base para un modelo predictivo.

### **Descripción de las Columnas**

A continuación, se describen las columnas presentes en el dataset:

| Columna                     | Tipo         | Descripción                                                                                     |
|-----------------------------|--------------|-------------------------------------------------------------------------------------------------|
| `Unnamed: 0`               | Numérica     | Índice o identificador de la fila.                                                             |
| `Hardness`                 | Numérica     | Dureza Mohs del mineral, **variable objetivo** del modelo.                                     |
| `allelectrons_Total`       | Numérica     | Número total de electrones en los elementos que componen el mineral.                          |
| `density_Total`            | Numérica     | Densidad total calculada para el mineral.                                                      |
| `allelectrons_Average`     | Numérica     | Promedio del número de electrones en los elementos que componen el mineral.                   |
| `val_e_Average`            | Numérica     | Promedio del número de electrones de valencia.                                                 |
| `atomicweight_Average`     | Numérica     | Promedio del peso atómico de los elementos del mineral.                                        |
| `ionenergy_Average`        | Numérica     | Promedio de la energía de ionización de los elementos en estado neutral.                       |
| `el_neg_chi_Average`       | Numérica     | Electronegatividad promedio de los elementos del mineral.                                      |
| `R_vdw_element_Average`    | Numérica     | Promedio del radio de Van der Waals de los elementos.                                          |
| `R_cov_element_Average`    | Numérica     | Promedio del radio covalente de los elementos.                                                 |
| `zaratio_Average`          | Numérica     | Promedio de la relación carga/radio de los elementos.                                          |
| `density_Average`          | Numérica     | Promedio de la densidad de los elementos que componen el mineral.                              |
---

### **Descripción del Proyecto**

El objetivo es automatizar el proceso de clasificación de minerales basándonos en su dureza, una característica crítica para su uso industrial. Utilizando un modelo de **XGBoost**, el pipeline incluye:
1. Preprocesamiento de datos.
2. Entrenamiento del modelo.
3. Evaluación del modelo.
4. Predicciones en datos nuevos (inferencia).

El proyecto está diseñado para ser modular, fácil de usar y adaptado para integrarse en flujos de trabajo industriales.

### **Estructura del Proyecto**
```
Model_Inference/
├── data/
│   ├── Synthetic_Single_Crystals.csv   # Datos de prueba para inferencia
│   ├── Naturally_Occurring_Minerals.csv # Dataset para entrenamiento
├── models/
│   ├── xgboost_model.joblib           # Modelo entrenado
├── src/
│   ├── data/
│   │   ├── data_processor.py          # Funciones de preprocesamiento
│   ├── inference.py                   # Pipeline de inferencia
│   ├── train_main.py                  # Pipeline de entrenamiento
│   ├── main.py                        # Script principal para inferencia
├── requirements.txt                   # Dependencias necesarias
├── Dockerfile                         # Configuración para Docker
└── README.md                          # Este archivo
```

### **Requisitos**
1. **Python 3.8 o superior.**
2. Instalar las dependencias listadas en `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
   - `pandas`
   - `scikit-learn`
   - `xgboost`
   - `joblib`

3. Tener Docker instalado si planeas usar contenedores.

### **Cómo ejecutar el proyecto**

**1. Entrenamiento del modelo**
Ejecuta el pipeline de entrenamiento para generar el modelo `xgboost_model.joblib`:
```bash
python src/train_main.py
```

Esto realizará:
1. Carga y preprocesamiento del dataset `Naturally_Occurring_Minerals.csv`.
2. División en datos de entrenamiento y prueba.
3. Entrenamiento del modelo XGBoost.
4. Evaluación del modelo en el conjunto de prueba.
5. Guardado del modelo en `models/`.

**2. Inferencia**
Ejecuta el pipeline de inferencia para generar predicciones:
```bash
python src/main.py
```

Esto realizará:
1. Carga del dataset `Synthetic_Single_Crystals.csv`.
2. Preprocesamiento del dataset.
3. Carga del modelo `xgboost_model.joblib`.
4. Generación de predicciones.
5. Guardado de las predicciones en `data/Inference_Results.csv`.

### **Uso con Docker**
**1. Construir la imagen de Docker:**
```bash
docker build -t model_training .
```

**2. Entrenar el modelo dentro del contenedor:**
```bash
docker run model_training
```

**3. Ejecutar inferencia dentro del contenedor:**
Modifica el `CMD` en el `Dockerfile` para ejecutar `src/main.py` si es necesario.

**Pruebas unitarias**
El proyecto incluye pruebas unitarias para las funciones clave del pipeline. Para ejecutarlas:
1. Instala `pytest`:
   ```bash
   pip install pytest
   ```
2. Ejecuta los tests:
   ```bash
   pytest tests/
   ```
