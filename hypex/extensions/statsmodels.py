from __future__ import annotations

import numpy as np
from scipy.stats import norm  # type: ignore
from statsmodels.stats.multitest import multipletests  # type: ignore

from ..dataset import Dataset, DatasetAdapter, StatisticRole
from ..utils import ID_SPLIT_SYMBOL, ABNTestMethodsEnum
from .abstract import Extension


class MultiTest(Extension):
    def __init__(self, method: ABNTestMethodsEnum, alpha: float = 0.05):
        self.method = method
        self.alpha = alpha
        super().__init__()

    def _calc_pandas(self, data: Dataset, **kwargs):
        pass


class MultitestQuantile(Extension):
    def __init__(
        self,
        alpha: float = 0.05,
        iteration_size: int = 20000,
        equal_variance: bool = True,
        random_state: int | None = None,
    ):
        self.alpha = alpha
        self.iteration_size = iteration_size
        self.equal_variance = equal_variance
        self.random_state = random_state
        super().__init__()

    def _calc_pandas(self, data: Dataset, **kwargs):
        pass

    def quantile_of_marginal_distribution(
        self,
        num_samples: int,
        quantile_level: float,
        variances: list[float] | None = None,
    ) -> list[float]:
        pass
