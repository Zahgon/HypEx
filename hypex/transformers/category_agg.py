from __future__ import annotations

from typing import Any, Sequence

from ..dataset.dataset import Dataset, ExperimentData
from ..dataset.roles import FeatureRole
from ..utils import CategoricalTypes
from ..utils.adapter import Adapter
from .abstract import Transformer


class CategoryAggregator(Transformer):
    def __init__(
        self,
        target_roles: str | Sequence[str] | None = None,
        threshold: int | None = 15,
        new_group_name: str | None = None,
        key: Any = "",
    ):
        super().__init__(key=key)
        self.target_roles = target_roles or FeatureRole()
        self.threshold = threshold
        self.new_group_name = new_group_name

    @property
    def search_types(self):
        pass

    @staticmethod
    def _inner_function(
        data: Dataset,
        target_cols: str | None = None,
        threshold: int | None = 15,
        new_group_name: str | None = None,
    ) -> Dataset:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
