from __future__ import annotations

from itertools import product
from typing import Any, Sequence

from tqdm import tqdm

from ..dataset import ABCRole, Dataset, ExperimentData, GroupingRole
from ..executor import Executor, IfExecutor
from ..reporters import DatasetReporter, Reporter
from ..utils.enums import ExperimentDataEnum
from .base import Experiment


class ExperimentWithReporter(Experiment):
    def __init__(
        self,
        executors: Sequence[Executor],
        reporter: Reporter,
        transformer: bool | None = None,
        key: str = "",
    ):
        super().__init__(executors, transformer, key)
        self.reporter = reporter

    def one_iteration(
        self, data: ExperimentData, key: str = "", set_key_as_index: bool = False
    ):
        pass

    def _set_result(
        self, data: ExperimentData, result: list[Dataset], reset_index: bool = True
    ):
        pass


class CycledExperiment(ExperimentWithReporter):
    def __init__(
        self,
        executors: list[Executor],
        reporter: DatasetReporter,
        n_iterations: int,
        transformer: bool | None = None,
        key: str = "",
    ):
        super().__init__(executors, reporter, transformer, key)
        self.n_iterations: int = n_iterations

    def generate_params_hash(self) -> str:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass


class GroupExperiment(ExperimentWithReporter):
    def __init__(
        self,
        executors: Sequence[Executor],
        reporter: Reporter,
        searching_role: ABCRole = GroupingRole(),
        transformer: bool | None = None,
        key: str = "",
    ):
        self.searching_role = searching_role
        super().__init__(executors, reporter, transformer, key)

    def generate_params_hash(self) -> str:
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass


class ParamsExperiment(ExperimentWithReporter):
    def __init__(
        self,
        executors: Sequence[Executor],
        reporter: DatasetReporter,
        params: dict[type, dict[str, Sequence[Any]]],
        transformer: bool | None = None,
        key: str = "",
    ):
        super().__init__(executors, reporter, transformer, key)
        self._params = params
        self._flat_params: list[dict[type, dict[str, Any]]] = []

    def generate_params_hash(self) -> str:
        pass

    def _update_flat_params(self):
        pass

    @property
    def flat_params(self) -> list[dict[type, dict[str, Any]]]:
        pass

    @property
    def params(self) -> dict[type, dict[str, Sequence[Any]]]:
        pass

    @params.setter
    def params(self, params: dict[type, dict[str, Sequence[Any]]]):
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass


class IfParamsExperiment(ParamsExperiment):
    def __init__(
        self,
        executors: Sequence[Executor],
        reporter: DatasetReporter,
        params: dict[type, dict[str, Sequence[Any]]],
        stopping_criterion: IfExecutor,
        transformer: bool | None = None,
        key: str = "",
    ):
        self.stopping_criterion = stopping_criterion
        super().__init__(executors, reporter, params, transformer, key)

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
