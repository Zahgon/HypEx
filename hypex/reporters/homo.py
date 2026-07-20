from __future__ import annotations

from typing import Any

from ..dataset import Dataset, ExperimentData
from .aa import OneAADictReporter
from .abstract import DatasetReporter


class HomoDictReporter(OneAADictReporter):
    def report(self, data: ExperimentData) -> dict[str, Any]:
        pass


class HomoDatasetReporter(DatasetReporter):
    def __init__(self):
        super().__init__(dict_reporter=HomoDictReporter(front=False))

    @staticmethod
    def convert_to_dataset(data: dict) -> dict[str, Dataset] | Dataset:
        pass
