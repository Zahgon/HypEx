from __future__ import annotations

import warnings
from abc import ABC, abstractmethod
from typing import Any, Literal

from ..dataset import (
    ABCRole,
    AdditionalTargetRole,
    Dataset,
    DatasetAdapter,
    ExperimentData,
    GroupingRole,
    InfoRole,
    PreTargetRole,
    StatisticRole,
    TargetRole,
    TempTargetRole,
)
from ..executor import Calculator
from ..utils import (
    NAME_BORDER_SYMBOL,
    BackendsEnum,
    ExperimentDataEnum,
    FromDictTypes,
    GroupingDataType,
)
from ..utils.errors import (
    AbstractMethodError,
    NoColumnsError,
    NoRequiredArgumentError,
    NotSuitableFieldError,
)


class Comparator(Calculator, ABC):
    def __init__(
        self,
        compare_by: Literal[
            "groups", "columns", "columns_in_groups", "cross", "matched_pairs"
        ],
        grouping_role: ABCRole | None = None,
        target_roles: ABCRole | list[ABCRole] | None = None,
        baseline_role: ABCRole | None = None,
        key: Any = "",
        calc_kwargs: dict[str, Any] = {},
    ):
        super().__init__(key=key)
        self.grouping_role = grouping_role or GroupingRole()
        self.compare_by = compare_by
        self.target_roles = target_roles or TargetRole()
        self.baseline_role = baseline_role or PreTargetRole()
        self.calc_kwargs = calc_kwargs

    @property
    def search_types(self) -> list[type] | None:
        pass

    def _local_extract_dataset(
        self, compare_result: dict[Any, Any], roles: dict[Any, ABCRole]
    ) -> Dataset:
        pass

    @classmethod
    @abstractmethod
    def _inner_function(
        cls, data: Dataset, test_data: Dataset | None = None, **kwargs
    ) -> Any:
        raise AbstractMethodError

    def _get_fields_data(self, data: ExperimentData) -> dict[str, Dataset]:
        pass

    @classmethod
    def _execute_inner_function(
        cls,
        baseline_data: list[tuple[str, Dataset]],
        compared_data: list[tuple[str, Dataset]],
        compare_by: Literal[
            "groups", "columns", "columns_in_groups", "cross", "matched_pairs"
        ],
        **kwargs,
    ) -> dict:
        pass

    @staticmethod
    def _check_test_data(test_data: Dataset | None = None) -> Dataset:
        pass

    def _set_value(
        self, data: ExperimentData, value: Dataset | None = None, key: Any = None
    ) -> ExperimentData:
        pass

    @staticmethod
    def _extract_dataset(
        compare_result: FromDictTypes, roles: dict[Any, ABCRole]
    ) -> Dataset:
        pass

    @staticmethod
    def _grouping_data_split(
        grouping_data: dict[str, Dataset],
        compare_by: Literal[
            "groups", "columns", "columns_in_groups", "cross", "matched_pairs"
        ],
        target_fields: list[str],
        baseline_field: str | None = None,
    ) -> GroupingDataType:
        pass

    @staticmethod
    def _split_ds_into_columns(
        data: list[tuple[str, Dataset]],
    ) -> list[tuple[str, Dataset]]:
        pass

    @staticmethod
    def _field_validity_check(
        field_data: Dataset,
        comparison_role: Literal[
            "group_field_data", "target_fields_data", "baseline_field_data"
        ],
        compare_by: Literal[
            "groups", "columns", "columns_in_groups", "cross", "matched_pairs"
        ],
    ) -> Dataset:
        pass

    @classmethod
    def _split_for_groups_mode(
        cls,
        group_field_data: Dataset,
        target_fields_data: Dataset,
    ) -> GroupingDataType:
        pass

    @classmethod
    def _split_for_columns_mode(
        cls,
        baseline_field_data: Dataset,
        target_fields_data: Dataset,
    ) -> GroupingDataType:
        pass

    @classmethod
    def _split_for_columns_in_groups_mode(
        cls,
        group_field_data: Dataset,
        baseline_field_data: Dataset,
        target_fields_data: Dataset,
    ) -> GroupingDataType:
        pass

    @classmethod
    def _split_for_cross_mode(
        cls,
        group_field_data: Dataset,
        baseline_field_data: Dataset,
        target_fields_data: Dataset,
    ) -> GroupingDataType:
        pass

    @classmethod
    def _split_for_matched_pairs_mode(
        cls,
        group_field_data: Dataset,
        baseline_field_data: Dataset,
        target_fields_data: Dataset,
    ) -> GroupingDataType:
        pass

    @classmethod
    def _split_data_to_buckets(
        cls,
        compare_by: Literal[
            "groups", "columns", "columns_in_groups", "cross", "matched_pairs"
        ],
        target_fields_data: Dataset,
        baseline_field_data: Dataset,
        group_field_data: Dataset,
    ) -> GroupingDataType:
        pass

    @classmethod
    def calc(
        cls,
        compare_by: (
            Literal["groups", "columns", "columns_in_groups", "cross", "matched_pairs"]
            | None
        ) = None,
        target_fields_data: Dataset | None = None,
        baseline_field_data: Dataset | None = None,
        group_field_data: Dataset | None = None,
        grouping_data: (
            tuple[list[tuple[str, Dataset]]] | list[tuple[str, Dataset]] | None
        ) = None,
        **kwargs,
    ) -> dict:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass


class StatHypothesisTesting(Comparator, ABC):
    def __init__(
        self,
        compare_by: Literal[
            "groups", "columns", "columns_in_groups", "cross", "matched_pairs"
        ],
        grouping_role: ABCRole | None = None,
        target_role: ABCRole | None = None,
        baseline_role: ABCRole | None = None,
        reliability: float = 0.05,
        key: Any = "",
        calc_kwargs: dict[str, Any] = {},
    ):
        super().__init__(
            compare_by=compare_by,
            grouping_role=grouping_role,
            target_roles=target_role,
            baseline_role=baseline_role,
            key=key,
            calc_kwargs=calc_kwargs,
        )
        self.reliability = reliability
