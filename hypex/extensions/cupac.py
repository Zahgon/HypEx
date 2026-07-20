from __future__ import annotations

from typing import Any, Literal

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.model_selection import KFold

from ..dataset import AdditionalTargetRole, Dataset
from ..utils.models import CUPAC_MODELS
from .abstract import MLExtension


class CupacExtension(MLExtension):

    def __init__(
        self,
        n_folds: int = 5,
        random_state: int | None = None,
    ):
        super().__init__()
        self.n_folds = n_folds
        self.random_state = random_state

    def _calc_pandas(
        self,
        data: Dataset,
        mode: Literal["kfold_fit", "fit", "predict"],
        model: str | Any,
        Y: Dataset | None = None,
        **kwargs,
    ) -> Any:
        pass

    def fit(self, model: str, X: Dataset, Y: Dataset) -> Any:
        pass

    def predict(self, model: Any, X: Dataset) -> Dataset:
        pass

    def _kfold_fit_pandas(
        self, model: str, X: Dataset, Y: Dataset
    ) -> tuple[float, dict[str, float]]:
        pass

    def _fit_pandas(self, model: str, X: Dataset, Y: Dataset) -> Any:
        pass

    def _predict_pandas(self, model: Any, X: Dataset) -> Dataset:
        pass

    @staticmethod
    def _extract_fold_importances(
        model: Any, model_name: str, feature_names: list[str]
    ) -> dict[str, float]:
        pass

    @staticmethod
    def _calculate_variance_reduction(y_original, y_adjusted) -> float:
        pass
