from __future__ import annotations

from ..dataset import Dataset
from ..extensions.scipy_stats import (
    Chi2TestExtension,
    KSTestExtension,
    TTestExtension,
    UTestExtension,
)
from ..utils.constants import NUMBER_TYPES_LIST
from .abstract import StatHypothesisTesting


class TTest(StatHypothesisTesting):

    @property
    def search_types(self) -> list[type] | None:
        pass

    @classmethod
    def _inner_function(
        cls, data: Dataset, test_data: Dataset | None = None, **kwargs
    ) -> Dataset:
        pass


class KSTest(StatHypothesisTesting):

    @property
    def search_types(self) -> list[type] | None:
        pass

    @classmethod
    def _inner_function(
        cls, data: Dataset, test_data: Dataset | None = None, **kwargs
    ) -> Dataset:
        pass


class UTest(StatHypothesisTesting):

    @property
    def search_types(self) -> list[type] | None:
        pass

    @classmethod
    def _inner_function(
        cls, data: Dataset, test_data: Dataset | None = None, **kwargs
    ) -> Dataset:
        pass


class Chi2Test(StatHypothesisTesting):

    @property
    def search_types(self) -> list[type] | None:
        pass

    @classmethod
    def _inner_function(
        cls, data: Dataset, test_data: Dataset | None = None, **kwargs
    ) -> Dataset:
        pass
