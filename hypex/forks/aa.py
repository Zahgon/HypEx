from __future__ import annotations

from ..analyzers.aa import OneAAStatAnalyzer
from ..executor.executor import Executor, IfExecutor
from ..utils.enums import ExperimentDataEnum


class IfAAExecutor(IfExecutor):
    def __init__(
        self,
        if_executor: Executor | None = None,
        else_executor: Executor | None = None,
        sample_size: float | None = None,
        key: str = "",
    ):
        self.sample_size = sample_size
        super().__init__(if_executor, else_executor, key)

    def check_rule(self, data, **kwargs) -> bool:
        pass
