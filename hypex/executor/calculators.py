from __future__ import annotations

from typing import Any

import numpy as np
from scipy.stats import norm

from ..dataset import ABCRole, Dataset, ExperimentData, TargetRole, TreatmentRole
from ..extensions import MultitestQuantile
from ..utils import NotSuitableFieldError
from ..utils.adapter import Adapter
from .executor import Calculator


class MinSampleSize(Calculator):

    def __init__(
        self,
        grouping_role: ABCRole | None = None,
        key: Any = "",
        *,
        mde: float,
        power: float = 0.2,
        quantile_1: float | list[float] | None = None,
        quantile_2: float | list[float] | None = None,
        initial_estimate: int = 0,
        power_iteration_size: int = 3000,
        alpha: float = 0.05,
        iteration_size: int = 5000,
        equal_variance: bool = False,
        random_state: int | None = 42,
        variances: list[float] | float | None = None,
    ):
        super().__init__(key=key)
        self.grouping_role = grouping_role or TreatmentRole()

        self.mde = mde
        self.power = power
        self.quantile_1 = quantile_1
        self.quantile_2 = quantile_2
        self.initial_estimate = initial_estimate
        self.power_iteration_size = power_iteration_size
        self.alpha = alpha
        self.iteration_size = iteration_size
        self.equal_variance = equal_variance
        self.random_state = random_state
        self.variances = variances

    @property
    def search_types(self) -> list[type] | None:
        pass

    def _get_fields(self, data: Dataset) -> tuple[list[str], list[str]]:
        pass

    @staticmethod
    def _variance_by_group(
        grouping_data: list[tuple[str, Dataset]],
        target_field: str,
    ) -> list[float]:
        pass

    @classmethod
    def _inner_function(
        cls,
        *,
        num_samples: int,
        mde: float,
        variances: list[float] | float,
        power: float = 0.2,
        quantile_1: float | list[float] | None = None,
        quantile_2: float | list[float] | None = None,
        initial_estimate: int = 0,
        power_iteration_size: int = 3000,
        alpha: float = 0.05,
        iteration_size: int = 5000,
        equal_variance: bool = True,
        random_state: int | None = 42,
    ) -> int:
        pass

    def calc(self, data: Dataset) -> dict:
        pass

    def execute(self, data: ExperimentData) -> dict:
        pass
