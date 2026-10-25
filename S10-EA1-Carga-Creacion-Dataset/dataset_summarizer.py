"""Resumen legible de un DataFrame y exportación a texto UTF-8."""

from pathlib import Path

import pandas as pd


class DatasetSummarizer:
    """Recibe un DataFrame ya procesado; no consulta Hugging Face."""

    def __init__(self, dataframe: pd.DataFrame) -> None:
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Se esperaba un DataFrame de pandas.")
        self.dataframe = dataframe.copy()

    def generar_resumen(self) -> str:
        """Construye un resumen que permite reconocer los datos."""
        df = self.dataframe
        lineas = [
            "RESUMEN DEL DATASET IRIS TRANSFORMADO",
            "=" * 42,
            f"Filas: {len(df)}",
            f"Columnas: {len(df.columns)}",
            "",
            "COLUMNAS Y TIPOS DE DATOS",
            "-" * 28,
        ]

        for nombre, tipo in df.dtypes.items():
            lineas.append(f"- {nombre}: {tipo}")

        lineas.extend(["", "VALORES NULOS POR COLUMNA", "-" * 28])
        for nombre, cantidad in df.isna().sum().items():
            lineas.append(f"- {nombre}: {cantidad}")

        lineas.extend(
            [
                f"Total de valores nulos: {int(df.isna().sum().sum())}",
                f"Filas duplicadas: {int(df.duplicated().sum())}",
                "",
                "ESTADÍSTICAS DESCRIPTIVAS (COLUMNAS NUMÉRICAS)",
                "-" * 48,
            ]
        )

        numericas = df.select_dtypes(include="number")
        if numericas.empty:
            lineas.append("No hay columnas numéricas.")
        else:
            lineas.append(numericas.describe().round(2).to_string())

        if "especie" in df.columns:
            lineas.extend(
                [
                    "",
                    "CANTIDAD DE REGISTROS POR ESPECIE",
                    "-" * 33,
                    df["especie"].value_counts().to_string(),
                ]
            )

        return "\n".join(lineas) + "\n"

    def guardar_txt(self, ruta: str | Path = "resumen_iris_transformado.txt") -> Path:
        """Guarda el resumen del DataFrame recibido en un archivo .txt."""
        destino = Path(ruta)
        if destino.suffix.lower() != ".txt":
            raise ValueError("El archivo de salida debe tener extensión .txt.")
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(self.generar_resumen(), encoding="utf-8")
        return destino
