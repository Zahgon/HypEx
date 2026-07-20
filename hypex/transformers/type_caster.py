from __future__ import annotations

from typing import Any, Sequence

from ..dataset.dataset import Dataset, ExperimentData
from ..dataset.roles import ABCRole, FeatureRole
from .abstract import Transformer


class TypeCaster(Transformer):
    def __init__(
        self,
        dtype: dict[str, type] | dict[type, type],
        roles: ABCRole | Sequence[ABCRole] | None = None,
        key: Any = "",
    ):
        super().__init__(key=key)
        self.dtype = dtype
        self.roles = roles or FeatureRole()

    @staticmethod
    def _inner_function(
        data: Dataset,
        dtype: dict[str, type],
    ) -> Dataset:
        pass

    @classmethod
    def calc(
        cls,
        data: Dataset,
        dtype: dict[str, type] | dict[type, type],
        roles: ABCRole | Sequence[ABCRole] | None = None,
        **kwargs,
    ):
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
