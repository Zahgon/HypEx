from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

import numpy as np
from scipy.stats import norm

from ..dataset import ABCRole, Dataset, ExperimentData, TreatmentRole, TargetRole
from ..utils import ExperimentDataEnum
from .comparators import Comparator


class PowerTesting(Comparator, ABC):
    def __init__(
        self,
        grouping_role: ABCRole | None = None,
        significance: float = 0.95,
        power: float = 0.8,
        key: Any = "",
    ):
        super().__init__(
            compare_by="groups",
            grouping_role=grouping_role,
            key=key,
        )
        self.significance = significance
        self.power = power

    @classmethod
    @abstractmethod
    def _inner_function(
        cls,
        data: Dataset,
        test_data: Dataset | None = None,
        significance: float = 0.95,
        power: float = 0.8,
        **kwargs,
    ) -> float:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass


class MDEBySize(PowerTesting):
    def __init__(
        self,
        grouping_role: ABCRole | None = None,
        significance: float = 0.95,
        power: float = 0.8,
        key: Any = "",
    ):
        super().__init__(
            grouping_role=grouping_role or TreatmentRole(),
            key=key,
        )
        self.significance = significance
        self.power = power

    def _set_value(
        self, data: ExperimentData, value: Dataset | None = None, key: Any = None
    ) -> ExperimentData:
        pass

    def calc(
        self,
        data: Dataset | None = None,
        compare_by: (
            Literal["groups", "columns", "columns_in_groups", "cross", "matched_pairs"]
            | None
        ) = "groups",
        **kwargs,
    ) -> dict:
        pass

    @classmethod
    def _inner_function(
        cls,
        data: Dataset,
        test_data: Dataset | None = None,
        significance: float = 0.95,
        power: float = 0.8,
        **kwargs,
    ) -> float:
        pass




