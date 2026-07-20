from __future__ import annotations

from typing import Any, Sequence

from ..dataset.dataset import Dataset, ExperimentData
from ..dataset.roles import FeatureRole, InfoRole, PreTargetRole, TargetRole
from ..utils.adapter import Adapter
from .abstract import Transformer


class CVFilter(Transformer):
    def __init__(
        self,
        target_roles: str | Sequence[str] | None = None,
        lower_bound: float | None = None,
        upper_bound: float | None = None,
        key: Any = "",
    ):
        """Initialize coefficient of variation filter of the columns in which it does not fit into the defined borders.

        Args:
            lower_bound:
                The minimum acceptable coefficient of variation below which we consider the column to be constant
            upper_bound:
                The maximum acceptable coefficient of variation above which we consider the to be incorrect
        """
        super().__init__(key=key)
        self.target_roles = target_roles or FeatureRole()
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.type_filter: bool = True

    @property
    def search_types(self):
        pass

    @staticmethod
    def _inner_function(
        data: Dataset,
        target_cols: str | None = None,
        lower_bound: float | None = None,
        upper_bound: float | None = None,
    ) -> Dataset:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass


class ConstFilter(Transformer):
    def __init__(
        self,
        target_roles: str | Sequence[str] | None = None,
        threshold: float = 0.95,
        key: Any = "",
    ):
        """Initialize constants filter of the values which occur more often than defined by threshold.

        Args:
            target:
                The column or columns to be filtered
            threshold:
                The maximum acceptable frequency above which we consider the column to be constant
        """
        super().__init__(key=key)
        self.target_roles = target_roles or FeatureRole()
        self.threshold = threshold

    @staticmethod
    def _inner_function(
        data: Dataset,
        target_cols: str | None = None,
        threshold: float = 0.95,
    ) -> Dataset:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass


class NanFilter(Transformer):
    def __init__(
        self,
        target_roles: str | Sequence[str] | None = None,
        threshold: float = 0.8,
        key: Any = "",
    ):
        """Initialize filter of the columns in which NaN occurs more often than defined by threshold.

        Args:
            target:
                The column or columns to be filtered
            threshold:
                The maximum acceptable frequency of NaN values in a column
        """
        super().__init__(key=key)
        self.target_roles = target_roles or FeatureRole()
        self.threshold = threshold

    @staticmethod
    def _inner_function(
        data: Dataset,
        target_cols: str | None = None,
        threshold: float = 0.8,
    ) -> Dataset:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass


class CorrFilter(Transformer):
    def __init__(
        self,
        target_roles: str | Sequence[str] | None = None,
        corr_space_roles: str | Sequence[str] | None = None,
        threshold: float = 0.8,
        method: str = "pearson",
        numeric_only: bool = True,
        key: Any = "",
    ):
        super().__init__(key=key)
        self.target_roles = target_roles or FeatureRole()
        self.corr_space_roles = corr_space_roles or [FeatureRole(), TargetRole()]
        self.threshold = threshold
        self.method = method
        self.numeric_only = numeric_only

    @staticmethod
    def _inner_function(
        data: Dataset,
        target_cols: str | None = None,
        corr_space_cols: str | None = None,
        threshold: float = 0.8,
        method: str = "pearson",
        numeric_only: bool = True,
        drop_policy: str = "cv",
    ) -> Dataset:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass


class OutliersFilter(Transformer):
    def __init__(
        self,
        target_roles: str | Sequence[str] | None = None,
        lower_percentile: float = 0,
        upper_percentile: float = 1,
        key: Any = "",
    ):
        """Initialize outliers filter of the values laying beyond the given percentile and NaNs.

        Args:
            target:
                The name of target column to be filtered from outlier values
            percentile:
                The value of the percentile to filter outliers
        """
        super().__init__(key=key)
        self.target_roles = target_roles or FeatureRole()
        self.lower_percentile = lower_percentile
        self.upper_percentile = upper_percentile

    @property
    def search_types(self):
        pass

    @staticmethod
    def _inner_function(
        data: Dataset,
        target_cols: str | None = None,
        lower_percentile: float = 0,
        upper_percentile: float = 1,
    ) -> Dataset:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
