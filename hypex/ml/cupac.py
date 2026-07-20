from __future__ import annotations

from typing import Any, Sequence

from ..dataset.dataset import Dataset, ExperimentData
from ..dataset.roles import (
    AdditionalTargetRole,
    FeatureRole,
    PreTargetRole,
    TargetRole,
)
from ..executor import MLExecutor
from ..extensions.cupac import CupacExtension
from ..utils.adapter import Adapter
from ..utils.models import CUPAC_MODELS


class CUPACExecutor(MLExecutor):

    def __init__(
        self,
        cupac_models: str | Sequence[str] | None = None,
        key: Any = "",
        n_folds: int = 5,
        random_state: int | None = None,
    ):
        super().__init__(target_role=TargetRole(), key=key)
        self.cupac_models = cupac_models
        self.extension = CupacExtension(n_folds, random_state)

    def _validate_models(self) -> None:
        pass

    @staticmethod
    def _prepare_data(data: ExperimentData) -> dict[str, dict[str, list]]:
        pass

    @classmethod
    def _execute_inner_function(cls) -> None:
        pass

    @classmethod
    def _inner_function(cls) -> None:
        pass

    def calc(
        self, mode: str, model: str | Any, X: Dataset, Y: Dataset | None = None
    ) -> Any:
        pass

    def kfold_fit(
        self, model: str, X: Dataset, Y: Dataset
    ) -> tuple[float, dict[str, float]]:
        pass

    def fit(self, model: str, X: Dataset, Y: Dataset) -> Any:
        pass

    def predict(self, model: Any, X: Dataset) -> Dataset:
        pass

    @staticmethod
    def _agg_data_from_cupac_data(
        data: ExperimentData, cupac_data_slice: list
    ) -> Dataset:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
