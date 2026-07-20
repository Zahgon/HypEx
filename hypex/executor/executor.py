from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Sequence

from ..dataset import (
    ABCRole,
    AdditionalMatchingRole,
    Dataset,
    ExperimentData,
    FeatureRole,
    GroupingRole,
    TargetRole,
)
from ..utils import (
    ID_SPLIT_SYMBOL,
    AbstractMethodError,
    ExperimentDataEnum,
    NotSuitableFieldError,
    SetParamsDictTypes,
)
from ..utils.adapter import Adapter


class Executor(ABC):
    def __init__(
        self,
        key: Any = "",
        **calc_kwargs,
    ):
        self._id: str = ""
        self._params_hash = ""

        self.key: Any = key
        self._generate_id()
        self.calc_kwargs = calc_kwargs

    def check_and_setattr(self, params: dict[str, Any]):
        pass

    def _generate_params_hash(self):
        pass

    def _generate_id(self):
        pass

    def set_params(self, params: SetParamsDictTypes) -> None:
        pass

    def init_from_hash(self, hash: str) -> None:
        pass

    @classmethod
    def build_from_id(cls, executor_id: str):
        pass

    @property
    def id(self) -> str:
        pass

    @property
    def key(self) -> Any:
        pass

    @key.setter
    def key(self, value: Any):
        pass

    @property
    def params_hash(self) -> str:
        pass

    @property
    def id_for_name(self) -> str:
        pass

    @property
    def _is_transformer(self) -> bool:
        pass

    def _set_value(
        self, data: ExperimentData, value: Any, key: Any = None
    ) -> ExperimentData:
        pass

    @abstractmethod
    def execute(self, data: ExperimentData) -> ExperimentData:
        raise AbstractMethodError


class Calculator(Executor, ABC):
    @classmethod
    def calc(cls, data: Dataset, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def _inner_function(data: Dataset, **kwargs) -> Any:
        raise AbstractMethodError

    @property
    def search_types(self):
        raise AbstractMethodError

    @staticmethod
    def _check_test_data(
        test_data: Dataset | None = None,
    ) -> Dataset:  # TODO to move away from Calculator. Where to?
        pass


class MLExecutor(Calculator, ABC):
    def __init__(
        self,
        grouping_role: ABCRole | None = None,
        target_role: ABCRole | None = None,
        key: Any = "",
    ):
        self.target_role = target_role or TargetRole()
        super().__init__(key=key)
        self.grouping_role = grouping_role or GroupingRole()

    def _get_fields(self, data: ExperimentData):
        pass

    @abstractmethod
    def fit(self, X: Dataset, Y: Dataset | None = None) -> MLExecutor:
        raise NotImplementedError

    @abstractmethod
    def predict(self, X: Dataset) -> Dataset:
        raise NotImplementedError

    def score(self, X: Dataset, Y: Dataset) -> float:
        raise NotImplementedError

    @property
    def search_types(self):
        pass

    @classmethod
    @abstractmethod
    def _inner_function(
        cls,
        data: Dataset,
        test_data: Dataset | None = None,
        target_data: Dataset | None = None,
        **kwargs,
    ) -> Any:
        raise AbstractMethodError

    @classmethod
    def _execute_inner_function(
        cls,
        grouping_data,
        target_field: str | None = None,
        **kwargs,
    ) -> Any:
        pass

    def _set_value(
        self, data: ExperimentData, value: Any, key: Any = None
    ) -> ExperimentData:
        pass

    @classmethod
    def calc(
        cls,
        data: Dataset,
        group_field: Sequence[str] | str | None = None,
        grouping_data: list[tuple[str, Dataset]] | None = None,
        target_field: str | list[str] | None = None,
        features_fields: str | list[str] | None = None,
        **kwargs,
    ) -> Dataset:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass


class IfExecutor(Executor, ABC):
    def __init__(
        self,
        if_executor: Executor | None = None,
        else_executor: Executor | None = None,
        key: Any = "",
    ):
        self.if_executor = if_executor
        self.else_executor = else_executor
        super().__init__(key)

    @abstractmethod
    def check_rule(self, data, **kwargs) -> bool:
        raise AbstractMethodError

    def _set_value(
        self, data: ExperimentData, value: Any, key: Any = None
    ) -> ExperimentData:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
