from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from ..dataset import (
    AdditionalTreatmentRole,
    Dataset,
    ExperimentData,
    StratificationRole,
    TreatmentRole,
)
from ..dataset.roles import ConstGroupRole
from ..executor import Calculator
from ..utils import ExperimentDataEnum


class AASplitter(Calculator):
    def __init__(
        self,
        control_size: float = 0.5,
        random_state: int | None = None,
        sample_size: float | None = None,
        constant_key: bool = True,
        save_groups: bool = True,
        groups_sizes: list[float] | None = None,
        key: Any = "",
    ):
        self.control_size = control_size
        self.random_state = random_state
        self._key = key
        self.constant_key = constant_key
        self.save_groups = save_groups
        self.sample_size = sample_size
        self.groups_sizes = groups_sizes
        super().__init__(key)

    def _generate_params_hash(self):
        pass

    def init_from_hash(self, params_hash: str):
        pass

    @property
    def key(self) -> Any:
        pass

    @key.setter
    def key(self, value: Any):
        pass

    def _set_value(self, data: ExperimentData, value, key=None) -> ExperimentData:
        pass

    @staticmethod
    def _inner_function(
        data: Dataset,
        random_state: int | None = None,
        control_size: float = 0.5,
        groups_sizes: list[float] | None = None,
        sample_size: float | None = None,
        const_group_field: str | None = None,
        **kwargs,
    ) -> list[str]:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass


class AASplitterWithStratification(AASplitter):
    @staticmethod
    def _inner_function(
        data: Dataset,
        random_state: int | None = None,
        control_size: float = 0.5,
        grouping_fields=None,
        **kwargs,
    ) -> list[str] | Dataset:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass




