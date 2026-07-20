from __future__ import annotations

from copy import deepcopy
from typing import Any

from ..dataset.dataset import Dataset, ExperimentData
from ..dataset.roles import StatisticRole, TargetRole
from .abstract import Transformer


class CUPEDTransformer(Transformer):
    def __init__(
        self,
        cuped_features: dict[str, str],
        key: Any = "",
    ):
        """
        Transformer that applies the CUPED adjustment to target features.

        Args:
            cuped_features (dict[str, str]): A mapping {target_feature: pre_target_feature}.
        """
        super().__init__(key=key)
        self.cuped_features = cuped_features

    @staticmethod
    def _inner_function(
        data: Dataset,
        cuped_features: dict[str, str],
    ) -> Dataset:
        pass

    @classmethod
    def calc(cls, data: Dataset, cuped_features: dict[str, str], **kwargs) -> Dataset:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
