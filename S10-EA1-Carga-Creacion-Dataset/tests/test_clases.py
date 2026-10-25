"""Pruebas breves para las dos clases de la actividad S10."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import pandas as pd

from dataset_summarizer import DatasetSummarizer
from hf_dataset_loader import HFDatasetLoader


class TestHFDatasetLoader(unittest.TestCase):
    def test_devuelve_dataframe_y_respeta_split(self):
        original = pd.DataFrame({"flor": ["iris"], "medida": [2.5]})
        dataset_simulado = Mock()
        dataset_simulado.to_pandas.return_value = original

        with patch("hf_dataset_loader.load_dataset", return_value=dataset_simulado) as descargar:
            resultado = HFDatasetLoader("autor/dataset", "test").cargar()

        descargar.assert_called_once_with("autor/dataset", split="test")
        self.assertIsInstance(resultado, pd.DataFrame)
        pd.testing.assert_frame_equal(resultado, original)
        self.assertIsNot(resultado, original)

    def test_identificador_vacio(self):
        with self.assertRaises(ValueError):
            HFDatasetLoader(" ")


class TestDatasetSummarizer(unittest.TestCase):
    def test_resume_y_guarda_el_dataframe_recibido(self):
        transformado = pd.DataFrame(
            {"especie": ["Iris-setosa", "Iris-setosa"], "area": [1.5, None]}
        )
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "resumen.txt"
            salida = DatasetSummarizer(transformado).guardar_txt(ruta)
            contenido = salida.read_text(encoding="utf-8")

        self.assertEqual(salida, ruta)
        self.assertIn("Filas: 2", contenido)
        self.assertIn("Columnas: 2", contenido)
        self.assertIn("- area: 1", contenido)
        self.assertIn("Iris-setosa", contenido)

    def test_rechaza_entrada_que_no_sea_dataframe(self):
        with self.assertRaises(TypeError):
            DatasetSummarizer([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
