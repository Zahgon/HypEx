from __future__ import annotations

from abc import abstractmethod
from typing import Any, Sequence

from ..dataset import (
    ABCRole,
    AdditionalTargetRole,
    Dataset,
    ExperimentData,
    GroupingRole,
    TargetRole,
)
from ..executor import Calculator
from ..utils import AbstractMethodError, ExperimentDataEnum, NotSuitableFieldError
from ..utils.adapter import Adapter


class GroupOperator(
    Calculator
):  # TODO: change the derive from Calculator to COmparator
    def __init__(
        self,
        grouping_role: ABCRole | None = None,
        target_roles: ABCRole | list[ABCRole] | None = None,
        key: Any = "",
    ):
        super().__init__(key=key)
        self.target_roles = target_roles or TargetRole()
        self.grouping_role = grouping_role or GroupingRole()

    @property
    def search_types(self):
        pass

    @classmethod
    @abstractmethod
    def _inner_function(
        cls, data: Dataset, test_data: Dataset | None = None, **kwargs
    ) -> Any:
        raise AbstractMethodError

    def _get_fields(self, data: ExperimentData):
        pass

    @classmethod
    def _execute_inner_function(
        cls,
        grouping_data,
        target_fields: list[str] | None = None,
        **kwargs,
    ) -> dict:
        pass

    @classmethod
    def calc(
        cls,
        data: Dataset,
        group_field: Sequence[str] | str | None = None,
        grouping_data: list[tuple[str, Dataset]] | None = None,
        target_fields: str | list[str] | None = None,
        **kwargs,
    ) -> dict:
        pass

    def _set_value(
        self, data: ExperimentData, value: dict | None = None, key: Any = None
    ) -> ExperimentData:
        pass
