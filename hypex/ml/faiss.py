from __future__ import annotations

from typing import Any, Literal
from warnings import warn

from ..comparators.distances import MahalanobisDistance
from ..dataset import (
    ABCRole,
    AdditionalMatchingRole,
    Dataset,
    ExperimentData,
    FeatureRole,
)
from ..executor import MLExecutor
from ..extensions.faiss import FaissExtension
from ..utils import ExperimentDataEnum
from ..utils.errors import PairsNotFoundError


class FaissNearestNeighbors(MLExecutor):
    def __init__(
        self,
        n_neighbors: int = 1,
        two_sides: bool = False,
        test_pairs: bool = False,
        grouping_role: ABCRole | None = None,
        key: Any = "",
        faiss_mode: Literal["base", "fast", "auto"] = "auto",
    ):
        self.n_neighbors = n_neighbors
        self.two_sides = two_sides
        self.test_pairs = test_pairs
        self.faiss_mode = faiss_mode
        super().__init__(
            grouping_role=grouping_role,
            target_role=FeatureRole(),
            key=key,
        )

    @classmethod
    def _set_global_match_indexes(
        cls, local_indexes: Dataset, data: tuple(str, Dataset)
    ) -> list[int, list[int]]:
        pass

    @classmethod
    def _execute_inner_function(
        cls,
        grouping_data,
        target_field: str | None = None,
        n_neighbors: int | None = None,
        two_sides: bool | None = None,
        test_pairs: bool | None = None,
        faiss_mode: Literal["base", "fast", "auto"] = "auto",
        **kwargs,
    ) -> dict:
        pass

    @classmethod
    def _inner_function(
        cls,
        data: Dataset,
        test_data: Dataset | None = None,
        target_data: Dataset | None = None,
        n_neighbors: int | None = None,
        faiss_mode: Literal["base", "fast", "auto"] = "auto",
        **kwargs,
    ) -> Any:
        pass

    def fit(self, X: Dataset, Y: Dataset | None = None) -> MLExecutor:
        pass

    def predict(self, X: Dataset) -> Dataset:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
