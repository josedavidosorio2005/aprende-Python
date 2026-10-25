"""Carga de conjuntos de datos de Hugging Face en formato pandas."""

import pandas as pd
from datasets import load_dataset


class HFDatasetLoader:
    """Obtiene un split de Hugging Face y lo convierte en DataFrame."""

    def __init__(self, dataset_id: str, split: str = "train") -> None:
        if not isinstance(dataset_id, str) or not dataset_id.strip():
            raise ValueError("El identificador del dataset no puede estar vacío.")
        if not isinstance(split, str) or not split.strip():
            raise ValueError("El split debe ser un texto no vacío.")

        self.dataset_id = dataset_id.strip()
        self.split = split.strip()

    def cargar(self) -> pd.DataFrame:
        """Descarga el dataset y devuelve una copia independiente en pandas."""
        try:
            dataset = load_dataset(self.dataset_id, split=self.split)
        except Exception as error:
            raise RuntimeError(
                f"No fue posible cargar '{self.dataset_id}' (split '{self.split}'). "
                "Revisa el nombre, la conexión y el split disponible."
            ) from error

        dataframe = dataset.to_pandas()
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("Hugging Face no devolvió un DataFrame de pandas.")
        return dataframe.copy()
