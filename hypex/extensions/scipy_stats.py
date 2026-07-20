from __future__ import annotations

import warnings
from typing import Callable

from scipy.stats import (  # type: ignore
    chi2_contingency,
    ks_2samp,
    mannwhitneyu,
    norm,
    ttest_ind,
)

from ..dataset import Dataset, DatasetAdapter, StatisticRole
from .abstract import CompareExtension


class StatTest(CompareExtension):
    def __init__(
        self, test_function: Callable | None = None, reliability: float = 0.05
    ):
        super().__init__()
        self.test_function = test_function
        self.reliability = reliability

    @staticmethod  # TODO: remove
    def check_other(other: Dataset | None) -> Dataset:
        pass

    @staticmethod
    def check_dataset(data: Dataset):
        pass

    def check_data(self, data: Dataset, other: Dataset | None) -> Dataset:
        pass

    def _calc_pandas(
        self, data: Dataset, other: Dataset | None = None, **kwargs
    ) -> Dataset | float:
        pass


class TTestExtension(StatTest):
    def __init__(self, reliability: float = 0.05):
        super().__init__(ttest_ind, reliability=reliability)

    def _calc_pandas(
        self, data: Dataset, other: Dataset | None = None, **kwargs
    ) -> Dataset | float:
        pass


class KSTestExtension(StatTest):
    def __init__(self, reliability: float = 0.05):
        super().__init__(ks_2samp, reliability=reliability)

    def _calc_pandas(
        self, data: Dataset, other: Dataset | None = None, **kwargs
    ) -> Dataset | float:
        pass


class UTestExtension(StatTest):
    def __init__(self, reliability: float = 0.05):
        super().__init__(mannwhitneyu, reliability=reliability)

    def _calc_pandas(
        self, data: Dataset, other: Dataset | None = None, **kwargs
    ) -> Dataset | float:
        pass


class Chi2TestExtension(StatTest):
    @staticmethod
    def mini_category_replace(counts: Dataset) -> Dataset:
        pass

    def matrix_preparation(self, data: Dataset, other: Dataset) -> Dataset | None:
        pass

    def _calc_pandas(
        self, data: Dataset, other: Dataset | None = None, **kwargs
    ) -> Dataset | float:
        pass


class NormCDF(StatTest):
    def _calc_pandas(
        self, data: Dataset, other: Dataset | None = None, **kwargs
    ) -> Dataset | float:
        pass
