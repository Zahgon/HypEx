from __future__ import annotations

from copy import deepcopy
from typing import Any, Iterable, Sequence

from ..dataset import ABCRole, AdditionalTargetRole, ExperimentData, TempTargetRole
from ..executor import Executor
from ..utils import ExperimentDataEnum


class Experiment(Executor):
    def _detect_transformer(self) -> bool:
        pass

    def get_executor_ids(
        self, searched_classes: type | Iterable[type] | None = None
    ) -> dict[type, list[str]]:
        pass

    def __init__(
        self,
        executors: Sequence[Executor],
        transformer: bool | None = None,
        key: Any = "",
    ):
        self.executors: Sequence[Executor] = executors
        self.transformer: bool = (
            transformer if transformer is not None else self._detect_transformer()
        )
        super().__init__(key)

    def set_params(self, params: dict[str, Any] | dict[type, dict[str, Any]]) -> None:
        pass

    def _set_value(self, data: ExperimentData, value, key=None) -> ExperimentData:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass


class OnRoleExperiment(Experiment):
    def __init__(
        self,
        executors: list[Executor],
        role: ABCRole | Sequence[ABCRole],
        transformer: bool | None = None,
        key: Any = "",
    ):
        self.role: list[ABCRole] = [role] if isinstance(role, ABCRole) else list(role)
        super().__init__(executors, transformer, key)

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
