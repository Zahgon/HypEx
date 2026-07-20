from __future__ import annotations

from copy import deepcopy
from typing import Any

from ..comparators import TTest, UTest
from ..dataset import Dataset, ExperimentData, StatisticRole, TargetRole, TreatmentRole
from ..experiments.base import Executor
from ..extensions.statsmodels import MultiTest, MultitestQuantile
from ..utils import (
    ID_SPLIT_SYMBOL,
    NAME_BORDER_SYMBOL,
    ABNTestMethodsEnum,
    BackendsEnum,
    ExperimentDataEnum,
)


class ABAnalyzer(Executor):
    def __init__(
        self,
        multitest_method: ABNTestMethodsEnum | None = None,
        alpha: float = 0.05,
        equal_variance: bool = True,
        quantiles: float | list[float] | None = None,
        iteration_size: int = 20000,
        random_state: int | None = None,
        key: Any = "",
    ):
        self.multitest_method = multitest_method
        self.alpha = alpha
        self.equal_variance = equal_variance
        self.quantiles = quantiles
        self.iteration_size = iteration_size
        self.random_state = random_state
        super().__init__(key)

    def _set_value(self, data: ExperimentData, value, key=None) -> ExperimentData:
        pass

    def execute_multitest(self, data: ExperimentData, p_values: Dataset, **kwargs):
        pass

    def _add_pvalues(self, multitest_pvalues, value, field):
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
