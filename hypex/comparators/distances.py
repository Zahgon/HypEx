from __future__ import annotations

from copy import deepcopy
from typing import Any, Sequence

import numpy as np

from ..dataset import (
    ABCRole,
    AdditionalFeatureRole,
    Dataset,
    ExperimentData,
    FeatureRole,
    GroupingRole,
    TargetRole,
)
from ..executor import Calculator
from ..extensions.scipy_linalg import CholeskyExtension, InverseExtension
from ..utils import ExperimentDataEnum, NotSuitableFieldError
from ..utils.adapter import Adapter


class MahalanobisDistance(Calculator):
    def __init__(
        self,
        grouping_role: ABCRole | None = None,
        key: Any = "",
        weights: dict[str, float] | None = None,
    ):
        super().__init__(key=key)
        self.grouping_role = grouping_role or GroupingRole()
        self.weights = weights

    @classmethod
    def _execute_inner_function(
        cls,
        grouping_data,
        target_fields: list[str] | None = None,
        **kwargs,
    ) -> dict:
        pass

    def _set_value(
        self, data: ExperimentData, value: dict | None = None, key: Any = None
    ) -> ExperimentData:
        pass

    def _get_fields(self, data: ExperimentData):
        pass

    @property
    def search_types(self) -> list[type] | None:
        pass

    @classmethod
    def _inner_function(
        cls,
        data: Dataset,
        test_data: Dataset | None = None,
        weights: dict[str, float] | None = None,
        **kwargs,
    ):
        pass

    @classmethod
    def calc(
        cls,
        data: Dataset,
        group_field: Sequence[str] | str | None = None,
        grouping_data: list[tuple[str, Dataset]] | None = None,
        target_fields: str | list[str] | None = None,
        weights: dict[str, float] | None = None,
        **kwargs,
    ) -> dict:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
