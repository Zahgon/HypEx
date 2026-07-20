from __future__ import annotations

from typing import Literal

import faiss  # type: ignore
import numpy as np
import pandas as pd  # type: ignore

from ..dataset import AdditionalMatchingRole, Dataset
from .abstract import MLExtension


class FaissExtension(MLExtension):
    def __init__(
        self, n_neighbors: int = 1, faiss_mode: Literal["base", "fast", "auto"] = "auto"
    ):
        self.n_neighbors = n_neighbors
        self.faiss_mode = faiss_mode
        self.index = None
        super().__init__()

    @staticmethod
    def _prepare_indexes(index: np.ndarray, dist: np.ndarray, k: int):
        pass

    def _predict(self, data: Dataset, test_data: Dataset, X: np.ndarray) -> pd.Series:
        pass

    def _calc_pandas(
        self,
        data: Dataset,
        test_data: Dataset | None = None,
        mode: Literal["auto", "fit", "predict"] | None = None,
        **kwargs,
    ):
        pass

    def fit(self, X: Dataset, Y: Dataset | None = None, **kwargs):
        pass

    def predict(self, X: Dataset, **kwargs) -> Dataset:
        pass
