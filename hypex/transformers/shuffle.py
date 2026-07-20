from __future__ import annotations

from typing import Any

from ..dataset import Dataset, ExperimentData
from ..executor.executor import Calculator


class Shuffle(Calculator):
    def __init__(
        self,
        random_state: int | None = None,
        key: Any = "",
    ):
        super().__init__(key)
        self.random_state = random_state

    @staticmethod
    def _inner_function(data: Dataset, random_state: int | None = None) -> Dataset:
        pass

    def generate_params_hash(self):
        pass

    def execute(self, data: ExperimentData) -> ExperimentData:
        pass
