from __future__ import annotations

from typing import Any, Sequence

from ..dataset import Dataset, ExperimentData, FeatureRole
from ..executor import Calculator
from ..utils import (
    NAME_BORDER_SYMBOL,
    AbstractMethodError,
    CategoricalTypes,
    ExperimentDataEnum,
)


class Encoder(Calculator):
    def __init__(
        self,
        target_roles: str | Sequence[str] | None = None,
        key: Any = "",
    ):
        self.target_roles = target_roles or FeatureRole()
        self._key = key
        super().__init__(key)

    @property
    def __is_encoder(self):
        pass

    @property
    def search_types(self):
        pass

    def _get_ids(self, col_name):
        pass

    def _ids_to_names(self, col_names: list[str]):
        pass

    @staticmethod
    def _inner_function(data: Dataset, **kwargs) -> Dataset:
        raise AbstractMethodError

    def _set_value(
        self, data: ExperimentData, value: Dataset, key=None
    ) -> ExperimentData:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
