# S10 – EA1: Carga y creación de dataset

**Estudiante:** José David Osorio Gallego  
**Curso:** Actividad S10, Evidencia de Aprendizaje 1  
**Año:** 2026

## ¿Qué hice?

En esta actividad quise practicar un flujo sencillo pero que pueda volver a usar: obtener un dataset desde Hugging Face, trabajarlo con pandas y generar un archivo de texto para conocer sus características.

Elegí [scikit-learn/iris](https://huggingface.co/datasets/scikit-learn/iris), en su partición `train`, porque sus columnas son fáciles de interpretar: contiene medidas de sépalos y pétalos de tres especies de flores.

## Archivos

| Archivo | Función |
| --- | --- |
| `hf_dataset_loader.py` | Clase `HFDatasetLoader`: descarga el dataset y devuelve un DataFrame. |
| `dataset_summarizer.py` | Clase `DatasetSummarizer`: revisa filas, columnas, tipos, nulos y estadísticas, y guarda el TXT. |
| `S10_EA1_iris.ipynb` | Notebook con la carga, cinco transformaciones, resultados visibles y comprobaciones. |
| `resumen_iris_transformado.txt` | Resumen generado a partir del **DataFrame final**, no del original. |
| `requirements.txt` | Dependencias de Python. |
| `tests/test_clases.py` | Pruebas de las dos clases y del archivo de salida. |

## Las cinco transformaciones

1. **Eliminar `Id`:** no es una medida de la flor.
2. **Renombrar las columnas:** usar nombres más fáciles de leer en español.
3. **Filtrar:** conservar solamente filas cuyo largo de pétalo sea mayor que 1,5 cm.
4. **Agregar una columna:** multiplicar largo por ancho del pétalo para calcular una medida rectangular aproximada en cm².
5. **Ordenar:** mostrar primero las flores con mayor área aproximada del pétalo.

Mostrar `head()` no se considera transformación: solo sirve para revisar las primeras filas.

**Resultado revisado:** 150 filas y 6 columnas al inicio; después de las transformaciones, 113 filas y 6 columnas. Las especies finales son Iris-virginica (50), Iris-versicolor (50) e Iris-setosa (13). Todas las columnas tienen 0 valores nulos. El resumen también informa una fila duplicada, que se conserva.

## Cómo ejecutarlo

Desde una terminal situada en esta carpeta, con Python 3.10 o más reciente:

```bash
python -m venv .venv
```

En Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
jupyter notebook S10_EA1_iris.ipynb
```

En Linux o macOS:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter notebook S10_EA1_iris.ipynb
```

En Jupyter, elegir **Run All / Ejecutar todas**. Se necesita conexión a Internet en la primera carga desde Hugging Face. La celda del resumen vuelve a escribir `resumen_iris_transformado.txt` para mantenerlo sincronizado con el DataFrame que se acaba de procesar.

Para ejecutar las pruebas:

```bash
python -m unittest discover -s tests -v
```

## ¿Qué comprobé?

- La carga se hace dentro de una clase que recibe el identificador y el split.
- El notebook importa las dos clases desde archivos Python independientes.
- Se muestran resultados después de cada transformación.
- La segunda clase recibe el DataFrame **ya transformado**.
- El TXT incluye nombres y tipos de columnas, cantidad de filas, nulos y estadísticas.
- Las afirmaciones `assert` al final comprueban el tamaño, el filtro, el orden y el contenido del TXT.

## Nota sobre los datos

El filtro reduce considerablemente los registros de Iris-setosa; por eso el resultado no conserva la distribución original de especies. La medida de área calculada es solo una aproximación rectangular, no el área geométrica real del pétalo.

Fuente del dataset: [Hugging Face – scikit-learn/iris](https://huggingface.co/datasets/scikit-learn/iris). El conjunto indica licencia CC0-1.0.
