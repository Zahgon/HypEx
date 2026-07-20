from __future__ import annotations

from copy import deepcopy
from typing import Any, Literal

import numpy as np

from ..dataset import (
    ABCRole,
    AdditionalMatchingRole,
    AdditionalTargetRole,
    Dataset,
    ExperimentData,
    FeatureRole,
    InfoRole,
    TargetRole,
)
from ..extensions.scipy_stats import NormCDF
from ..utils.enums import ExperimentDataEnum
from ..utils.errors import NoneArgumentError
from .abstract import GroupOperator


class SMD(GroupOperator):
    def execute(self, data: ExperimentData) -> ExperimentData:
        pass

    @classmethod
    def _inner_function(
        cls, data: Dataset, test_data: Dataset | None = None, **kwargs
    ) -> Any:
        pass


class MatchingMetrics(GroupOperator):
    def __init__(
        self,
        grouping_role: ABCRole | None = None,
        target_roles: ABCRole | list[ABCRole] | None = None,
        metric: Literal["auto", "atc", "att", "ate"] | None = None,
        n_neighbors: int = 1,
        key: Any = "",
    ):
        self.metric = metric or "auto"
        self.n_neighbors = n_neighbors
        self.__scaled_counts = {}
        target_roles = target_roles or TargetRole()
        super().__init__(
            grouping_role=grouping_role,
            target_roles=(
                target_roles if isinstance(target_roles, list) else [target_roles]
            ),
            key=key,
        )

    def _calc_scaled_counts(self, matches, indexes, group):
        pass

    @staticmethod
    def _calc_vars(value):
        pass

    @staticmethod
    def _calc_se(var_c, var_t, scaled_counts, group=None):
        pass

    @classmethod
    def _inner_function(
        cls,
        data: Dataset,
        test_data: Dataset | None = None,
        target_fields: list[str] | None = None,
        **kwargs,
    ) -> Any:
        pass

    @classmethod
    def _execute_inner_function(
        cls, grouping_data, target_fields: list[str] | None = None, **kwargs
    ) -> dict:
        pass

    def _prepare_new_target(
        self,
        data: ExperimentData,
        t_data: Dataset,
        group_field: str,
    ) -> Dataset:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass


class Bias(GroupOperator):
    def __init__(
        self,
        grouping_role: ABCRole | None = None,
        target_roles: list[ABCRole] | None = None,
        key: Any = "",
    ):
        super().__init__(
            grouping_role=grouping_role, target_roles=target_roles, key=key
        )

    @staticmethod
    def calc_coefficients(X: Dataset, Y: Dataset) -> list[float]:
        pass

    @staticmethod
    def calc_bias(
        X: Dataset, X_matched: Dataset, coefficients: list[float]
    ) -> list[float]:
        pass

    @classmethod
    def _inner_function(
        cls,
        data: Dataset,
        test_data: Dataset | None = None,
        target_fields: list[str] | None = None,
        features_fields: list[str] | None = None,
        **kwargs,
    ) -> dict:
        pass

    @classmethod
    def _execute_inner_function(
        cls,
        grouping_data,
        target_fields: list[str] | None = None,
        features_fields: list[str] | None = None,
        **kwargs,
    ) -> dict:
        pass

    @staticmethod
    def prepare_data(data: ExperimentData, t_data: Dataset) -> Dataset:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
