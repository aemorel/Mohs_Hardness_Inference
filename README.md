# **Sobre el Dataset**
**Propiedades de Minerales**

El dataset contiene información sobre minerales y sus propiedades químicas, físicas y atómicas. 
El objetivo principal es **predecir la dureza Mohs** (`Hardness`) de los minerales en función de sus características. 

Este análisis se enfoca en entender la estructura, calidad y posibles desafíos del dataset, sirviendo como base para un modelo predictivo.

## **Descripción de las Columnas**

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

